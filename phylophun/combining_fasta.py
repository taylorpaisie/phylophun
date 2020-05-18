#!/usr/bin/env python
"""Combines fasta files one by one
Author: Taylor K. Paisie <tpaisie@ufl.edu>
Version: 1.0
Date: 2020-05-15
"""

__version="1.0"

args = ''
import os, sys, operator, logging, argparse
import numpy, urllib, time
from Bio import SeqIO, Entrez, SearchIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature
from ftplib import FTP
from urllib.error import HTTPError
