#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Copyright 2020 The Open Microscopy Environment
   All rights reserved.

   Use is subject to license terms supplied in LICENSE.txt

"""
from glob import glob
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


def parse_requirements(fname):
    """
    Utility function to parse requirements.txt files.
    """
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        txt = f.read().splitlines()
        return [
            line.strip() for line in txt if not line.strip().startswith('#')]


def get_extras_require():
    extras = {}
    requirements_files = [os.path.basename(g) for g in glob(
        os.path.join(os.path.dirname(__file__), 'requirements-*.txt'))]
    for fname in requirements_files:
        if fname != 'requirements-pinned.txt':
            extras[fname[13:-4]] = parse_requirements(fname)
    return extras


setup(name="omero-server",
      version=osv,
      description="CLI plugin for managing an OMERO.server",
      long_description=read("README.rst"),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v2 '
          'or later (GPLv2+)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],  # Get strings from
          # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      author="The Open Microscopy Team",
      author_email="ome-devel@lists.openmicroscopy.org.uk",
      url="https://github.com/ome/omero-cli-server/",
      license='GPLv2+',
      packages=find_packages(exclude=("test",))+["omero.plugins"],
      python_requires='>=3',
      install_requires=parse_requirements('requirements-pinned.txt'),
      include_package_data=True,
      tests_require=['pytest'],
      extras_require=get_extras_require(),
      )
