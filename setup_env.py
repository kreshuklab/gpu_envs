import argparse
from util.replace_torch import replace_torch
from util.link_packages import link_all


def set_up_env(replace, link):
    if replace:
        replace_torch()
    if link:
        link_all()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--replace', '-r', default=1)
    parser.add_argument('--link', '-l', default=1)
    args = parser.parse_args()
    set_up_env(bool(args.replace), bool(args.link))
