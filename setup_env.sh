#! /bin/bash

ARCH_NAME=$1
if [ $# == 2 ]; then  # check if an alternative base-env.yaml was specified
  conda env create -f "$2"
else
  conda env create -f base-env.yaml -n "cluster_gpu_$ARCH_NAME"
fi

# if the conda environment was already present its creation will have failed
ENV_CREATED=$?
if [ $ENV_CREATED != 0 ]; then
    exit $ENV_CREATED
fi

SCRIPT_NAME="setup_${ARCH_NAME}.batch"
sbatch $SCRIPT_NAME
