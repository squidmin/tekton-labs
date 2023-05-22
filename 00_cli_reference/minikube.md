# minikube CLI reference

### Interact with a cluster

<details>
<summary>Display cluster info</summary>

```shell
kubectl get po -A
```

</details>

<details>
<summary>Access the Kubernetes Dashboard</summary>

```shell
minikube dashboard
```

</details>

---

### Deploy a service

<details>
<summary>Create a sample deployment and expose it on port 8080</summary>

```shell
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube --type=NodePort --port=8080
```

</details>

<details>
<summary>List deployment info</summary>

It may take a moment, but your deployment will soon show up when you run:

```shell
kubectl get services hello-minikube
```

</details>

<details>
<summary>Access the service</summary>

```shell
minikube service hello-minikube
```

</details>

<details>
<summary>Forward the application port</summary>

```shell
kubectl port-forward service/hello-minikube 7080:8080
```

</details>

---

### Manage your cluster

<details>
<summary>Pause Kubernetes without impacting deployed applications</summary>

```shell
minikube pause
```

</details>

<details>
<summary>Unpause a paused instance</summary>

```shell
minikube unpause
```

</details>

<details>
<summary>Halt the cluster</summary>

```shell
minikube stop
```

</details>

<details>
<summary>Change the default memory limit (requires a restart)</summary>

```shell
minikube config set memory 9001
```

</details>

<details>
<summary>Browse the catalog of easily installed Kubernetes services</summary>

```shell
minikube addons list
```

</details>

<details>
<summary>Create a second cluster running an older Kubernetes release</summary>

```shell
minikube start -p aged --kubernetes-version=v1.16.1
```

</details>

<details>
<summary>Delete all of the minikube clusters</summary>

```shell
minikube delete --all
```

</details>
