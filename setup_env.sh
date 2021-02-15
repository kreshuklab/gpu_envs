#! /bin/bash

ARCH_NAME=$1
ENV_NAME="cluster_gpu_$ARCH_NAME"

# if the environment is already present this will fail
conda env create -f base-env.yaml -n $ENV_NAME

ENV_CREATED=$?
if [ $ENV_CREATED != 0 ]; then
    exit $ENV_CREATED
fi

SCRIPT_NAME="setup_${ARCH_NAME}.batch"
sbatch $SCRIPT_NAME
