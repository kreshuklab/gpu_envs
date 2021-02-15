from util.replace_torch import replace_torch
from util.link_packages import link_all


def set_up_env():
    replace_torch()
    link_all()


if __name__ == '__main__':
    set_up_env()
