# GPU Envs

Apparently, using the pytorch from conda is much less performant than using the easybuild version [see these benchmarks for details.](https://github.com/constantinpape/3d-unet-benchmarks#embl-cluster-results)
This environment contains helper functions to set up and use conda environments that uses the easybuild pytorch.

## Setting up the environments

Easybuild provides packages for the different cpu architectures; so we need a different conda environment
for these architctures. Currently there are three different architectures for the EMBL gpu nodes: `haswell`, `skylake` and `rome`
and they map to gpu tpyes like this:
- 1080Ti: haswell
- 2080Ti:
    - GPU6-9: skylake
    - GPU11-20: rome
- V100: skylake
- 3090: rome
- A100: rome

To set up an environment for one of these architectures call
```
setup_env.sh ARCH_NAME [ENV_NAME_PREFIX] [PATH_TO_BASE_ENV.YAML]
```
Note that this will submit a job to the cluster, so it should be run from the `login.cluster.embl` node.

You can modify the environment that wil be set up by:
- Adding / removing conda pacakges from `base-env.yaml` (or specifying ENV_NAME_PREFIX and PATH_TO_BASE_ENV.YAML)
- Adding / removing packages that will be linked into the environment in `util/link_pacakges.py`
- Enable / disable building nvidia apex by calling `util/install_apex.sh` in the batch script. (Other pip build dependencies can be added in an analogous manner).


## Using the environments

Once set up, you can activate the correct gpu environment for your current architecture via
````
source bin/activate_gpu_env [ENV_NAME_PREFIX]
````
(it's a good idea to add this to the `PATH` so it can be called from everywhere).

To submit jobs to the cluster with the correct environment, you can use the scrpt `bin/submit_gpu_job`
```
bin/submit_gpu_job my_script.py arg1 arg2 ...
```
You can also override the default job settings, e.g. the type of gpu used.
```
bin/submit_gpu_job my_script.py arg1 arg2 ... --gpu_type A100
```
All the settings that are exposed as [arguments here](https://github.com/kreshuklab/gpu_envs/blob/main/bin/submit_gpu_job#L44-L48) can be set in this manner.

To submit jobs to be run in a non-default env, `export CLUSTER_GPU_ENV=<your ENV_NAME_PREFIX>` 
