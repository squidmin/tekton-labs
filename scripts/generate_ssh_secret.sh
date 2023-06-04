#!/bin/bash

# Example usage:
# ./scripts/generate_ssh_secret.sh SSH_SECRET_FILENAME

GH_USERNAME="$1"
GH_SSH_TOKEN="$(cat ~/.ssh/${SSH_SECRET_FILENAME})"

cat <<EOF > ./Secrets/ssh_secret.yaml
apiVersion: v1
kind: Secret
metadata:
  annoatations:
    tekton.dev/git-0: https://github.com
type: kubernetes.io/ssh-auth
stringData:
  ssh-privatekey: ${GH_SSH_TOKEN}
  known_hosts: ${GH_SSH_TOKEN}
EOF
