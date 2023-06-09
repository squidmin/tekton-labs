"""
Example usage:
python3 ./scripts/generate_docker_credentials.py "$(cat ~/.docker/config.json | base64)"
"""

import os
import sys
import yaml

CWD = os.path.dirname(os.path.realpath(__file__))

OUTPUT_FILE = CWD + "/../Secrets/docker-credentials.yaml"

DOCKER_CONFIG = sys.argv[1]

tekton_secret = {
    "apiVersion": "v1",
    "kind": "Secret",
    "metadata": {
        "name": "docker-credentials",
    },
    "data": {
        "config.json": DOCKER_CONFIG,
    },
}

with open(OUTPUT_FILE, "w") as docker_secret:
    yaml.dump(tekton_secret, docker_secret)

with open(OUTPUT_FILE, "r") as docker_secret:
    print(docker_secret.read())
