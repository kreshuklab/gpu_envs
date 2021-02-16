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
setup_env.sh ARCH_NAME
```
Note that this will submit a job to the cluster, so it should be run from the `login.cluster.embl` node.

You can modify the environment that wil be set up by:
- Adding / removing conda pacakges from `base-env.yaml`
- Adding / removing packages that will be linked into the environment in `util/link_pacakges.py`
- Enable / disable building nvidia apex by calling `util/install_apex.sh` in the batch script. (Other pip build dependencies can be added in an analogous manner).


## Using the environments

Once set up, you can activate the correct gpu environment for your current architecture via `source bin/activate_gpu_env` (it's good to add this to the `PATH` so it can be called from everywhere).
The script `bin/submit_gpu_job` enables submitting jobs to the cluster and automatically enabling the right environment.
