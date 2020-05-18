#!/usr/bin/env python
"""This script part is the program called phylophun which is a combination of python
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


#first uploading the list of IDs using EPost
#can refer to the long list of IDs and download the associated data with EFetch
class get_country_date:
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

    def get_country(args):
        gb_file = open(args.ouput, 'r')
        #extract country and collection date from genbank file
        #take out accession numbers and country in a text file
        save_country = open(arg.output + '_country.txt', 'w')
        for gb_record in SeqIO.parse(gb_file, 'genbank'):
            save_country.write(gb_record.name+'\t'),
            for feat in gb_record.features:
                if feat.type == 'soure':
                    source = gb_record.features[0]
                    for qualifiers in source.qualifiers:
                        if qualifiers == 'country':
                            country = source.qualifiers['country']
                            save_country.write(country[0]+'\n'),
        save_country.close()
        gb_file.close()

    def get_date(args):
        #take out accession numbers and collection date in a text file
        # parse genbank file
        gb_file = gb_file = open(args.ouput, 'r')
        save_date = open(arg.output + '_date.txt', 'w')
        for gb_record in SeqIO.parse(gb_file, 'genbank'):
            save_date.write(gb_record.name+"\t"),
            for feat in gb_record.features:
                if feat.type == 'source':
                    source = gb_record.features[0]
                    for qualifiers in source.qualifiers:
                        if qualifiers == 'collection_date':
                            date = soure.qualifiers['collection_date']
                            save_date.write(date[0], "\n"),
        save_date.close()
        gb_file.close()


def main():
	parser=argparse.ArgumentParser(description="Get all the GenBank files! Give me a list of GenBank IDs, and I shall download them.")
    #parser=argparse.ArgumentParser(description="Change the names in your fasta file. Make it your way or find your way on the fasta-file highway.")
	parser.add_argument("-e", help="Entrez email address.", dest='email', type=str, required=True)
	parser.add_argument("-i",help="GenBank IDs of GenBank files to download.", dest="id_list", type=str, required=True)
	parser.add_argument("-o",help="Output GenBank file.", dest="output", type=str, required=True)
	parser.set_defaults(func=get_country_date)
    # parser.set_defaults(func=get_country_date)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()
