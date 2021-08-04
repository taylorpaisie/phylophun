#!/usr/bin/env python
"""This script part is the program called phylophun which is a combination of python
scripts to help manipulate and conduct phylogenetic analysis.
Author: Taylor K. Paisie <tpaisie@ufl.edu>
Version: 1.0
Date: 2020-05-15
"""

__version="0.1.0"

args = ''
import os, sys, operator, logging, argparse
import numpy, urllib, time
from Bio import SeqIO, Entrez, SearchIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature
from ftplib import FTP
from urllib.error import HTTPError


#first uploading the list of IDs using EPost
#can refer to the long list of IDs and download the associated data with EFetch

Entrez.api_key = "b8558abb22f17ea43a6fc07d48097c50a208"


def change_seq_names(args):
	fasta_file = open(sys.argv[1], 'r')
	ids = open(sys.argv[2], 'r')
	new_fasta = open(sys.argv[3], 'w')

	for f in fasta_file.readlines():
	    if f.__contains__(">"):
	        new_fasta.write(">" + ids.readline() + "\n")
	    else:
	        new_fasta.write(f)
	new_fasta.close()
	fasta_file.close()
	ids.close()


def main():
	parser=argparse.ArgumentParser(description="Change the sequence names (Fasta header) in a multisequence fasta file.")
    #parser=argparse.ArgumentParser(description="Change the names in your fasta file. Make it your way or find your way on the fasta-file highway.")
	parser.add_argument("-i", help="Input Fasta file (File to change sequence fasta file headers.", dest='Input fasta file', type=str, required=True)
	parser.add_argument("-rename",help="GenBank IDs of fasta files to download.", dest="id_list", type=str, required=True)
	parser.add_argument("-o",help="Output fasta file (file with new fasta headers).", dest="output", type=str, required=True)
	parser.set_defaults(func=get_gb_file)
	args=parser.parse_args()
	args.func(args)
	print('Your sequence names have now been changed.')
	print('Good luck on your next bioinformatics adventure!')
	print('"May the force of phylogenetics be with you" - Taylor Paisie')

if __name__=="__main__":
	main()	