#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="taylorpaisie",
    version="0.0.1",
    author="Taylor K. Paisie",
    author_email="tpaisie@ufl.edu",
    description="A python package to help manipulate files for conducting phylogenetic analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taylorpaisie/phylophun",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
