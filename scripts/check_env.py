#!/usr/bin/env python

"""Computational environment check script for 2014 SciPy Conference Tutorial:
Reproducible Research: Walking the Walk.

https://github.com/reproducible-research/scipy-tutorial-2014
"""

import sys
import subprocess


return_value = 0

required_packages = ['numpy', 'scipy', 'matplotlib', 'SimpleITK']
for package in required_packages:
    print('Importing ' + package + ' ...')
    try:
        __import__(package, globals(), locals(), [], 0)
    except ImportError:
        print('Error: could not import ' + package)
        return_value += 1


required_executables = ['git', 'dexy', 'ipython', 'nosetests']
for executable in required_executables:
    print('Executing ' + executable + ' ...')
    try:
        output = subprocess.check_output([executable, '--help'])
    except OSError:
        print('Error: could not execute ' + executable)
        return_value += 1


if return_value is 0:
    print('\nSuccess.')
else:
    print('\nAn error was found in your environment, please see the messages ' +
          'above.')
sys.exit(return_value)
