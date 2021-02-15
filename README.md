# GPU Envs

https://github.com/constantinpape/3d-unet-benchmarks#embl-cluster-results

## Setting up the environments

Setting up the environments for different gpu types:
Run the following command for `ARCH_NAME=[haswell, skylake, rome]`:
```
setup_env.sh ARCH_NAME
```

Architectures for the different gpus:

- 1080Ti: haswell
- 2080Ti:
    - GPU6-9: skylake
    - GPU11-20: rome
- V100: skylake
- 3090: rome
- A100: rome

## Using the environments
