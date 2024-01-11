
### installation


### infra

#### charts

Chart.yaml
charts
templates
    - ingress.yaml
    - 
values.yaml

use values:
```bash

type: {{ .Values.service.type }}
````

update values
`helm upgrade demo ./app \ --set=service.port`


templates

```bash
labels: 
    {{ include "app.labels" . | nindent 4 }}
```


dynamic generate name
```tpl
{{- define "webserver.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}
```


5) packaging:
`helm package [CHART DIRECTORY]`
product chart based on NAME and Version
e.g: cloudacademyapp-0.13.tgz


install
`helm install ca-demo1 cloudacademyapp-0.13.tgz \ -- dry-run`


host
`helm repo index .`
recursive directory scan to search for chart archive files
then write to index.yml file


install chart 
```bash
helm repo add local http://127.0.0.1:8080
helm repo update
helm search repo cloudacademy

helm install ca-demo1 local/cloudacademyapp

helm install ca-demo1 lcoal/cloudacademyapp \ --set app.color=red


```



### templates


{{ - include "webserver.labels" . | nindent 4 }}

- "-" remove white space
- "|" take output from previous
- "nindent" indent with a new line
- "indent" just indent

{{ include (print $.Template.BasePath "/configmap.yaml") . | sha265 sum }}
- "$": root



#### tutorial

1. install, unpack, list helm
```bash
### install, unpack, list
curl -O https://get.helm.sh/....

tar -xvf   helm-v3 ....

tree

sudo cp dar-win...  /usr/local/bin

## check
which helm
helm version

## auto-complete
echo 'source <(helm completion bash)' >> ~/.bash_profile

```


```bash
minikube start

# list helm
helm list

# helm search
helm search hub [package] # online hub package, e.g: wordpress

# find online
helm add ...

# list repos
helm repo list
helm repo update

helm install wordpress \
--set wordpressUserName= \
--set wordpressPassword= \
--set mariadb.mariadbPassword=

```


```bash
## check
k get all

## check URL
minikube service wordpress
```



2. create custom helm chart

```bash
helm create cloudacademy-app

tree

```

file structure
- template
----- _helper.tpl
----- configmap.yaml
- values.yaml


values.yml
```yml

replicasCount: 2

service:
    type: ClusterIP
    port: 80

autoscaling:
    enabled: false

nginx:
    conf:
        message: 'devops'

```


configmap.yml
```yml
api: v1
kind: configmap
metadata:
    name: {{ include "webserver.fullname"  . }}-config
    namespace: cloudacademy
data:
    nginx.conf: |-
        server {

            location {
                return 200 '{{ .Values.nginx.conf.message }}\n';
            }
        }


```


deployment.yml
```yml

spec:
{{ - if not .Values.autoscaling.enabled }}
    replicas: {{ .Values.replicaCount }}
{{ - end}}
    selector:
        matchLabels:
            {{ - include "webserver.selectorLabels" . | nindent 6 }}
        template:
            metadata:
                annotations:
                    # checksum config: pull in new config map when there are changes
                    checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
                labels:
                    {{- include "webserver.selectorLabels" . | nindent 8 }}
            spec:
                containers:
                    - name: {{ .Chart.Name }}
                      image: "{{ .Values.image.repository }}: {{ .Values.image.tag | default .Chart.AppVersion }}"
                      volumeMounts:
                        - name: nginx-config
                          mountPath: /etc/nginx/conf.d/default.conf
                          subPath: nginx.conf

volumes:
- name: nginx-config
  configMap:
    name: {{ include "webserver.fullname" .}}-config

```

```bash
helm hint 
# -> lint success

helm template
# check template

helm package cloudacademy-webapp
# successfully packaged ... to ...tgz

ls -la

k config set-context --current --namespace cloudacademy

helm install ca-demo1 cloudacademy-webapp-1.tgz
# $ status: deployed

k get all
# can see cluster resource

# try get request
k run --image=busybox bbox1 --restart=Never -it --rm -- /bin/sh -c "wget -qOq http://[SVC-IP-ADDRESS]/"

# --rm ensures the Pod is deleted when the shell exits.

# If you want to detach from the shell and leave it running with the ability to re-attach, omit the --rm. 
# reattach with: `kubectl attach $pod-name -c $pod-container -i -t` after you exit the shell.

helm upgrade ca-demo1 cloudacademy-webapp-1.tfz --set nginx.conf.message="updated message"
# $ status: deployed

k rollout history deployment ca-demo1-cloudacademy-webapp
# check history

helm history ca-demo1
```


3. create helm using github page

create branch 
```bash
git add README.md
git commit -m "commit"
git push -u origin master

git checkout --orphan gh-pages
git add index.yaml ...tgz
git commit -m "commit"
git push

```

on Gihub settings > "github page" > get URL
Github Page site is currently build from [YOUR BRANCH] branch.
site published as "[SITE_URL]".

```bash
# create index repository (index.yaml)
helm repo index .


ls -la

curl -i [SITE_URL]

helm repo add cloudacademy-gh-repo https://... /helm-repo

helm repo update

helm install ca-demo2 cloudacademy-gh-repo/cloudabademy-webapp --set nginx.conf.message='new message'

```


### tutorial

### 1. deployment using ConfigMaps and Helm

with in app structure
```bash

docker build -t cloudacademydevops/flaskapp .


kubectl create ns cloudacademy

kubectl config set-context --current --namespace=cloudacademy

POD_NAME=`kubectl get pods -o jsonpath='{.items[0].metadata.name}'`
echo $POD_NAME


# use the sed command to perform an inline find for the incorrect image tag "cloudacademydevops/flask" and replace it with the correct image tag "cloudacademydevops/flaskapp" within the deployment.yaml file
sed -i 's/cloudacademydevops\/flask.*/cloudacademydevops\/flaskapp/g' deployment.yaml

# service can be called via a stable cluster network VIP address
kubectl expose deployment frontend --port=80 --target-port=80

kubectl get svc frontend 

# extract the frontend service cluster IP address
FRONTEND_SERVICE_IP=`kubectl get service/frontend -o jsonpath='{.spec.clusterIP}'`
echo $FRONTEND_SERVICE_IP


FRONTEND_POD_NAME=`kubectl get pods --no-headers -o custom-columns=":metadata.name"`
echo $FRONTEND_POD_NAME

# listing directly within the NGINX container listing out the contents of the /var/log/nginx directory
kubectl exec -it $FRONTEND_POD_NAME -c nginx -- ls -la /var/log/nginx/

# check logs on nginx container and flask container

kubectl logs $FRONTEND_POD_NAME nginx
kubectl logs $FRONTEND_POD_NAME flask


```

- configmap
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
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://localhost:5000/;
            proxy_set_header Host "localhost";
        }
    }
```

- deployment
```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: cloudacademy
  labels:
    role: frontend
    env: demo
spec:
  replicas: 1
  selector:
    matchLabels:
      role: frontend
  template:
    metadata:
      labels:
        role: frontend
    spec:
      containers:
      #CODE2.0:
      #add the NGINX container to the pod - configure it to mount the nginx.conf file stored in the nginx-conf configMap 
      - name: nginx
        image: nginx:1.13.7
        imagePullPolicy: IfNotPresent
        ports:
        - name: http
          containerPort: 80
        volumeMounts:
        - name: nginx-proxy-config
          mountPath: /etc/nginx/conf.d/default.conf
          subPath: nginx.conf
      #CODE2.1:
      #add the FLASK container to the pod
      - name: flask
        image: cloudacademydevops/flaskapp
        imagePullPolicy: IfNotPresent
        ports:
        - name: http
          containerPort: 5000
        env:
        - name: APP_NAME
          value: CloudAcademy.DevOps.K8s.Manifest
      volumes:
      #CODE2.2:
      #reference the nginx-conf configMap - this will be mounted into the NGINX container
      - name: nginx-proxy-config
        configMap:
          name: nginx-conf
```


create Helm
```bash

helm create test-app

tree test-app/

# └── test-app
#     ├── charts
#     ├── Chart.yaml
#     ├── templates
#     │   ├── deployment.yaml
#     │   ├── _helpers.tpl
#     │   ├── hpa.yaml
#     │   ├── ingress.yaml
#     │   ├── NOTES.txt
#     │   ├── serviceaccount.yaml
#     │   ├── service.yaml
#     │   └── tests
#     │       └── test-connection.yaml
#     └── values.yaml


# convert the Helm templates into a single deployable Kubernetes manifest file
helm template test-app/

# exam "values.yaml" file have been injected into their respective placeholders within each of the "test-app/templates/*.yaml" files.

```


values.yaml
```yml
podSecurityContext: {}
  # fsGroup: 2000

image:
  repository: nginx
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion.
  tag: ""
```

_helpers.tpl
```yml
{{/*
Create the name of the service account to use
*/}}
{{- define "app.serviceAccountName" -}}
{{- if .Values.serviceAccount.create -}}
    {{ default (include "app.fullname" .) .Values.serviceAccount.name }}
{{- else -}}
    {{ default "default" .Values.serviceAccount.name }}
{{- end -}}
{{- end -}}
```

Chart.yaml
```yml
apiVersion: v2
name: test-app
description: A Helm chart for Kubernetes
```

deployment.yaml
```yml
spec:
    serviceAccountName: {{ include "test-app.serviceAccountName" . }}
    securityContext:
        {{- toYaml .Values.podSecurityContext | nindent 8 }}
    containers:
        - name: {{ .Chart.Name }}
          securityContext:
            {{- toYaml .Values.securityContext | nindent 12 }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
```

"values" that are injected into their respective placeholders located within the templates/*.yaml files when the helm template command is executed.


```bash
helm template ./app

# perform the actual deployment into the cluster
helm template cloudacademy ./app | kubectl apply -f -

# Perform a dev redeployment back into the cluster by referencing the values.dev.yaml Values file
helm template cloudacademy -f ./app/values.dev.yaml ./app | kubectl apply -f -

# List out all of the current Helm releases for the current namespace context.
helm ls 

#  package up the app into a chart.
helm package app/

# 
helm template cloudacademy -f ./app/values.prod.yaml ./app | kubectl delete -f - 
```


#### 2. ingress

Ingress resources are used to expose HTTP(S) routes.

An Ingress resource can provide any of the following:

Load balancing
SSL termination
HTTP Virtual Hosting (routing based on the domain name in a request)
HTTP URL path-based routing

create deployment and service
```bash
cat << EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: blue-app
spec:
  selector:
    matchLabels:
      app: blue-app
  replicas: 2
  template:
    metadata:
      labels:
        app: blue-app
    spec:
      containers:
      - name: blue-app
        image: public.ecr.aws/cloudacademy-labs/cloudacademy/labs/k8s-ingress-app:f9a36c8
        env:
        - name: COLOR
          value: '#A7C7E7'
        ports:
        - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: blue-app
spec:
  selector:
    app: blue-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
EOF
```

The Deployment's container listens on port 8000. The Service translates port 80 to port 8000 and provides a way of accessing the application inside the cluster. 


create ingress resource
```bash
cat << EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: lab-ingress
  annotations:
    kubernetes.io/ingress.class: "nginx"
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - http:
      paths:
      - path: /blue
        pathType: Prefix
        backend:
          service:
            name: blue-app
            port:
              number: 80
      - path: /red
        pathType: Prefix
        backend:
          service:
            name: red-app
            port:
              number: 80
EOF

```

The Ingress manifest consists of one http rule with two path configurations. The paths direct traffic to either the blue or red application, depending on whether the URL is blue or red.

Observe that the Ingress has a rewrite annotation on it. This means requests will be rewritten to the root HTTP path (/) before the request is routed to the application's Service.

To see a full list of the annotations available and their behaviour, visit the Annotations page of the NGINX Ingress Controller documentation.