#!/bin/bash

python3 -m venv wolt-env
source "./wolt-env/bin/activate"
pip install --upgrade pip
pip install -r requirements.txt