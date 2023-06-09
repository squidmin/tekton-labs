#!/bin/bash

kubectl apply --filename https://raw.githubusercontent.com/tektoncd/catalog/main/task/git-clone/0.6/git-clone.yaml
kubectl apply --filename https://api.hub.tekton.dev/v1/resource/tekton/task/kaniko/0.6/raw

kubectl apply -f Secrets/
kubectl apply -f Tasks/
kubectl apply -f Pipelines/
