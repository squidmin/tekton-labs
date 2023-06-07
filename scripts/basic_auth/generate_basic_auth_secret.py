"""
Example usage:
python3 ./scripts/basic_auth/generate_basic_auth_secret.py GH_USERNAME GH_PAT
"""

import os
import sys
import yaml

CWD = os.path.dirname(os.path.realpath(__file__))

OUTPUT_FILE = CWD + "/../../Secrets/basic_auth_secret.yaml"

GH_USERNAME = sys.argv[1], GH_PAT = sys.argv[2]

tekton_secret = {
    "apiVersion": "v1",
    "kind": "Secret",
    "metadata": {
        "name": "basic-user-pass",
        "annotations": {
            "tekton.dev/git-0": "https://github.com",
        },
    },
    "type": "kubernetes.io/basic-auth",
    "stringData": {
        "username": GH_USERNAME,
        "password": GH_PAT,
    },
}

with open(OUTPUT_FILE, 'w') as basic_auth_secret:
    yaml.dump(tekton_secret, basic_auth_secret)

with open(OUTPUT_FILE, 'r') as basic_auth_secret:
    print(basic_auth_secret.read())
