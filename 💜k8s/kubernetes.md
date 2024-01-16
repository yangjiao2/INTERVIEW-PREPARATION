## Overview

1. [Architecture](#architecture)
2. [Deploy a Stateless Application in a Kubernetes Cluster](#deploy-a-stateless-application-in-a-kubernetes-cluster)
3. use alias

```bash
alias k=kubectl
alias kg="k get"
```
---

fully-managed
- amazon EKS

full control
- kubespray
- kops
- kubeadm


## Architecture

- clusters:
    - machines
    - nodes: works and masters
        - master node: control plane
            - control plane schedules containers onto nodes
            - scheduling decisions

- pods:
    - +1 containers
    - smallest building block
    - all pods share container network
    - 1 IP address per pod

- services:
    - networking rules
    - use labels to select a group of pods
    - fixed IP address
    - expose pods port (to internet or other pods)

- deployments:
    - manage configuration changes to run pods
    - horizontal scaling: roll out and roll back

### kubectl

```bash
# create/delete resource (pods, services, etc)
kubectl create [-f]
kubectl delete

kubectl get pods / deployments / services

kubectl describe

# print container logs
kubectl logs

# explain resource field by using the explain command. The pattern for the command is, e.g: kubectl explain Pod.spec.containers.image
kubectl explain <Resource_Kind>.<Path_To_Field>

kubectl get pod first-pod -o yaml | more

# watch it change
kubectl get pods -w 

# grab pod info
pod_node=$(kubectl get pod coin-toss -o jsonpath='{.status.hostIP}')
pod_id=$(kubectl get pod coin-toss -o jsonpath='{.metadata.uid}')

## --   : exec in the container
## wc -l: count lines
kubectl exec coin-toss -- wc -l /var/log/tosses.txt

```

---

## manifest


[](./assets/manifests.png)

### Network

- services controller for accessing pods
- scope to namespace

`kubectl get pods -n network-policy -L app, region

```yml
spec:
    podSelector:
        matchLabels:
            app: server
    policyTypes:
    - Ingress
    - Egress
    ingress: # rules for traffic come from
    - from:
        # podSelector, nameSelector, ipBlock (range of ip)
        - podSelector:
            matchLabels:
                region: us-west
        ports: 
        # if not present, allow all ports
        - protocol: TCP
        post: 8888
```

IPblock

```yml
spec:
    podSelector:
        matchLabels:
            app: server
    
    policyTypes:
    - Egress
    egress:
    - to:
        - ipBlock:
            cidr: 0.0.0.0/0
            except:
            - 192.168.134.72/32


```



### Pods

```yml
apiVersion: v2
kind: Pod
metadata:
    name: nginx-pod
spec:
    containers:
    - name: mycontainer
      image: nginx: latest
      resources:
        requests:
            memory:
            cpu: "0.5" # half of cpu

        limits:
            memory:
            cpu: "0.5" # half of cpu
      port:
        - containerPort:
```

when using `kubectl describe` to examine
- can check state, IP, node, port, events



labels:
-  identify resources
- annotations can not be used for selection

Use the -L (or --label-columns) kubectl get option to display columns for both labels:

`kubectl get pods -L color,tier`

Pods that do not based on color label
`kubectl get pods -L color,tier -l color`
`kubectl get pods -L color,tier -l 'color=red'`
`kubectl get pods -L color,tier -l 'color in (blue,green)'`

- selector

A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches
all objects. A null label selector matches no objects.

### Service
```yml
apiVersion: v1
kind: Service
metadata:
    lables:
        app: webserver
    name: webserver

spec:
    ports:
        - port: 80
    selector: # find pod to match against, target app = webserver
        app: webserver
    type: NodePort  # NodePort expose access from outside of cluster. ClusterIP is for access for internal cluster.
```

type = NodePort: defines port on each cluster, allow access from outside of cluster



when using `kubectl describe` to examine
- can check port, nodeport, endpoints

`-A [\d]`: shows the information including number of lines after (this example is 1): `kubectl describe nodes | grep -i address -A 1`


### Namespace

- RBAC access for namespace
- seperate resources


```yml
apiVersion: v1
kind: Namespace
metadata:
    name: microservice
    labels: 
        app: counter

```

### Service discovery

```yml
apiVersion: v1
kind: Service
metadata:
  name: app-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 8080
  selector:
    tier: app
---
apiVersion: v1
kind: Pod
metadata:
  name: app-tier
  labels:
    app: microservices
    tier: app
spec:
  containers:
    - name: server
      image: lrakai/microservices:server-v1
      ports:
        - containerPort: 8080
      env:
        - name: REDIS_URL
          # Environment variable service discovery
          # Naming pattern:
          #   IP address: <all_caps_service_name>_SERVICE_HOST
          #   Port: <all_caps_service_name>_SERVICE_PORT
          #   Named Port: <all_caps_service_name>_SERVICE_PORT_<all_caps_port_name>
          value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
          # In multi-container example value was
          # value: redis://localhost:6379 
```

`kubectl create -f multi_container.yaml -n microservice` to initiate with namespace

`kubectl logs -n microservice app counter --tail 10` to view the last 10 line of logs 



- environment variables
    - injected in container
    - for environment variable to be set, service name should be not up to enable to be found (e.g, data tier, app tier depends on query data tier below)
    - if service is in the same namespace, e.g: service-name.service-namespace:port
- DNS
    - auto create
    - configuration auto route


- data tier

```yml
apiVersion: v1
kind: Service
metadata:
  name: data-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 6379
    protocol: TCP # default 
    name: redis # optional when only 1 port
  selector:
    tier: data 
  type: ClusterIP # default
---
apiVersion: v1
kind: Pod
metadata:
  name: data-tier
  labels:
    app: microservices
    tier: data
spec:
  containers:
    - name: redis
      image: redis:latest
      imagePullPolicy: IfNotPresent
      ports:
        - containerPort: 6379

```

- app tier: where it uses "DATA_TIER_SERVICE_HOST" and "DATA_TIER_SERVICE_PORT_REDIS" 

```yml
apiVersion: v1
kind: Service
metadata:
  name: app-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 8080
  selector:
    tier: app
---
apiVersion: v1
kind: Pod
metadata:
  name: app-tier
  labels:
    app: microservices
    tier: app
spec:
  containers:
    - name: server
      image: lrakai/microservices:server-v1
      ports:
        - containerPort: 8080
      env:
        - name: REDIS_URL
          # Environment variable service discovery
          # Naming pattern:
          #   IP address: <all_caps_service_name>_SERVICE_HOST
          #   Port: <all_caps_service_name>_SERVICE_PORT
          #   Named Port: <all_caps_service_name>_SERVICE_PORT_<all_caps_port_name>
          value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
          # In multi-container example value was
          # value: redis://localhost:6379 
```


support tier
```yml
apiVersion: v1
kind: Pod
metadata:
  name: support-tier
  labels:
    app: microservices
    tier: support
spec:
  containers:

    - name: counter
      image: lrakai/microservices:counter-v1
      env:
        - name: API_URL
          # DNS for service discovery
          # Naming pattern:
          #   IP address: <service_name>.<service_namespace>
          #   Port: needs to be extracted from SRV DNS record
          value: http://app-tier.service-discovery:8080

    - name: poller
      image: lrakai/microservices:poller-v1
      env:
        - name: API_URL
          # omit namespace to only search in the same namespace
          value: http://app-tier:$(APP_TIER_SERVICE_PORT)
```




### Autoscaling

top pod resource utilization
`kubectl top pods -n deployments`


resource updates on existing deployment
`kubectl apply -f app-tier-with-cpu-utilization.yaml -n deployment` 

```yml
apiVersion: v1
kind: Service
metadata:
  name: app-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 8080
  selector:
    tier: app
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-tier
  labels:
    app: microservices
    tier: app
spec:
  replicas: 5
  selector:
    matchLabels:
      tier: app
  template:
    metadata:
      labels:
        app: microservices
        tier: app
    spec:
      containers:
      - name: server
        image: lrakai/microservices:server-v1
        ports:
          - containerPort: 8080
        resources:
          requests:
            cpu: 20m # 20 milliCPU / 0.02 CPU
        env:
          - name: REDIS_URL
            # Environment variable service discovery
            # Naming pattern:
            #   IP address: <all_caps_service_name>_SERVICE_HOST
            #   Port: <all_caps_service_name>_SERVICE_PORT
            #   Named Port: <all_caps_service_name>_SERVICE_PORT_<all_caps_port_name>
            value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
            # In multi-container example value was
            # value: redis://localhost:6379 
```

containers with resource (cpu request) is required to enable autoscale


```yml
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: app-tier
  labels:
    app: microservices
    tier: app
spec:
  maxReplicas: 5
  minReplicas: 1
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app-tier
  targetCPUUtilizationPercentage: 70  # target average cpu across replicas
  # decrease if < 63% and incrase if 77% 


```
Equivalent to
`kubectl autoscale deployment app-tier --max=5 --min=1 --cpu-percent=70`

check on resource
`kubectl api-resources` group by api group. short name on 2nd column
`kubectl get -n deployments hpa`

edit manifest
`kubectl edit`


### rolling update and rollback

scale back
`kubectl scale -n deployments deployment app-tier --replicas=1`


#### Probe

- Liveness
- Ready

server might be live, but not ready for request
for example,
Data Tier (Redis)
- liveness (open TCP request)
- readiness (redis-cli pint command)

App Tier (Server)
- liveness
- readiness (setup ready for request)


- Readiness probes: needs more time to become ready to serve traffic => the Service will not serve traffic to any Pods that have a failing readiness probe. 

- Liveness probes: fails to make progress after entering a broken state, such as deadlock => restart the Pod and allow progress to be made, compared to leaving the Pod in the broken state.

- Startup probes: starts slowly. The startup probe runs before both readiness and liveness probes. startup time that is longer than the time needed to detect a broken state for a container.



`kubectl explain pod.spec.containers.readinessProbe`:
- exec <Object>: action to take
- grpc <Object>: GRPC port
- httpGet <Object>: http request to perform
- initialDelaySeconds
- periodSeconds: How often (in seconds) to perform the probe
- successThreshold
- failureThreshold
- tcpSocket <Object>:
- terminationGracePeriodSeconds
- timeoutSeconds

The number of consecutive successes is configured via the ***successThreshold*** field and the number of consecutive failures required to transition from success to failure is ***failureThreshold***. The probe runs every ***periodSeconds*** and each probe will wait up to ***timeoutSeconds*** to complete.


```yml

    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 3
```


```yml

  livenessProbe:
      tcpSocket:
        port: 8888
      initialDelaySeconds: 3
      periodSeconds: 5
```


```yml
apiVersion: v1
kind: Service
metadata:
  name: data-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 6379
    protocol: TCP # default 
    name: redis # optional when only 1 port
  selector:
    tier: data 
  type: ClusterIP # default
---
apiVersion: apps/v1 # apps API group
kind: Deployment
metadata:
  name: data-tier
  labels:
    app: microservices
    tier: data
spec:
  replicas: 1
  selector:
    matchLabels:
      tier: data
  template:
    metadata:
      labels:
        app: microservices
        tier: data
    spec: # Pod spec
      containers:
      - name: redis
        image: redis:latest
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 6379
            name: redis  # using name to avoid ovverride
        livenessProbe:
          tcpSocket:
            port: redis # named port
          initialDelaySeconds: 15
        readinessProbe:
          exec:
            command:
            - redis-cli
            - ping
          initialDelaySeconds: 5
```

generally liveness probe has longer delay period to ensure not early kill the container
liveness probe will check 3 times before marking it failed

```yml
apiVersion: v1
kind: Service
metadata:
  name: app-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 8080
  selector:
    tier: app
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-tier
  labels:
    app: microservices
    tier: app
spec:
  replicas: 1
  selector:
    matchLabels:
      tier: app
  template:
    metadata:
      labels:
        app: microservices
        tier: app
    spec:
      containers:
      - name: server
        image: lrakai/microservices:server-v1
        ports:
          - containerPort: 8080
            name: server
        env:
          - name: REDIS_URL
            # Environment variable service discovery
            # Naming pattern:
            #   IP address: <all_caps_service_name>_SERVICE_HOST
            #   Port: <all_caps_service_name>_SERVICE_PORT
            #   Named Port: <all_caps_service_name>_SERVICE_PORT_<all_caps_port_name>
            value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
            # In multi-container example value was
            # value: redis://localhost:6379 
          - name: DEBUG
            value: express:*
        livenessProbe:
          httpGet:
            path: /probe/liveness
            port: server
          initialDelaySeconds: 5 ## dummy request for 200
        readinessProbe:
          httpGet:
            path: /probe/readiness
            port: server
          initialDelaySeconds: 3
```

`kubectl logs -n probes app-tier-123123123123 | cut -d' ' -f5, 8-11`

#### resource

    resources:
      limits:
        cpu: "0.5" # half a core
        memory: "20Mi" # 20 mebibytes 
      requests:
        cpu: "0.35" # 35% of a core
        memory: "10Mi" # 20 mebibytes


`kubectl get pods -o wide` and to check pods `kubectl top nodes` / `kubectl top pods`

Containers that exceed their memory limits will be terminated and restarted if possible.
Containers that exceed their memory request may be evicted when the node runs out of memory.
Containers that exceed their CPU limits may be allowed to exceed the limit depending on the other Pods on the node. Containers will not be terminated for exceeding CPU limits.
### Deployment

```bash

# Create namespace
kubectl create namespace deployment
# Set namespace as the default for the current context
kubectl config set-context $(kubectl config current-context) --namespace=deployment


kubectl create deployment --image=httpd:2.4.38 web-server --dry-run=client -o yaml

#  without the dry run to actually create the Deployment
kubectl create deployment --image=httpd:2.4.38 web-server

# replicas in the Deployment to six (6):
kubectl scale deployment web-server --replicas=6


# view the Deployment's rollout history
kubectl rollout history deployment web-server

# --record option will record the command as an annotation i
kubectl edit deployment web-server --record

kubectl set image deployment web-server httpd=httpd:2.4.38-alpine

# Rollback
kubectl rollout undo deployment web-server

# create service with exposed DNS address
kubectl expose deployment web-server --type=LoadBalancer --port=80

watch kubectl get services

# check logs `kubectl logs <POD_NAME> <CONTAINER_NAME>
kubectl logs pod-logs server 

# display the most recent log (--tail=1) including the timestamp and stream (-f for follow) 
kubectl logs -f --tail=1 --timestamps pod-logs client

# check last 10 line of a file
kubectl exec webserver-logs -- tail -10 conf/httpd.conf

# address <POD_NAME>:<PATH>
kubectl cp webserver-logs:conf/httpd.conf local-copy-of-httpd.conf

# output array result in table and remove table cells before & after
... --output table | tr -d \|

# resource usage
kubectl top pods -n kube-system
kubectl top pod -n kube-system --containers  #  NAME column refers to container names.
kubectl top pod -n kube-system --containers -l k8s-app=kube-dns

# get service hostname
kubectl get service app -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'

```

ubuntu@ip-10-0-128-5:~$ kubectl get service
NAME         TYPE           CLUSTER-IP     EXTERNAL-IP                                                             PORT(S)        AGE
web-server   LoadBalancer   10.108.61.64   a4fcb6cf758b04effbfaf727e017d05f-21816900.us-west-2.elb.amazonaws.com   80:32526/TCP   4m57s


### Jobs


Create a Job named one-off that sleeps for 30 seconds:

```
kubectl create job one-off --image=alpine -- sleep 30
```

- backoffLimit: Number of times a Job will retry before marking a Job as failed
- completions: Number of Pod completions the Job needs before being considered a success
- parallelism: Number of Pods the Job is allowed to run in parallel
- spec.template.spec.restartPolicy: Job Pods default to never attempting to restart. Instead, the Job is responsible for managing the restart of failed Pods.



- completionMode       <string>
     completionMode specifies how Pod completions are tracked. It can be
     `NonIndexed` (default) or `Indexed`.

     `NonIndexed` means that the Job is considered complete when there have been
     .spec.completions successfully completed Pods. Each Pod completion is
     homologous to each other.

     `Indexed` means that the Pods of a Job get an associated completion index
     from 0 to (.spec.completions - 1), available in the annotation
     batch.kubernetes.io/job-completion-index. The Job is considered complete
     when there is one successfully completed Pod for each index. When value is
     `Indexed`, .spec.completions must be specified and `.spec.parallelism` must
     be less than or equal to 10^5. In addition, The Pod name takes the form
     `$(job-name)-$(index)-$(random-string)`, the Pod hostname takes the form
     `$(job-name)-$(index)`.


```yml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: cronjob-example
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - image: alpine
            name: fail
            command: ['date']
          restartPolicy: Never
```

use `watch kubectl describe cronjob cronjob-example` to see its start every min

### Daemonsets
- create pod
- one pod per node



### init containers

- run in order
- images are available
- block start of application
- run EVERY pod created (failed pod will also run init containers)


```yml
apiVersion: v1
kind: Service
metadata:
  name: app-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 8080
  selector:
    tier: app
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-tier
  labels:
    app: microservices
    tier: app
spec:
  replicas: 1
  selector:
    matchLabels:
      tier: app
  template:
    metadata:
      labels:
        app: microservices
        tier: app
    spec:
      containers:
      - name: server
        image: lrakai/microservices:server-v1
        ports:
          - containerPort: 8080
            name: server
        env:
          - name: REDIS_URL
            # Environment variable service discovery
            # Naming pattern:
            #   IP address: <all_caps_service_name>_SERVICE_HOST
            #   Port: <all_caps_service_name>_SERVICE_PORT
            #   Named Port: <all_caps_service_name>_SERVICE_PORT_<all_caps_port_name>
            value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
            # In multi-container example value was
            # value: redis://localhost:6379 
          - name: DEBUG
            value: express:*
        livenessProbe:
          httpGet:
            path: /probe/liveness
            port: server
          initialDelaySeconds: 5
        readinessProbe:
          httpGet:
            path: /probe/readiness
            port: server
          initialDelaySeconds: 3
      initContainers: 
        - name: await-redis
          image: lrakai/microservices:server-v1
          env:
          - name: REDIS_URL
            value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
          command: # rewrite default command
            - npm
            - run-script
            - await-redis # will block until connection established

```


#### ephemeral volume
- Sharing data between containers in a Pod (multi-container Pods)
- Providing read-only input configuration data to a Pod
- Temporary data caches (container restart erase data)
- Best use: ConfigMaps and Secrets

```yml

    # Mount the log directory /var/log using a volume
    volumeMounts:
    - name: varlog
      mountPath: /var/log
  # Declare log directory volume an emptyDir ephemeral volume
  volumes:
  - name: varlog
    emptyDir: {}
      sizeLimit: 1Ki

```

to access the file
```sh
pod_node=$(kubectl get pod coin-toss -o jsonpath='{.status.hostIP}')
pod_id=$(kubectl get pod coin-toss -o jsonpath='{.metadata.uid}')
ssh $pod_node -oStrictHostKeyChecking=no sudo ls /var/lib/kubelet/pods/$pod_id/volumes/kubernetes.io~empty-dir/varlog
```

`medium: Memory` => data will not survive Node restarts


when sizeLimit reach the max, pod lose READY state

```bash
  Normal   Created    110s  kubelet            Created container cache
  Normal   Started    110s  kubelet            Started container cache
  Warning  Evicted    101s  kubelet            Usage of EmptyDir volume "ephemeral" exceeds the limit "1Ki".
  Normal   Killing    101s  kubelet            Stopping container cache
```

#### claim (PVC)

```yml
kind: PersistentVolumeClaim
metadata:
  name: db-data
spec:
  # Only one node can mount the volume in Read/Write
  # mode at a time
  accessModes:
  - ReadWriteOnce 
  resources:
    requests:
      storage: 2Gi
```
`kubectl get pvc` Status: change from `Pending` to `Bound`

after creation of pvc, `kubectl get pv`, PV is created automatically.
RECLAIM POLICY associated is `Delete`: means the PV is deleted once the PVC is deleted.


```yml
kind: Pod
metadata:
  name: db 
spec:
  containers:
  - image: mongo:4.0.6
    name: mongodb
    # Mount as volume 
    volumeMounts:
    - name: data
      mountPath: /data/db
    ports:
    - containerPort: 27017
      protocol: TCP
  volumes:
  - name: data
    # Declare the PVC to use for the volume
    persistentVolumeClaim:
      claimName: db-data
```

MongoDB stores its database files at `/data/db` by default.



#### Persistent Volume (PV)
- Pods claim PV resources through Persistent Volume Claims (PVCs)
- 


`kubectl exec -n deployment data-tier-12343242 -it -- /bin/bash`
exec `kill 1` to exit database, since only 1 process will always be redis, so PID would be `1`


then check `kubectl log -n deployments poller`
counter restart


```yml

apiVersion: v1
kind: Service
metadata:
  name: data-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 6379
    protocol: TCP # default 
    name: redis # optional when only 1 port
  selector:
    tier: data 
  type: ClusterIP # default
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: data-tier-volume
spec:
  capacity:
    storage: 1Gi # 1 gibibyte
  accessModes:
    - ReadWriteOnce # write and read by single node
  awsElasticBlockStore: 
    volumeID: INSERT_VOLUME_ID # replace with actual ID
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-tier-volume-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 128Mi # 128 mebibytes 
---
apiVersion: apps/v1 # apps API group
kind: Deployment
metadata:
  name: data-tier
  labels:
    app: microservices
    tier: data
spec:
  replicas: 1
  selector:
    matchLabels:
      tier: data
  template:
    metadata:
      labels:
        app: microservices
        tier: data
    spec: # Pod spec
      containers:
      - name: redis
        image: redis:latest
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 6379
            name: redis
        livenessProbe:
          tcpSocket:
            port: redis # named port
          initialDelaySeconds: 15
        readinessProbe:
          exec:
            command:
            - redis-cli
            - ping
          initialDelaySeconds: 5
        volumeMounts:
          - mountPath: /data  # where redis configure for its data
            name: data-tier-volume
      volumes:
      - name: data-tier-volume
        persistentVolumeClaim:
          claimName: data-tier-volume-claim

```

PVC has requirements and access mode, which is used to check on the if available  PV satisfy

use `aws ec2 decribe-volumes --region=us-west-2 --filters="Name=tag:Type,Values=PV"` to query volume id

check on the lines `cat pv-data-tier.yaml | grep INSERT -C5` to check on before and after 5 lines

### config maps & secret

- data stoer in key-value pairs
- config maps & secrets can be used as Volumes or Env variables

```yml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-conf
  namespace: cloudacademy
data:
  nginx.conf: |-
    #CODE1.0:
    #add the nginx.conf configuration - this will be referenced within the deployment.yaml
    #CODE1.0:
    #add the nginx.conf configuration - this will be referenced within the deployment.yaml
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://localhost:5000/;
            proxy_set_header Host "localhost";
        }
    }

```


```yml
apiVersion: v1
kind: ConfigMap
metadata:
  name: redis-config
data:
  config: | # YAML for multi-line string
    # Redis config file
    tcp-keepalive 240
    maxmemory 1mb

```

```yml
apiVersion: v1
kind: Service
metadata:
  name: data-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 6379
    protocol: TCP # default 
    name: redis # optional when only 1 port
  selector:
    tier: data 
  type: ClusterIP # default
---
apiVersion: apps/v1 # apps API group
kind: Deployment
metadata:
  name: data-tier
  labels:
    app: microservices
    tier: data
spec:
  replicas: 1
  selector:
    matchLabels:
      tier: data
  template:
    metadata:
      labels:
        app: microservices
        tier: data
    spec: # Pod spec
      containers:
      - name: redis
        image: redis:latest
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 6379
            name: redis
        livenessProbe:
          tcpSocket:
            port: redis # named port
          initialDelaySeconds: 15
        readinessProbe:
          exec:
            command:
            - redis-cli
            - ping
          initialDelaySeconds: 5
        command: # command to load configuration
          - redis-server
          - /etc/redis/redis.conf
        volumeMounts:
          - mountPath: /etc/redis
            name: config
      volumes:
        - name: config
          configMap: # type: configMap, secret
            name: redis-config # for secret, "name" will change to "secretName"
            items: # declare which key value pair to use from configmaps
            - key: config
              path: redis.conf # path of mount value 

```

to check
`-it -- bin/bash` onto pod
then `cat /etc/redis/redis.conf`

to check on redis configuration using redis cli
`kubectl exec -n config data-tier-1234312341234 -it -- redis-cli CONFIG GET tcp-keepalive`

`kubectl rollout -n config restart deployment data-tier`

```yml
apiVersion: v1
kind: Secret
metadata:
  name: app-tier-secret
stringData: # unencoded data
  api-key: LRcAmM1904ywzK3esX
  decoded: hello
data: #for base-64 encoded data
  encoded: aGVsbG8= # hello in base-64

# api-key secret (only) is equivalent to
# kubectl create secret generic app-tier-secret --from-literal=api-key=LRcAmM1904ywzK3esX
```

to use the secret, need to use "valueFrom" to "secretKeyRef"

```yml
apiVersion: v1
kind: Service
metadata:
  name: app-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 8080
  selector:
    tier: app
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-tier
  labels:
    app: microservices
    tier: app
spec:
  replicas: 1
  selector:
    matchLabels:
      tier: app
  template:
    metadata:
      labels:
        app: microservices
        tier: app
    spec:
      containers:
      - name: server
        image: lrakai/microservices:server-v1
        ports:
          - containerPort: 8080
            name: server
        env:
          - name: REDIS_URL
            # Environment variable service discovery
            # Naming pattern:
            #   IP address: <all_caps_service_name>_SERVICE_HOST
            #   Port: <all_caps_service_name>_SERVICE_PORT
            #   Named Port: <all_caps_service_name>_SERVICE_PORT_<all_caps_port_name>
            value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
            # In multi-container example value was
            # value: redis://localhost:6379 
          - name: DEBUG
            value: express:*
          - name: API_KEY
            valueFrom:
              secretKeyRef:
                name: app-tier-secret
                key: api-key # key is the name of the key
        livenessProbe:
          httpGet:
            path: /probe/liveness
            port: server
          initialDelaySeconds: 5
        readinessProbe:
          httpGet:
            path: /probe/readiness
            port: server
          initialDelaySeconds: 3
      initContainers:
        - name: await-redis
          image: lrakai/microservices:server-v1
          env:
          - name: REDIS_URL
            value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
          command:
            - npm
            - run-script
            - await-redis
```


--- 


display ConfigMap

```bash
kubectl create configmap app-config --from-literal=DB_NAME=testdb \
  --from-literal=COLLECTION_NAME=messages

kubectl get configmaps app-config -o yaml
```

create a ConfigMap from two literal key-value pairs
```yml
kubectl create configmap app-config --from-literal=DB_NAME=testdb \
  --from-literal=COLLECTION_NAME=messages

```

mount ConfigMap using a volume
```yml
cat << 'EOF' > pod-configmap.yaml
apiVersion: v1
kind: Pod
metadata:
  name: db 
spec:
  containers:
  - image: mongo:4.0.6
    name: mongodb
    # Mount as volume 
    volumeMounts:
    - name: config
      mountPath: /config
    ports:
    - containerPort: 27017
      protocol: TCP
  volumes:
  - name: config
    # Declare the configMap to use for the volume
    configMap:
      name: app-config
EOF
kubectl create -f pod-configmap.yaml
```

check on key & name
```yml
kubectl exec db -it -- ls /config
kubectl exec db -it -- cat /config/DB_NAME && echo
```

generic key-value pair Secret 
`kubectl create secret generic app-secret --from-literal=password=123457`


Confirm the secret value is base-64 encoded by decoding it:
```yml
kubectl get secret app-secret -o jsonpath="{.data.password}" \
  | base64 --decode \
  && echo

```yml

cat << EOF > pod-secret.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: pod-secret
spec:
  containers:
  - image: busybox:1.30.1
    name: busybox
    args:
    - sleep
    - "3600"
    env:
    - name: PASSWORD      # Name of environment variable
      valueFrom:
        secretKeyRef:
          name: app-secret  # Name of secret
          key: password     # Name of secret key
EOF

```

`kubectl create -f pod-secret.yaml`
`kubectl exec pod-secret -- /bin/sh -c 'echo $PASSWORD'`


### etcd

The etcdctl command (see spec.template.spec.containers.args) requires the certificate authority certificate, a client key, and a client certificate to encrypt the etcd traffic. kubeadm configures etcd to listen to HTTPS only as a security best practice. The snapshot save command creates a snapshot of the entire key-value store at the given location (/snapshots/backup.db).

```yml
cat <<EOF | kubectl create -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: backup
  namespace: management
spec:
  template:
    spec:
      containers:
      # Use etcdctl snapshot save to create a snapshot in the /snapshot directory 
      - command:
        - /bin/sh 
        args:
        - -ec
        - etcdctl --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/peer.crt --key=/etc/kubernetes/pki/etcd/peer.key snapshot save /snapshots/backup.db
        # The same image used by the etcd pod
        image: registry.k8s.io/etcd:3.5.9-0
        name: etcdctl
        env:
        # Set the etcdctl API version to 3 (to match the version of etcd installed by kubeadm)
        - name: ETCDCTL_API
          value: '3'
        volumeMounts:
        - mountPath: /etc/kubernetes/pki/etcd
          name: etcd-certs
          readOnly: true
        - mountPath: /snapshots
          name: snapshots
      # Use the host network where the etcd port is accessible (etcd pod uses host network)
      # This allows the etcdctl to connect to etcd that is listening on the host network
      hostNetwork: true
      affinity:
        # Use node affinity to schedule the pod on the control-plane (where the etcd pod is)
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: node-role.kubernetes.io/control-plane
                operator: Exists
      restartPolicy: OnFailure
      tolerations:
      # tolerate the control-plane's NoSchedule taint to allow scheduling on the control-plane
      - effect: NoSchedule
        operator: Exists
      volumes:
      # Volume storing the etcd PKI keys and certificates
      - hostPath:
          path: /etc/kubernetes/pki/etcd
          type: DirectoryOrCreate
        name: etcd-certs
      # A volume to store the backup snapshot
      - hostPath:
          path: /snapshots
          type: DirectoryOrCreate
        name: snapshots
EOF
```

API access control
-  deploy stored in the cluster's data store (etcd) once the request is accepted 
-  three layers of access control 
1. Authentication: Requests sent to the API server are authenticated to prove the identity of the requester, be it a normal user or a service account, and are rejected otherwise.
2. Authorization: The action specified in the request must be in the list of actions the authenticated user is allowed to perform or it is rejected.
3. Admission Control: Authorized requests must then pass through all of the admission controllers configured in the cluster (excluding read-only requests) before any action is performed.


##### 1. Authentication: 
```bash
# Display the contents of the kubeconfig file:
cat /home/ubuntu/.kube/config

kubectl config --help

#  CURRENT context
kubectl config get-contexts

```

if we remove cert from `~/.kube/config` 

```
grep "client-cert" ~/.kube/config | \
  sed 's/\(.*client-certificate-data: \)\(.*\)/\2/' | \
  base64 --decode \
  > cert.pem
openssl x509 -in cert.pem -text -noout
```

by checking 
```bash
kubectl describe pod nginx
```
```yml
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
```

check on service token
```bash
kubectl exec nginx -- cat /var/run/secrets/kubernetes.io/serviceaccount/token && echo
```


#### 2. Authorization:
RBAC, subjects (users, groups, ServiceAccounts) are bound to roles and the roles describe what actions the subject is allowed to perform. There are two kinds of roles in Kubernetes RBAC:
- Role: A namespaced resource specifying allowed actions
- ClusterRole: A non-namespaced resource specifying allowed actions. non-namespaced resources, such a Nodes.



```bash
# List the Roles in all Namespaces
kubectl get roles --all-namespaces
# Roles all have an associated Namespace

```

check rules for kube-proxy role
```bash
kubectl get -n kube-system role kube-proxy -o yaml

# rules:
# - apiGroups:
#   - ""
#   resourceNames:
#   - kube-proxy
#   resources:
#   - configmaps
#   verbs:
#   - get
```
- verbs:
read (get) access to ConfigMaps (configmaps) named kube-proxy. The verbs declare which HTTP verbs are allowed for requests. 
- apiGroups:
The Kubernetes API is organized into groups and the apiGroups list indicates which API group(s) the rule applies to. 
The core API group which includes the most commonly used resources, including ConfigMaps, is denoted by an empty string ("").


---

get cluster-admin ClusterRole 
```bash
kubectl get clusterrole cluster-admin -o yaml
# rules:
# - apiGroups:
#   - '*'
#   resources:
#   - '*'
#   verbs:
#   - '*'
# - nonResourceURLs:
#   - '*'
#   verbs:
#   - '*'

```
The RoleRef map specifies the name of the ClusterRole that is being bound, and the subjects map lists all the subjects (users, groups, or service accounts) that are bound to the ClusterRole. In this case, the ClusterRole is bound to a Group named system:masters. Because identities are managed outside of Kubernetes, you cannot use kubectl to show details of users or groups. However, recall that the client certificate used in the kubeconfig identifies the user as kubernetes-admin and the group as system:masters. Because the kubernetes-admin is in the system:masters group, the cluster-admin ClusterRole allows any request sent.





#### Implement Common Deployment Strategies

- Canary deployments - A small subset of traffic is sent to the new version to build confidence in it before fully deploying the new version
- Blue/Green deployments - All traffic is cut over from the existing version, referred to as the "blue" environment, to the new version, referred to as the "green" environment
A drawback is that you need twice the amount of resources of a single environment.

```yml
apiVersion: apps/v1
kind: Deployment
spec:

  strategy:
    type: RollingUpdate # Default value is RollingUpdate, Recreate also supported

  template:
    spec:
      containers:
      - image: nginx:1.21.3-alpine
        readinessProbe:
          failureThreshold: 3 
          httpGet:
            path: /
            port: 80
            scheme: HTTP
          periodSeconds: 5
          successThreshold: 2
          timeoutSeconds: 10
```

1. green/blue

Patch the Service's selector to include both the app: web and version: old labels
```bash
cat << EOF | kubectl patch service app --patch-file /dev/stdin
spec:
  selector:
    app: web
    version: old
EOF
```

Cut over to the green environment by patching the Service to select the new version
```bash
cat << EOF | kubectl patch service app --patch-file /dev/stdin
spec:
  selector:
    app: web
    version: new
EOF
```


2. canary

kubectl delete deployment app-canary
kubectl set image deployment app-new *=caddy:2.4.5-alpine

#### Deploy a Stateless Application in a Kubernetes Cluster

check available worker node
`watch kubectl get nodes`



`kubectl get pods -l app=game` select pods with app: game label

`kubectl create -f service.yml` create based on manifest

`kubectl describe services game` describe services [Name]

scale out deploy with update on replicas
`sed -i 's/\(replicas: \).*/\12/' deployment.yml`

`kubectl apply -f deployment.yml` apply the changes

`ssh worker1 -o StrictHostKeyChecking=no "curl -s ifconfig.me; echo"`
"curl -s ifconfig.me; echo": This part of the command is the command that will be executed on the remote host after the SSH connection is established. It consists of two commands separated by a semicolon (;):

 - curl -s ifconfig.me: This command uses the curl tool to make an HTTP request to ifconfig.me, which is a service that returns your public IP address. The -s flag is used to suppress unnecessary output.

 - echo: This command is used to print a newline (echo a blank line) after the output of the previous curl command.


delete service and deployment
`kubectl delete service game && kubectl delete deployment game-deployment`

Enable autocompletion for the Kubernetes
`source <(kubectl completion bash)`


#### Taints & Tolerations

Taints
- apply to nodes
- repel pods

Tolerations
- apply to pods
- counteract taints

tolerations

```yaml
tolerations:
    - key: priority
      value: high
      effect: NoSchedule

```
```yml
tolerations:
- key: CriticalAddonOnly
  operator: Exists
- operator: Exists
- effect: NoExecute
  key: node.kubernetes.io/not-ready
  operator: Exists
- effect: NoExecute
  key: node.kubernetes.io/unreadable
  operator: Exists
- effect: NoSchedule
  key: node.kubernetes.io/disk-pressure
  operator: Exists
- effect: NoSchedule
  key: node.kubernetes.io/memory-pressure
  operator: Exists
```


node with taints will prevent pod scheduling on it. However, with tolerations,
pods should be able to schedule on the trainted nodes

`Taints: node-role.kubernetes.io/master:NoSchedule`
:<Associate>
- NoSchedule: do not schedule pods that not allow this taint
- preferNoSchedule: allow schedule the pod if no other nodes is available 
- NoExecute: NoSchedule + evict existing

DeamonSets are scheduled by deamon controller which allow pods to circumvent taint conditions

Add taint to node
`kubectl taint node ip-10-0-1-102 priority=high:NoSchedule`
> node/ip-10-0-1-1-2 taited

`kubectl create namespace scheduling`
nanespace/scheduling created

`kubectl run nginx -n scheduling --image=nginx --replicas=5`
deployment.apps/nginx created

`kubectl explain pod.spec.tolerations | more`

`kubectl run nginx -n scheduling --image=nginx --relicas=5 -o yaml`

`kubectl run nginx -n scheduling --image=nginx --replicas=5 -o yaml --dry-run > toleration.yaml`

remove taint from node
`kubectl taint node ip-10-0-1-102 priority:NoSchedule-`


###  Affinity

- operators: In, NotIn, Exists, DoesNotExist, Gt, Lt
- rules: Requirements, Preferences

1. Node affinity
```yml
spec:
    affinity:
        nodeAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms: # 1 OR more terms should be satisfied
                - matchExpressions:
                    - key: zone
                      operator: In
                      values:
                        - orange
                        - red
            preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 1 # relative importance
              preference: 
                matchExpressions:
                - key: hardware
                  operator: In
                  values:
                  - SSD

```

2. Pod affinity
- similar to node
- use running pod labels
- namespaced (pod restricted in namespace)
- top level pod affinity and anti-affinity‘；//////，，m
- topological key: zone
    - decide which node to schedule on



### Resources

`kubectl set resources deployment nginx --requests=cpu=0.25`

`kubectl patch`

imperative approach
`kubectl get deployments nginx -o yaml --export > deployment.yaml`
`vi deployments.yaml`
use `\[THINGS TO FIND]` in vim for matching keyword
`kubectl replace -f deployment.yaml --save-config` update by replace

handle difference
`kubectl get deployments nginx --
annotations in metadata is like labels

`kubectl get deployments nginx -o yaml | more`
last-applied-annotation: 3 way diff to apply desired update

`kubectl apply view-last-applied deployments nginx > last-applied.yaml`
`diff last-applied.yaml deployment.yaml`


### Networking
- Type: ClusterIP, NodePort, LoadBalance
- Ingress







## Stateful applications are applications that have a memory of what happened in the past.     

-  ConfigMaps: A type of Kubernetes resource that is used to decouple configuration arti/facts from image content to keep containerized applications portable. The configuration data is stored as key-v            alue pairs.

 
- Headless Service: A headless service is a Kubernetes service resource that won't load balance behind a single service IP. Instead, a headless service returns a list of DNS records that point directly to the pods that back the service. A headless service is defined by declaring the clusterIP property in a service spec and setting the value to None. StatefulSets currently require a headless service to identify pods in the cluster network.


- Stateful Sets: Similar to Deployments in Kubernetes, StatefulSets manage the deployment and scaling of pods given a container spec.StatefulSets differ from Deployments in that the Pods in a stateful set are not interchangeable. Each pod in a StatefulSet has a persistent identifier that it maintains across any rescheduling. The pods in a StatefulSet are also ordered. This provides a guarantee that one pod can be created before following pods. In this lab, this is useful for ensuring the MySQL primary is provisioned first.
 

- PersistentVolumes (PVs) and PersistentVolumeClaims (PVCs): PVs are Kubernetes resources that represent storage in the cluster. Unlike regular Volumes which exist only until while containing pod exists, PVs do not have a lifetime connected to a pod. Thus, they can be used by multiple pods over time, or even at the same time. Different types of storage can be used by PVs including NFS, iSCSI, and cloud-provided storage volumes, such as AWS EBS volumes. Pods claim PV resources through PVCs.


- MySQL replication: This lab uses a single primary, asynchronous replication scheme for MySQL. All database writes are handled by a single primary. The database replicas asynchronously synchronize with the primary. This means the primary will not wait for the data to be copied onto the replicas. This can improve the performance of the primary at the expense of having replicas that are not always exact copies of the primary. Many applications can tolerate slight differences in the data and are able to improve the performance of database read workloads by allowing clients to read from the replicas.






show namespaces
`kubectl get namespace`

Create the StatefulSet and start watching the associated pods:
`kubectl create -f mysql-statefulset.yaml`
`kubectl get pods -l app=mysql --watch`

`kubectl get statefulset`

Run a temporary container to use mysql to connect to the primary at mysql-0.mysql and run a few SQL commands
```
kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\
  /usr/bin/mysql -h mysql-0.mysql -e "CREATE DATABASE mydb; CREATE TABLE mydb.notes (note VARCHAR(250)); INSERT INTO mydb.notes VALUES ('k8s Cloud Academy Lab');"
```
Run a query using the mysql-read endpoint to select all of the notes in the table
```
kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\
  /usr/bin/mysql -h mysql-read -e "SELECT * FROM mydb.notes"
```


Run an SQL command that outputs the MySQL server's ID to confirm that the requests are distributed to different pods
```
kubectl run mysql-client-loop --image=mysql:5.7 -i -t --rm --restart=Never --\
  bash -ic "while sleep 1; do /usr/bin/mysql -h mysql-read -e 'SELECT @@server_id'; done"
```



running the mysql-2 pod out of service for maintenance:
`node=$(kubectl get pods --field-selector metadata.name=mysql-2 -o=jsonpath='{.items[0].spec.nodeName}')
kubectl drain $node --force --delete-emptydir-data --ignore-daemonsets`

Uncordon the node you drained so that pods can be scheduled on it again
`kubectl uncordon $node`

Delete the mysql-2 pod to simulate a node failure and watch it get rescheduled automatically 
`kubectl delete pod mysql-2`
`kubectl get pod mysql-2 -o wide --watch`

** this automatically reschudule onto drained node for load balance

Scale the number of replicas up to 5
`kubectl scale --replicas=5 statefulset mysql`  

Confirm that the data is replicated in the new mysql-4 pod
`kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\
  /usr/bin/mysql -h mysql-4.mysql -e "SELECT * FROM mydb.notes"`


Display the internal virtual IP of the mysql-read endpoint:
`kubectl get services mysql-read`

Recall the mysql-read service used the default type of ClusterIP so it is only accessible inside the cluster.

 

Append a load balancer type to the mysql-read service declaration and apply changes

`echo "  type: LoadBalancer" >> mysql-services.yaml`
`kubectl apply -f mysql-services.yaml`


Kubernetes is in the process of provisioning an elastic load balancer (ELB) to access the mysql-read service from outside the cluster.

 

After a minute, describe the mysql-read service to find the DNS name of the external load balancer endpoint:

`kubectl describe services mysql-read | grep "LoadBalancer Ingress"`
 

Use the external load balancer to send some read requests to the cluster:

```bash
load_balancer=$(kubectl get services mysql-read -o=jsonpath='{.status.loadBalancer.ingress[0].hostname}')
kubectl run mysql-client-loop --image=mysql:5.7 -i -t --rm --restart=Never --\
  bash -ic "while sleep 1; do /usr/bin/mysql -h $load_balancer -e 'SELECT @@server_id'; done"
```



#### CRD

example:  Argo CD custom resources

```bash
# get the custom resource definitions (crds) 
kubectl get crds


# enter the following to retrieve the Argo server initial password which is stored in a Secret:
kubectl -n default get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo


# The names provide the supported names you can use to reference applications when using kubectl (singular, plural, and shortNames). 
kubectl get crds applications.argoproj.io -o yaml | more | grep -C 15 spec:

kubectl edit applications [APPLICATION_NAME]

```

### Cluster

every node in a Kubernetes cluster has the following components:

- kubelet: The primary node agent that accepts pod specifications
- Container runtime: Software responsible for running containers, for example, containerd
- kube-proxy: Implements network rules and connection forwarding to enable the Kubernetes service abstraction 

control-plane nodes:

- kube-apiserver: Exposes the Kubernetes API
- etcd: Key-value store for backing cluster data
- kube-scheduler: Responsible for scheduling pods onto nodes
- kube-controller-manager: Responsible for running Kubernetes controllers, for example, the node controller that responds to changes in a node's status


1. static pods
when we delete pod / update on control plane via 

```bash
ssh control-plane

# proxy_pod_1 is a variable with the name of the first kube-proxy pod
proxy_pod_1=$(kubectl get pods -n kube-system | grep proxy | cut -d" " -f1 | head -1)
kubectl logs -n kube-system $proxy_pod_1
```

ssh onto control plane, view the static pod path
`sudo cat /var/lib/kubelet/config.yaml`

**static pods**: we see that NO changes has been made for the pod
`kubectl get pod` is actually a "mirror pod" of the real pod running on the control-plane node. The changes you make to the mirror pod are not reflected by the actual underlying pod. 


2. manifest on control-plane

list the contents of the /etc/kubernetes/manifests directory:

```bash
ls /etc/kubernetes/manifests
# etcd.yaml  kube-apiserver.yaml  kube-controller-manager.yaml  kube-scheduler.yaml
```

check on the control plane's component
```bash
for pod in "etcd" "kube-controller-manager" "kube-scheduler"; do 
  kubectl describe -n kube-system pod $pod | grep -A 5 Conditions:
done
```

addresses of the control plane and services with label kubernetes.io/cluster-service=true.
`kubectl cluster-info --help`



---


## Shortcut command

1. Install bash completion
load from completion code into shell
`source < (kubectl completion bash)`

or 
```bash
echo "source <(kubectl completion bash)" >> ~/.bashrc
source ~/.bashrc
```

via brew
`brew install bash-completion@2`
`kubectl completion bash > $(brew --prefix)/etc/bash_completion.d/kubectl


`kubectl api-resources`
FULL NAME | SHORT NAME

`kubectl get nodes -o wide`

`kubectl get po --all-namespaces`
check NAMESPACE and NAME 

show labels (at the end)
`kubectl get pods --all-namespaces --show-labels`

show with specific label 
`kubectl get pods --all-namespaces -L k8s-app -l k8s-app!=kube-proxy `


sort by creation time
`kubectl get pods -n kube-system --sort-by='{.metadata.creationTimestamp}'`

sort by podId
`kubectl get pods -n kube-system --sort-by='{.status.podId}'` 
`kubectl get pods -n kube-system -o wide` to see IP and Node

to check on the YAML structure
`kubectl get pods -n kube-system kube-proxy-12321312 --output=yaml`

to use regex jsonpath
`kubectl get pods -n kube-system --sort-by='{.status.podIP}' -o jsonpath='{.items[*].status.podIP}'`
or 
`kubectl get pods -n kube-system --sort-by='{.status.podIP}' -o jsonpath='{range .items[*]}{.metadata.name}{"\t}{.status.podIP}{"\n"}{end}'`

easy way to generate dry-run manifest file
`kubectl run nginx --image=nginx --port=80 --replicas=2 --expose --dry-run -o yaml > deployment.yaml`

check CPU and memory usage
`kubectl top pods`

explain resources
`kubectl explain pod.spec.containers.resources | more`
`kubectl explain pod.spec.containers --recursive | more`

ssh onto host
`ssh ubuntu@35.93.115.161 -oStrictHostKeyChecking=no`

connect to one of the worker nodes using SSH
`ssh -o StrictHostKeyChecking=no worker1`

check the status of the kubelet 
`sudo systemctl status kubelet`

view all of the log messages associated with kubelet service
`journalctl -u kubelet`

stop and start worker node
```bash
sudo systemctl stop kubelet
ssh worker1 'sudo systemctl start kubelet'
```

restart the worker node's kubelet with an additional option to make it detect memory pressure:
`ssh worker1 'sudo sed -i "s%\(/usr/bin/kubelet\) %\1 --eviction-hard=memory.available<3.75Gi %" /etc/systemd/system/kubelet.service.d/10-kubeadm.conf && sudo systemctl daemon-reload && sudo systemctl restart kubelet'`

restart the worker node's kubelet without the hard eviction limit option to repair the node:

`ssh worker1 'sudo sed -i "s%--eviction-hard=memory.available<3.75Gi %%" /etc/systemd/system/kubelet.service.d/10-kubeadm.conf && sudo systemctl daemon-reload && sudo systemctl restart kubelet'`


check on the condition
```bash
kubectl describe node ip-10-0-0-10 | grep -A 10 -B 2 "Conditions"
```


change the image that the kube-apiserver pod is using:

```bash
# Get the name of the kube-apiserver pod
apiserver_pod=$(kubectl get pods -n kube-system | grep apiserver | cut -d" " -f1 | head -1)
# change the pod's image to hello-world using the patch command
kubectl patch pod $apiserver_pod -n kube-system \
  -p '{"spec":{"containers":[{"name":"kube-apiserver","image":"hello-world"}]}}'
```

generate cert for users
```bash
mkdir certs  # create certificate directory
sudo openssl genrsa -out certs/andy.key 2048  # generate private key
sudo chmod 666 certs/andy.key  # make the key read & write
```



### Static pods 

- managed directly by the node's kubelet, and not by the API server (so we could not update/delete)
- configured by placing pod specifications in a manifest directory that the kubelet periodically reads to keep the pods in sync with the specifications on disk


### Kubernetes certificate signing request

references the CSR created by OpenSSL with the request key. It must be base64 encoded and have newlines stripped out (tr -d '\n')

```bash
cat > certs/andy-csr.k8s <<EOF
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: new-user-request
spec:
  signerName: kubernetes.io/kube-apiserver-client
  request: $(cat certs/andy.csr | base64 | tr -d '\n')
  usages:
  - digital signature
  - key encipherment
  - client auth
EOF
```
```bash
kubectl create -f certs/andy-csr.k8s
```

approve the CSR to generate the signed certificate:
```bash
kubectl certificate approve new-user-request
```

extract the certificate from the CSR resource object and save it to a file:
```bash
kubectl get csr new-user-request -o jsonpath='{.status.certificate}' \
  | base64 --decode > certs/andy.crt

```

create a new network admin context using the new user:
`kubectl config set-context network-admin --cluster=kubernetes --user=andy`
`kubectl config use-context network-admin`


list the network policies
`kubectl config use-context kubernetes-admin@kubernetes`
`kubectl get networkpolicy`


"cluster-admin" binding is what gives the admin user in your current kubectl context access to all the resources in the cluster
`kubectl get clusterrolebinding`


### patterns


- ambassador

The ambassador pattern uses a container to proxy communication to and from a primary container. The primary container only needs to consider connecting to localhost, while the ambassador controls proxying the connections to different environments. This is because containers in the same pod share the same network space, and can communicate with each other over localhost. 


- sidecar

The sidecar multi-container pattern uses a "sidecar" container to extend the primary container in the Pod. In the context of logging, the sidecar is a logging agent. The logging agent streams logs from the primary container, such as a web server, to a central location that aggregates logs. To allow the sidecar access to the log files, both containers mount a volume at the path of the log files. In this Lab Step, you will use an S3 bucket to collect logs. You will use a sidecar that uses Fluentd, a popular data collector often used as a logging layer, with an S3 plugin installed to stream log files in the primary container to S3.




## Kubeadm

```bash
kubeadm init to bootstrap a Kubernetes control-plane node
kubeadm join to bootstrap a Kubernetes worker node and join it to the cluster
kubeadm upgrade to upgrade a Kubernetes cluster to a newer version
kubeadm config if you initialized your cluster using kubeadm v1.7.x or lower, to configure your cluster for kubeadm upgrade
kubeadm token to manage tokens for kubeadm join
kubeadm reset to revert any changes made to this host by kubeadm init or kubeadm join
kubeadm certs to manage Kubernetes certificates
kubeadm kubeconfig to manage kubeconfig files
kubeadm version to print the kubeadm version
kubeadm alpha to preview a set of features made available for gathering feedback from the community
```

1. kube config from combine plane

```bash
mkdir .kube  # create the .kube directory
scp -o "ForwardAgent yes" control-plane:.kube/config .kube/config  # secure copy (scp) the kubeconfig file
```

kubeconfig file that you copied from the control-plane node includes:

Information about the cluster, such as the server address
Information about users to authenticate as including certificates that were generated when the cluster was created

Fields:
- clusters
- contexts
- current-context
- users


2. help

View the config commands provided by kubectl:
```bash
kubectl config --help
```


3. confirm the admin user is authorized to list all nodes:

```bash
kubectl auth can-i list nodes -A
```

The can-i command will return a binary response for whether or not a user is authorized to perform a specified action. You can learn more about the actions from the command's help page (kubectl auth can-i --help). The admin user is authorized because it is bound to an RBAC role that grants permission. Kubernetes does not store any user resources. Instead, role binding resources store information about the names of users or groups that are assigned to a role. Roles can be for a specific namespace (Role) or for an entire cluster (ClusterRole). Similarly, role bindings can be for a specific namespace (RoleBinding) or for an entire cluster (ClusterRoleBinding).



4. roles and rules 

- clusterroles
```bash
kubectl get clusterroles
kubectl get clusterrole cluster-admin -o yaml
kubectl describe clusterrole cluster-admin
```

```yml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  creationTimestamp: "2023-09-20T14:44:05Z"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: cluster-admin
  resourceVersion: "74"
  uid: a9569b5a-50c5-4d2e-bb4d-32326149d75c
rules:
- apiGroups:
  - '*'
  resources:
  - '*'
  verbs:
  - '*'
- nonResourceURLs:
  - '*'
  verbs:
  - '*'
```

```bash
kubectl describe clusterrole cluster-admin
Name:         cluster-admin
Labels:       kubernetes.io/bootstrapping=rbac-defaults
Annotations:  rbac.authorization.kubernetes.io/autoupdate: true
PolicyRule:
  Resources  Non-Resource URLs  Resource Names  Verbs
  ---------  -----------------  --------------  -----
  *.*        []                 []              [*]
             [*]                []              [*]
```
Resources: the rule applies to
Non-Resource URLs: it applies to (e.g: pods or services)
Verbs: actions that are allowed, for example get, list, and watch for read-only access

`-o yaml` option on get commands to quickly create templates from existing resources



-  clusterrolebinding
```bash
kubectl describe clusterrolebinding admin-cluster-binding
```
admin-cluster-binding cluster role 
```yml

Name:         admin-cluster-binding
Labels:       <none>
Annotations:  <none>
Role:
  Kind:  ClusterRole
  Name:  cluster-admin
Subjects:
  Kind  Name   Namespace
  ----  ----   ---------
  User  admin  
```

cluster-admin cluster role
`kubectl get clusterrolebinding cluster-admin -o yaml`

```yml

roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects: # subjects are bound to the role
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: system:masters
```


Create a cluster role resource file for network administration:

```yml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: network-admin
rules:
- apiGroups:
  - networking.k8s.io
  resources:
  - networkpolicies
  verbs:
  - '*'
- apiGroups:
  - extensions
  resources:
  - networkpolicies
  verbs:
  - '*'
```

create the network-admin cluster role
`kubectl create -f network-admin-role.yaml`

bind users in  the network-admin group to the network-admin cluster role
`kubectl create clusterrolebinding network-admin --clusterrole=network-admin --group=network-admin`


### NetworkPolicy & Network traffic



```
cat > app-policy.yaml <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-tiers
  namespace: test
spec:
  podSelector:
    matchLabels:
      app-tier: web
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app-tier: cache
    ports:
    - port: 80
EOF

```

then create nginx with specified port
`kubectl run web-server -n test -l app-tier=web --image=nginx:1.15.1 --port 80`


get the web server pod's IP address
```yaml
web_ip=$(kubectl get pod -n test -o jsonpath='{.items[0].status.podIP}')
kubectl run busybox -n test -l app-tier=cache --image=busybox --env="web_ip=$web_ip" --rm -it /bin/sh
```

success
`wget $web_ip`




#### securityContext

- privileged: as root
- readOnlyRootFilesystem: true (containers)
- runAsNonRoot: true (pod level)


the container security context overrides the setting in the pod security context when both security contexts include the same field

```yml
    securityContext:
      runAsUser: 2000
      readOnlyRootFilesystem: true

```

A best practice is to use volumes to mount any files that require modification, allowing the root file system to be read-only.


#### services account

- providing Pods with an identity in the cluster
- authenticate using ServiceAccounts and gain access to APIs that the ServiceAccount has been granted
- role-based access control (RBAC)
- each namespace a default ServiceAccount. 

`pod -o yaml | more | grep serviceAccount`
```
spec:
  serviceAccount: default
  serviceAccountName: default

```


create service account
`kubectl create serviceaccount app-sa`