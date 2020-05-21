#!/usr/bin/env python
"""This script part is the program called phylophun. It takes a fasta file and a text file with ids,
to give you a filter fasta file output.
Author: Taylor K. Paisie <tpaisie@ufl.edu>
Version: 0.1.0
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

input_file = args.input
id_file = args.id_list
output_file = args.output

wanted = list(line.rstrip("\n").split(None, 1)[0] for line in open(id_file))
print(wanted)
print("Found %i unique identifiers in %s" % (len(wanted), id_file))
records = (r for r in SeqIO.parse(input_file, "fasta") if r.id in wanted)
count = SeqIO.write(records, output_file, "fasta")
print("Saved %i records from %s to %s" % (count, input_file, output_file))
if count < len(wanted):
    print("Warning %i IDs not found in %s" % (len(wanted) - count, input_file))

def main():
	parser=argparse.ArgumentParser(description="Get all the GenBank files! Give me a list of GenBank IDs, and I shall download them.")
    #parser=argparse.ArgumentParser(description="Change the names in your fasta file. Make it your way or find your way on the fasta-file highway.")
	parser.add_argument("-e", help="Entrez email address.", dest='email', type=str, required=True)
	parser.add_argument("-i",help="GenBank IDs of fasta files to download.", dest="id_list", type=str, required=True)
	parser.add_argument("-o",help="Output GenBank file.", dest="output", type=str, required=True)
	parser.set_defaults(func=get_gb_file)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()
