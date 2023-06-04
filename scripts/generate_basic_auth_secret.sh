#!/bin/bash

# Example usage:
# ./scripts/generate_basic_auth_secret.sh YOUR_GH_USERNAME YOUR_PAT

GH_USERNAME="$1"
GH_PAT="$2"

cat <<EOF > ./Secrets/basic_auth_secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: basic-user-pass
  annotations:
    tekton.dev/git-0: https://github.com
type: kubernetes.io/basic-auth
stringData:
  username: ${GH_USERNAME}
  password: ${GH_PAT}
EOF
