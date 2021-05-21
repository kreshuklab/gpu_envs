#! /bin/bash

ARCH_NAME=$1
if [ $# -gt 1 ]; then
  ENV_NAME=$2
else
  ENV_NAME="cluster_gpu"
fi

if [ $# -gt 3 ]; then
  BASE_ENV=$3
else
  BASE_ENV="base-env.yaml"
fi


conda env create -f "$BASE_ENV" -n "${ENV_NAME}_$ARCH_NAME"

# if the conda environment was already present its creation will have failed
ENV_CREATED=$?
if [ $ENV_CREATED != 0 ]; then
    exit $ENV_CREATED
fi

sbatch "setup_${ARCH_NAME}.batch" $ENV_NAME
