#!/usr/bin/env python
"""combines fasta files into one sequence sequentially
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


def concatenate_fasta(args):
    for fasta_file in glob.glob(args.input):
        concat = Seq.Seq("")
        for s in SeqIO.parse(fasta_file, 'fasta'):
            concat += s
        print(fasta_file)
        concat.id = fasta_file
        concat.description = ""
        SeqIO.write(concat, args.output, 'fasta')


def main():
	parser=argparse.ArgumentParser(description="Get all the Fasta files! Give me a list of GenBank IDs, and I shall download them.")
    #parser=argparse.ArgumentParser(description="Change the names in your fasta file. Make it your way or find your way on the fasta-file highway.")
	parser.add_argument("-i",help="Input fasta files in a directory to be concatenated together.", dest="input", type=str, required=True)
	parser.add_argument("-o",help="Output Fasta files with all fasta files in directory is concatenated one by one in sequential order.", dest="output", type=str, required=True)
	parser.set_defaults(func=concatenate_fasta)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()
