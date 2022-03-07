#!/usr/bin/env bash
sudo apt update
sudo apt install virtualenv -y

virtualenv --python=python3 venv
source venv/bin/activate
python -m pip install -r requirements.txt
deactivate