#!/usr/bin/env python3

import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description="Install Localr and dependencies.")
parser.add_argument('--venv', metavar='DIR', type=str, default="python-venv", help='Destination of local Python virtual environment')
parser.add_argument('--path', metavar='DIR', type=str, default="python3", help='Path to local Python installation.')
for deployment in ["raw", "vm", "docker"]:
    parser.add_argument(f"--{deployment}", action="store_const", const=True, default=True, dest=deployment)
    parser.add_argument(f"--no-{deployment}", action="store_const", const=False, dest=deployment)
parser.add_argument("--rebuild", default=False, help='Force rebuild of virtual machine.')
args = parser.parse_args()

def execute(cmd):
    ret = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True
    )
    if ret.returncode:
        raise RuntimeError(
            "Running {} failed!\n Output: {}".format(cmd, ret.stdout.decode("utf-8"))
        )
    return ret.stdout.decode("utf-8")

env_dir=args.venv

if not os.path.exists(env_dir):
    print("Creating Python virtualenv at {}".format(env_dir))
    execute(f"{args.path} -mvenv {env_dir}")
    execute(f". {env_dir}/bin/activate && pip install --upgrade pip")
else:
    print(f"Using existing Python virtualenv at {env_dir}")

print("Install Python dependencies with pip")
execute(f". {env_dir}/bin/activate && pip3 install -r requirements.txt --upgrade")
