#!/usr/bin/env python
"""This script part is the program called phylophun which is a combination of python
scripts to help manipulate and conduct phylogenetic analysis.
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

class get_gb_gene:
        Entrez.api_key = "b8558abb22f17ea43a6fc07d48097c50a208"
        def get_gb_file(args):
        	Entrez.email = str(args.email)
        	id_list = open(args.id_list, 'r')
        	accessions = []
        	for line in id_list:
        		line = line.strip()
        		accessions.append(line)

        	gb_output = open(args.output, "w")
        	for gb_num in accessions:
        		gb_handle = Entrez.efetch(db="nucleotide", id=gb_num, rettype="gb", retmode="text")
        		gb_seqs = SeqIO.parse(gb_handle, "gb")
        		SeqIO.write(gb_seqs, gb_output, "gb")
        		gb_handle.close()
        		gb_output.close()

        def get_gene(args):
            gb_file = open(args.output, 'r')
            save_gene = open(args.output + '_gene.txt', 'w')
            for gb_record in SeqIO.parse(gb_file, 'genbank'):
                save_gene.write(gb_record.name+'\t'),
                for feat in gb_record.features:
                    if feat.type == 'source':
                        

def main():
	parser=argparse.ArgumentParser(description="Get all the GenBank files! Give me a list of GenBank IDs, and I shall download them.")
    #parser=argparse.ArgumentParser(description="Change the names in your fasta file. Make it your way or find your way on the fasta-file highway.")
	parser.add_argument("-e", help="Entrez email address.", dest='email', type=str, required=True)
	parser.add_argument("-i",help="GenBank IDs of GenBank files to download.", dest="id_list", type=str, required=True)
	parser.add_argument("-o",help="Output GenBank file.", dest="output", type=str, required=True)
	parser.set_defaults(func=get_gb_gene)
    # parser.set_defaults(func=get_country_date)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()
