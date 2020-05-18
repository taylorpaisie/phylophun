#!/usr/bin/env python
"""Combines fasta files one by one
Author: Taylor K. Paisie <tpaisie@ufl.edu>
Version: 1.0
Date: 2020-05-15
"""

__version="0.1.0"

args = ''
import os, sys, operator, logging, argparse
import numpy, urllib, time, glob
from Bio import SeqIO, Entrez, SearchIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature
from ftplib import FTP
from urllib.error import HTTPError

def combining_fasta(args):
    file_list = glob.glob(args.input)
    with open(args.output, 'w') as w_file:
        for filen in file_list:
            with open(filen, 'rU') as o_file:
                seq_records = SeqIO.parse(o_file, 'fasta')
                SeqIO.write(seq_records, w_file, 'fasta')


def main():
	parser=argparse.ArgumentParser(description="Get all the Fasta files! Give me a list of GenBank IDs, and I shall download them.")
    #parser=argparse.ArgumentParser(description="Change the names in your fasta file. Make it your way or find your way on the fasta-file highway.")
	parser.add_argument("-i",help="Input fasta files in a directory.", dest="input", type=str, required=True)
	parser.add_argument("-o",help="Output Fasta file with all fasta files in directory combined one by one into a single fasta file.", dest="output", type=str, required=True)
	parser.set_defaults(func=combining_fasta)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()
