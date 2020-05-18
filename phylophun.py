#!/usr/bin/env python
"""This script is the program called phylophun which is a combination of python
scripts to help manipulate and conduct phylogenetic analysis.
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

Entrez.api_key = "b8558abb22f17ea43a6fc07d48097c50a208"

# class get_all_the_files_your_heart_desires:
def get_fasta_file(args):
	Entrez.email = input(str(args.email))
	id_list = open(args.id_list, 'r')
	accessions = []
	for line in id_list:
		line = line.strip()
		accessions.append(line)
	fasta_output = open(args.output, 'w')
	for num in accessions:
		handle = Entrez.efetch(db='nuccore', id=num, rettype='fasta')
		fasta_seqs = SeqIO.parse(handle, 'fasta')
		SeqIO.write(fasta_seqs, fasta_output, 'fasta')
	handle.close()
	fasta_output.close()


def main():
	parser=argparse.ArgumentParser(description="Get all the Fasta files! Give me a list of GenBank IDs, and I shall download them.")
    #parser=argparse.ArgumentParser(description="Change the names in your fasta file. Make it your way or find your way on the fasta-file highway.")
	parser.add_argument("-e", help="Entrez email address.", dest='email', type=str, required=True)
	parser.add_argument("-i",help="GenBank IDs of fasta files to download.", dest="id_list", type=str, required=True)
	parser.add_argument("-o",help="Output Fasta file.", dest="output", type=str, required=True)
	parser.set_defaults(func=get_fasta_file)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()
