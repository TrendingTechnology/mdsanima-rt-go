#!/usr/bin/python3

"""
Help Developmend Release Workflow.

.. important::

    This file is not a part of `mdsanima-rt-go` App.
    Run in `package.json` script.

Bumping version in `package.json` file.
Bumping version in '__init__.py` file.
Autogenerate 'CHANGELOG.md` based on commits.
Committing `package.json`, `__init__py` and `CHANGELOG.md` with signed GPG keys.
Creating tagging release and signed commit with GPG keys.

Check version in `package.json` and then replece this version in `__init__.py`
file.

:usage: ./make_release.py
"""


import os
import json
import pathlib

HERE = pathlib.Path(__file__).parent


def go_check():
    """
    Load data from ``package.json``file.
    ``postbump`` executex after the version is bumped.

    :return: new version to replece
    :rtype: str
    """
    path_to_file = HERE / "package.json"
    with open(path_to_file) as dt:
        data_package = json.load(dt)
    new_version = data_package["version"]
    return new_version


def go_read_write(old_version, new_version):
    """
    This function replecing old version with new version file ``__init__.py``

    :param old_version: lines with old version
    :type old_version: str
    :param new_version: lines with new version
    :type new_version: str
    """
    path_to_file = HERE / "__init__.py"
    with open(path_to_file, 'r', encoding='utf-8') as r:
        replace_version = r.read().replace(old_version, new_version)
    with open(path_to_file, 'w', encoding='utf-8') as w:
        w.write(replace_version)


def go_bump():
    """
    Reading file ``__init__.py`` and splits lines. Searching matching lines
    and replacing this line with new version. Printing info in the console.
    """
    path_to_file = HERE / "__init__.py"
    with open(path_to_file, 'r', encoding='utf-8') as r:
        lines = r.read().splitlines()
    lines_len = len(lines)

    for line in range(lines_len):
        if str("__version__") in str(lines[line]):
            print('[MDSANIMA-DEV] -> bumping __init__.py')
            print('[MDSANIMA-DEV] => matching line', line + 1, lines[line])
            new_version = go_check()
            print('[MDSANIMA-DEV] => checking new version =>', new_version)
            new_line_version = '__version__ = "' + new_version + '"'
            go_read_write(str(lines[line]), str(new_line_version))
            print('[MDSANIMA-DEV] => replace line', line + 1, new_line_version)


if __name__ == "__main__":
    go_bump()