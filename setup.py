#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="limerick",
    version="0.1",
    description="A simple python library for validating limericks",
    author="Michael Abed",
    author_email="michaelabed@gmail.com",

    packages=find_packages('limerick', exclude="tests"),
    zip_safe=True,

    install_requires=['nltk>=2.0.0', 'nltk-contrib>=2.0.0', 'numpy>=1.6.0']
)
