#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import Bio
from Bio import SeqIO
fic = list(SeqIO.parse("Homo_sapiens_CNBP_sequence.fa", "fasta"))
i=0
while i<len(fic):
    print(fic[i].id, '\n')
    i=i+1

pattern='CCTG'
n=fic.count(pattern)
if n>0:
    i=0
    while i<len(fic):
        if condition:
            pass
        i=i+4
