#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

# import QtWrapperWeka

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def get_reqs(*fns):
    lst = []
    for fn in fns:
        for package in open(os.path.join(CURRENT_DIR, fn)).readlines():
            package = package.strip()
            if not package:
                continue
            lst.append(package.strip())
    return lst

setup(name='QtWrapperWeka',
    version=(0,0,1),
    description='A Python wrapper for the Weka graphics .',
    author='Picatureanu Nicusor',
    author_email='nicolaepicatureanu@gmail.com',
    url='https://github.com/Nicusor97/WekaPythonWrapper',
    license='LGPL License',
    packages=find_packages(),
    package_data={
        'QtWekaWrapper': [
            'fixtures/*'
        ],
    },

    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Operating System :: Linux(Ubuntu)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: General",
    ],
    platforms=['Linux'],
    install_requires=get_reqs('dev_requirements.txt'),
)
