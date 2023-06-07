"""
Example usage:
python3 ./scripts/basic_auth/generate_ssh_secret.py "$(cat ~/.ssh/id_ed25519)"
"""

import os
import sys
import yaml

CWD = os.path.dirname(os.path.realpath(__file__))

OUTPUT_FILE = CWD + "/../../Secrets/ssh_secret.yaml"

SSH_KEY = sys.argv[1]

tekton_secret = {
    "apiVersion": "v1",
    "kind": "Secret",
    "metadata": {
        "name": "ssh-key",
        "annotations": {
            "tekton.dev/git-0": "https://github.com",
        },
    },
    "type": "kubernetes.io/ssh-auth",
    "stringData": {
        "ssh-privatekey": SSH_KEY,
        "known_hosts": SSH_KEY,
    },
}

with open(OUTPUT_FILE, 'w') as ssh_secret:
    yaml.dump(tekton_secret, ssh_secret)

with open(OUTPUT_FILE, 'r') as ssh_secret:
    print(ssh_secret.read())
