# `kubectl` cli reference


### Verify that a task is working as expected

<details>
<summary>Expand</summary>

Xreate a `TaskRun` to run the `Task`.

Assuming the `TaskRun` you create is named `example-task-run`, you can call the `TaskRun` to test it using:

```shell
kubectl get taskrun example-task-run
```

</details>


### Apply changes to a `Task`

<details>
<summary>Expand</summary>

If changes are made to one of the `Task` files, you can apply the changes to your cluster using:

```shell
kubectl cpply --filename Tasks/filename.yaml
```

Applying changes to a `Task` will cause the `Task` to launch.

</details>


### Monitor a `PipelineRun`

<details>
<summary>Expand</summary>

```shell
kubectl get pipelineruns -w
```

</details>
