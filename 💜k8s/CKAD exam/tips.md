20% design & build
20% service & network
20% deployment
25% env, configuration, security
15: observability

browser shell:
ctrl c, ctrl v not work: control insert, shift insert
k alias and bash autocompletion
``` bash
## kub
source < (kubectl completion bash)

echo "source <(kubectl completion bash)" >> ~/.bashrc
source ~/.bashrc

## helm
echo 'source <(helm completion bash)' >> ~/.bash_profile

## alias
alias k=kubectl
alias kg="k get"

```
editor:
tmux

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