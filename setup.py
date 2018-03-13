#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
from setuptools import find_packages, setup

# Package meta-data.
NAME = 'graph_report'
DESCRIPTION = 'A CLI wrapper that rewrites a RAGE brief report to include graphs'
URL = 'https://code.citrite.net/users/callumiandam/repos/graph-report'
EMAIL = 'callum.mcintyre@citrix.com'
AUTHOR = 'Callum McIntyre'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'ragelib'
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
# TODO: add a readme.md
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Where the magic happens:
setup(
    name=NAME,
    use_scm_version=True,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    py_modules=['graph_report'],

    entry_points={
         'console_scripts': ['graph-report = graph_report:main'],
    },
    install_requires=REQUIRED,
    include_package_data=True,
    license='BSD-3-Clause',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
