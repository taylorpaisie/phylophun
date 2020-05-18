#!/usr/bin/env python

#**********************************************#

# Author: Taylor K. Paisie
# 

#**********************************************#
"""This script will extract snps from a vcf file and produce a multi-fasta
output with extracted reference and all variant sequences.
Author: Taylor Paisie <tpaisie@ufl.edu>
Version: 1.0
Date: 2020-05-06
"""
import os, sys, operator, logging, argparse
from SampleCollection import SampleCollection

__version="1.0"
