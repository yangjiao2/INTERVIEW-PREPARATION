20% design & build
20% service & network
20% deployment
25% env, configuration, security
15: observability

browser shell:
ctrl c, ctrl v not work: control insert, shift insert
k alias and bash autocompletion
``` bash
## kub completion
k completion -h
source < (kubectl completion bash)

echo "source <(kubectl completion bash)" >> ~/.bashrc
source ~/.bashrc

# shortversion of api resources
kubectl api-resources | more

## helm
echo 'source <(helm completion bash)' >> ~/.bash_profile

## alias
alias k=kubectl
alias kg="k get"

## context
kubectl config use-context challenge-context

# -L (or --label-columns) 
# -l (or --selector) 
# --show-labels option to display all labels 
k get pods -L k8s-app -l k8s-app!=kube-proxy

k get pos -n kube-system --sort-by='{.metadata.createTimestamp}'

# .items[*] as results are json array, * for index which stands for all
k get pods -n kube-system --sort-by='{.status.podIP}' -o jsonpath='{.items[*].status.podIP}'

k get pods -n kube-system --sort-by='{.status.podIP}' -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'

# export remove cluster specific lines
k get pod -n kube-system kube-proxy-pod -o yaml --export > pod.yaml


k scale deployment web-server --replicas=6
k rollout status deployment web-server
k rollout undo deployment web-server

k set image deployment web-server httpd=httpd:2.4.38-alpine

# load balancer allows communication with clients outside of the Kubernetes cluster
k expose deployment web-server --type=LoadBalancer --port=80


# Get the Cluster IP of the service
service_ip=$(kubectl get service web -o jsonpath='{.spec.clusterIP}')
# Use curl to send an HTTP request to the service
curl $service_ip
```


```bash
# debug and monitor

kubectl get events -n default
kubectl top pods -n kube-system

# with label selector to show only resource utilization for Pods with a k8s-app=kube-dns label:
kubectl top pod -n kube-system --containers -l k8s-app=kube-dns




```

### probes:
```yml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-tcp
spec:
  containers:
  - name: liveness
    image: busybox:1.30.1
    ports:
    - containerPort: 8888
    # Listen on port 8888 for 30 seconds, then sleep
    command: ["/bin/sh", "-c"]
    args: ["timeout 30 nc -p 8888 -lke echo hi && sleep 600"]
    livenessProbe:
      tcpSocket:
        port: 8888
      initialDelaySeconds: 3
      periodSeconds: 5
---
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: readiness
  name: readiness-http
spec:
  containers:
  - name: readiness
    image: httpd:2.4.38-alpine
    ports:
    - containerPort: 80
    # Sleep for 30 seconds before starting the server
    command: ["/bin/sh","-c"]
    args: ["sleep 30 && httpd-foreground"]
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 3
      periodSeconds: 3

```

## resources

```yml
spec:
  containers:
  - name: cpu-load
    resources:
      requests:
        cpu: "1.7"

```
### security context:
pod.spec:
    fsGroup(integer)/runAsGroup(integer)

pod.spec.containers:
    allowPriviliedgeEscalation(bool)/priviledged
    readOnlyRootFilesystem
    runAsGroup(integer)

```yaml
spec:
  containers:
    securityContext:
      privileged: true  # run as sudp
```

### environment variable:
```bash
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

      env:
        - name: API_URL
          # DNS for service discovery
          # Naming pattern:
          #   IP address: <service_name>.<service_namespace>
          #   Port: needs to be extracted from SRV DNS record
          value: http://app-tier.service-discovery:8080

```

- service discovery
service must created before pod
service also must be in the same namespace



### configmaps &  secret

```bash
# ConfigMap from two literal key-value pairs:

k create configmap app-config --from-literal=DB_NAME=testdb \
  --from-literal=COLLECTION_NAME=messages

# generic secret
kubectl create secret generic app-secret --from-literal=password=123457
```

cm on pod:
```yml
  volumes:
  - name: config
    # Declare the configMap to use for the volume
    configMap:
      name: app-config


        volumeMounts:
          - mountPath: /etc/redis
            name: config
      volumes:
        - name: config
          configMap:
            name: redis-config
            items:
            - key: config
              path: redis.conf
```

secret on pod:
```yml
    env:
    - name: PASSWORD      # Name of environment variable
      valueFrom:
        secretKeyRef:
          name: app-secret  # Name of secret
          key: password     # Name of secret key
```

use `kubectl exec pod-secret -- /bin/sh -c 'echo $PASSWORD'` to get the env value

### deployment

```yml
kind: Deployment
spec:
  selector:
    matchLabels:
      app: microservice
  templates: # pod templates
    metadata: # does not need pod name
      labels: # pod labels
        app: microservice
```

```bash
# scale
k scale -n namesapce deployment app-tier --replicas=5
# autoscale
k autoscale deployment app-tier --max=5, --min=1 --cpu-percent=70
```


### PV & PVC

PVC needs to bound to "Bound" to a PV.
```yml
kind: PersistentVolumeClaim
spec:
  # Only one node can mount the volume in Read/Write
  # mode at a time
  accessModes:
  - ReadWriteOnce 
  resources:
    requests:
      storage: 2Gi


```

pod claim PV
```yml
kind: Pod

spec:
  containers:
  - image: mongo:4.0.6
    # Mount as volume 
    volumeMounts:
    - name: data
      mountPath: /data/db
  volumes:
  - name: data
    # Declare the PVC to use for the volume
    persistentVolumeClaim:
      claimName: db-data
```

RECLAIM POLICY associated with the PV. The Delete policy means the PV is deleted once the PVC is deleted

PV:
```yml
spec:
  capacity:
    storage:  1Gi
```

PVC:
```yml
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 128Mi

```



### service account
```bash
# Each Namespace has a default ServiceAccount.
# Service account is bound to pod on creation.

kubectl create serviceaccount app-sa
```

```yml
kind: Pod
spec:
  serviceAccount: app-sa

```

### volumes

- ephemeral volume
lifetime tied to the lifetime of the Pod 
data does survive across container restarts
use case:  read-only input, configmaps and secrets

```yml
kind: Pod
spec:
  containers:
  - name: cache
    image: redis:6.2.5-alpine
    resources:
      requests:
        ephemeral-storage: "1Ki"
      limits:
        ephemeral-storage: "1Ki"
    volumeMounts:
    - name: ephemeral
      mountPath: "/data"
  volumes:
    - name: ephemeral
      emptyDir:
        sizeLimit: 1Ki
```

result of above:
After the Pod is Started, its container exceeds the ephemeral storage limit set (Usage of EmptyDir volume "ephemeral" exceeds the limit "1Ki"). The kubelet then evicts the Pod and it is subsequently killed

### network policy

```bash
kubectl get networkpolicy deny-metadata -o yaml
```

```yaml

spec:
  - Egress
  egress:
    - to: #     - from:
      - ipBlock:
        cidr:
        except:
        - 123.345.567.789

  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app-tier: cache
    ports:
    - port: 80

```
also has namespaceSelector, podSelector

### rollout rollback

```bash

k rollout status deployment [deployment_name]
k rollout pause/resume

k rollout undo deployment [deployment_names]
```

### init containers

run in order of declaration

### other
editor:
tmux:
```tmux
ctrl b + % to split
ctrl b + <- or -> to switch between window

```

vim:
```
:set nu to set line number visible
:[line_number]
:%s/ [origin_text] [replaced_text]

```
YAML json processing: 
jq

testing:
curl / wget -O for testing web service

documentation:
man

allowed web:
kub doc, kub github, kub blog
kubectl cheat sheet: https://jamesdefabia.github.io/docs/user-guide/kubectl-cheatsheet/
official doc: https://kubernetes.io/docs/home/ 