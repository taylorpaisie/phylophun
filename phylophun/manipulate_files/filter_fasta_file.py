#!/usr/bin/env python
"""This script part is the program called phylophun. It takes a fasta file and a text file with ids,
to give you a filter fasta file output.
#!/usr/bin/env python
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




def filter_fasta_file(args):
	wanted = list(line.rstrip("\n").split(None, 1)[0] for line in open(args.ids))
	print(wanted)
	print("Found %i unique identifiers in %s" % (len(wanted), args.ids))
	records = (r for r in SeqIO.parse(args.input, "fasta") if r.id in wanted)
	count = SeqIO.write(records, "filter_"+args.input, "fasta")
	print("Saved %i records from %s to %s" % (count, args.input, "filter_"+args.input))
	if count < len(wanted):
	    print("Warning %i IDs not found in %s" % (len(wanted) - count, args.input))

	record_ids = list()

	# this part is needed with replicates are in fasta file 
	with open(args.output, 'w') as f:
		for record in SeqIO.parse("filter_"+args.input, 'fasta'):
	 		if record.id not in record_ids:
	 			record_ids.append(record.id)
	 			SeqIO.write(record, f, 'fasta')
		# print("Saved %i records from %s to %s" % (len(record), args.input, args.output))


# replicates are first removed and placed in "filter_" file, the taxa in text file will only 
# be in the output file

def main():
	parser=argparse.ArgumentParser(description="Filter fasta alignment. Text file is for what sequences to keep in alignment.")
	parser.add_argument("-i", help="Input fasta file that needs to be filtered.", 
		dest='input', type=str, required=True)
	parser.add_argument("-t",help="Sample IDs of fasta seqs to keep in alignment.", 
		dest="ids", type=str, required=True)
	parser.add_argument("-o",help="Filtered output fasta file.", 
		dest="output", type=str, required=True)
	parser.set_defaults(func=filter_fasta_file)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()
