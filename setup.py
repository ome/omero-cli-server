#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Copyright 2020 The Open Microscopy Environment
   All rights reserved.

   Use is subject to license terms supplied in LICENSE.txt

"""

import os
import sys

from setuptools import setup, find_packages

sys.path.append(".")
from omeroserver.version import omeroserver_version as osv  # noqa


def read(fname):
    """
    Utility function to read the README file.
    :rtype : String
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="omero-server",
    version=osv,
    description="CLI plugin for managing an OMERO.server",
    long_description=read("README.rst"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 " "or later (GPLv2+)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],  # Get strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    author="The Open Microscopy Team",
    author_email="ome-devel@lists.openmicroscopy.org.uk",
    url="https://github.com/ome/omero-cli-server/",
    license="GPLv2+",
    packages=find_packages(exclude=("test",)) + ["omero.plugins"],
    python_requires=">=3",
    install_requires=[
        # requires Ice (use wheel for faster installs)
        "omero-py",
        # minimum requirements for `omero admin start`
        "omero-certificates",
        "tables",
    ],
    include_package_data=True,
    tests_require=["pytest"],
)
