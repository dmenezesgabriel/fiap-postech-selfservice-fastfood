# Kubernetes

## Minikube
```shell
minikube start --mount-string "$HOME/minikube/postgres-data:/data" --driver=docker --install-addons=true --kubernetes-version=stable
minikube stop
minikube delete

kubectl get nodes
```

## K3s
```shell
multipass launch --name k3s --mem 4G --disk 40G
multipass info k3s

multipass shell k3s
curl -sfL https://get.k3s.io | sh -
```
## Kind
```shell
brew install kind

kind create cluster
kind get clusters

- Pausing cluster
docker stop kind-control-plane

- Resume cluster 
docker start kind-control-plane
```

## Enable metrics on cluster
```shell
kubectl apply -f cluster/components.yml

kubectl get deployment metrics-server -n kube-system

kubectl top node
```

## Building image
```shell
docker build -t alorencatto/fiap-postech-selfservice-fastfood .
docker push alorencatto/fiap-postech-selfservice-fastfood
```

## Applying manifests
```shell
kubectl apply -f namespace/ns.yml

-- Application
kubectl apply -f code/config-map.yml -n postech
kubectl apply -f code/deployment.yml -n postech
kubectl apply -f code/service.yml -n postech
kubectl apply -f code/nodeport-service.yml -n postech
kubectl apply -f hpa/fiap-postech-selfservice-fastfood-hpa.yml -n postech

-- Postgres
kubectl apply -f postgres/pv.yml -n postech
kubectl apply -f postgres/secret.yml -n postech
kubectl apply -f postgres/pvc.yml -n postech
kubectl apply -f postgres/deployment.yml -n postech
kubectl apply -f postgres/service.yml -n postech

-- Migration Job
kubectl apply -f job/migration-secret.yml -n postech # Not used yet
kubectl apply -f job/migration.yml -n postech

-- Nginx
kubectl apply -f nginx/nginx-config.yml -n postech
kubectl apply -f nginx/nginx-deployment.yml -n postech
kubectl apply -f nginx/nginx-service.yml -n postech

-- Get resources
kubectl get deployments -n postech
kubectl get pods -n postech

kubectl get svc -n postech
kubectl get pv -n postech
kubectl get pvc -n postech
kubectl get secrets -n postech

kubectl get jobs -n postech
kubectl get hpa -n postech

kubectl describe service nginx-service -n postech
kubectl describe deployment postgres-deployment -n postech
kubectl describe pv postgres-pv -n postech

kubectl top pod -n postech

-- Exposing services
kubectl port-forward service/svc-nodeport-fiap-postech-selfservice-fastfood --address 0.0.0.0 8000:8000 -n postech

-- Rollout restart
kubectl apply -f code/deployment.yml -n postech
kubectl rollout restart deployment fiap-postech-selfservice-fastfood -n postech
```

## Logging
```shell

kubectl get events --all-namespaces  --sort-by='.metadata.creationTimestamp'

kubectl fiap-postech-selfservice-fastfood-84f4fcb59-j4fkf -n postech
kubectl logs fiap-postech-selfservice-fastfood-nginx-deployment-55d6d96n7h6m -n postech
kubectl logs postgres-deployment-857594b99c-tq8kn -n postech
kubectl logs fiap-postech-selfservice-fastfood-migrations-7kkg5 -n postech
```

## Housekeeping
```shell
kubectl delete -f namespace/ns.yml

kubectl delete -f code/config-map.yml -n postech
kubectl delete -f code/deployment.yml -n postech
kubectl delete -f code/service.yml -n postech
kubectl delete -f code/nodeport-service.yml -n postech
kubectl delete -f hpa/fiap-postech-selfservice-fastfood-hpa.yml -n postech

kubectl delete -f job/migration.yml -n postech

kubectl delete -f postgres/pv.yml -n postech
kubectl delete -f postgres/secret.yml -n postech
kubectl delete -f postgres/deployment.yml -n postech
kubectl delete -f postgres/pvc.yml -n postech
kubectl delete -f postgres/service.yml -n postech

kubectl delete -f nginx/nginx-config.yml -n postech
kubectl delete -f nginx/nginx-deployment.yml -n postech
kubectl delete -f nginx/nginx-service.yml -n postech
```

## Stress test
```shell
k6 run scripts/stress-test/test-api.js

kubectl describe deployment fiap-postech-selfservice-fastfood -n postech
```