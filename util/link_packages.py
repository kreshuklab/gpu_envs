import os
import site


def link_package(package_name, package_root):
    env_lib = site.getsitepackages()
    assert len(env_lib) == 1
    env_lib = env_lib[0]

    dst = os.path.join(env_lib, package_name)
    assert not os.path.exists(dst), f"Dest package {dst} is already in env"

    src = os.path.join(package_root, package_name)
    assert os.path.exists(src), f"Source pacakge {src} does not exist"

    os.symlink(src, dst)


# all the noarch python packages for the gpu dev env
def link_noarch_packages():
    roots = [
        '/g/kreshuk/pape/Work/my_projects/inferno',
        '/g/kreshuk/pape/Work/my_projects/neurofire',
        '/g/kreshuk/pape/Work/my_projects/MIPNet',
        '/g/kreshuk/pape/Work/my_projects/super_embeddings',
        '/g/kreshuk/pape/Work/my_projects/elf',
        '/g/kreshuk/pape/Work/my_projects/cluster_tools',
        '/g/kreshuk/pape/Work/my_projects/pybdv'
    ]
    names = [
        'inferno',
        'neurofire',
        'mipnet',
        'embed_utils',
        'elf',
        'cluster_tools',
        'pybdv'
    ]
    assert len(roots) == len(names)
    for name, root in zip(names, roots):
        link_package(name, root)


def link_build_packages():
    roots = [
        '/g/kreshuk/pape/Work/software/bld/py38/affogato/python',
        '/g/kreshuk/pape/Work/software/bld/py38/nifty/python',
        '/g/kreshuk/pape/Work/software/bld/py38/z5/python'
    ]
    names = [
        'affogato',
        'nifty',
        'z5py'
    ]
    assert len(roots) == len(names)
    for name, root in zip(names, roots):
        link_package(name, root)


def link_all():
    link_noarch_packages()
    link_build_packages()
