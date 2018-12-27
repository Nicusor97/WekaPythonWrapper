Weka - Python wrapper for Weka Graphics
==========================================

Overview
--------

Provides a convenient wrapper for calling Weka from Python to generate a graph with the data from an arff file.

Installation
------------

First install the Weka and LibSVM Java libraries. On Debian/Ubuntu this is simply:

    sudo apt-get install weka libsvm-java

Then install the Python package with pip:

    sudo pip install weka

Usage
-----

Create a Python 3 environment with the 'virtualenv' module and after activate it. After install the requirements using the pip module : `pip install dev_requirements.txt` and run the `main.py` script from command line.


Development
-----------

Tests require the Python development headers to be installed, which you can install on Ubuntu with:

    sudo apt-get install python-dev python3-dev python3.4-dev

To run unittests across multiple Python versions, install:

    sudo apt-get install python3.4-minimal python3.4-dev python3.5-minimal python3.5-dev

To run all [tests](http://tox.readthedocs.org/en/latest/):

    export TESTNAME=; tox