#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 - 2022 James E. King III (@jeking3) <jking@apache.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from pathlib import Path

from pkg_resources import parse_version
from setuptools import setup

# Configurables

name = "tempenv"
description = "Environment Variable Context Manager"
packages = ["tempenv"]
versionfile = "tempenv/version.py"

# Everything below should be cookie-cutter


def get_requirements(name: str) -> list:
    """
    Return the contents of a requirements file

    Arguments:
      - name: the name of a file in the requirements directory

    Returns:
      - a list of requirements
    """
    return read_file(Path(f"requirements/{name}.txt")).splitlines()


def read_file(path: Path) -> str:
    """
    Return the contents of a file

    Arguments:
      - path: path to the file

    Returns:
      - contents of the file
    """
    with path.open() as desc_file:
        return desc_file.read().rstrip()


def version():
    """
    Return the version string for the package stored in versionfile.
    """
    _version = {}
    exec(read_file(Path(versionfile)), _version)
    return str(parse_version(_version["__version__"]))


requirements = {}
for type in ["run", "test"]:
    requirements[type] = get_requirements(type)

setup(
    name=name,
    version=version(),
    python_requires=">=3.7",
    description=description,
    long_description=read_file(Path("README.md")),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security",
        "Topic :: System :: Shells",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    keywords="temporary, environment variable, context manager, test, testing",
    download_url="https://github.com/jeking3/tempenv/archive/main.zip",
    url="https://github.com/jeking3/tempenv",
    author="James E. King III",
    author_email="jking@apache.org",
    license="Apache License 2.0",
    install_requires=requirements["run"],
    tests_require=requirements["test"],
    test_suite="unittest",
    packages=packages,
    include_package_data=True,
    package_data={"tempenv": ["py.typed"]},
)
