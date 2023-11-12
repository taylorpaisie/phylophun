#!/usr/bin/env python
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.2.0'
PACKAGE_NAME = 'phylophun'
AUTHOR = 'Taylor K. Paisie'
AUTHOR_EMAIL = 'tpaisie91@gmail.com'
URL = 'https://github.com/taylorpaisie/phylophun'

LICENSE = ''
DESCRIPTION = 'phylophun is a python package to help manipulate and download files to conduct phylogenetic analysis.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'pandas',
      'biopython'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
      python_requires='>=3.6',
      )
