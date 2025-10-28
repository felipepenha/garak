#!/bin/bash
# This script creates a conda environment named 'purple_team' with Python 3.12 and uv.

conda remove --name purple_team --all -y

conda clean --all -y

conda create -n purple_team python=3.12 uv -c conda-forge -y

conda run -n uv purple_team pip install transformers torch
