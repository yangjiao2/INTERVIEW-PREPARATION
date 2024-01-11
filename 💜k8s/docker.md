

 built a custom Docker image and then created a new namespace resource and set it as the default namespace into which the remaining deployment will take place.

```bash
docker build -t cloudacademydevops/flaskapp .

kubectl create ns cloudacademy

kubectl config set-context --current --namespace=cloudacademy
```
