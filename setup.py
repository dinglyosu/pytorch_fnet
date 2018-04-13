#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

setup(name='pytorch_fnet',
      description=' a machine learning model for transforming microsocpy images between modalities',
      author='Ounkomol, Chek and Fernandes, Daniel A. and Seshamani, Sharmishtaa and Maleckar, Mary M. and Collman, Forrest and Johnson, Gregory R.',
      author_email='gregj@alleninstitute.org',
      url='https://github.com/AllenCellModeling/pytorch_fnet',
      packages=find_packages(exclude=['doc/*', 'docker/*', 'data/*', 'scripts/*', 'tests/*']),
      install_requires=required)
