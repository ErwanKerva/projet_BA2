#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

def get_all_fasta_rep(repo):
    fastas={}
    for files in os.listdir(repo):

        content=open(repo+"/"+files,'r')
        for line in content:
            if (line[0]=='>'):
                header=line[1:]
                fastas[header]=''
            else:
                fastas[header]+=line
        content.close()
    return fastas

def repetmotifseq(listepattern,p,cutoff): #p doit être renommé sequence ou autre
    for pattern in listepattern:
        results.write('Current pattern: '+'\t' + pattern + '\n')
        nb=[] #contient le nomb de motifs dans la "répétition"
        pos=[] #contient la position du début du motif dans la séquence
        j=0 #est incrémenté chaque fois qu'on passe sur une nouvelle répétition du motif dans la séquence
        var=0 #représente les bases de 3 en 3 (taille pattern)
        i=0
        while i<len(p):
            var=p[i:i+len(pattern)] #var contient les bases avec un nb correspondant à pattern
            if var==pattern:
                pos.append(i) #retient la position du 1er motif de la partie répétée
                nb.append(1)
                i=i+len(pattern)
                var=p[i:i+len(pattern)]
                for i in range(i,len(p),len(pattern)):
                    if var!=pattern:
                        j=j+1
                        break
                    var=p[i:i+len(pattern)]
                    if var!=pattern:
                        j=j+1
                        break
                    nb[j]=(nb[j]+1)
            i=i+1
        indice=0
        rep=False
        for indice in range(indice,len(nb)):
            if nb[indice]>cutoff:
                rep=True
        indice=0
        if rep:
            for indice in range(len(nb)):
                if nb[indice]>cutoff:
                    taille=(pos[indice]+nb[indice]*len(pattern))-(pos[indice])
                    results.write('\t\t' + 'Repeated ' + str(nb[indice]) + ' times in: ') 
                    results.write("["+str(pos[indice])+":"+str(pos[indice] + nb[indice]*len(pattern))+"]"+" on the sequence."+"\n") 
                    results.write('\t\tExpansion size: '+ str(taille) + ' kbp.' + '\n\n')	
        else:
            results.write('\t\t' + 'No OUTPUT found over the current threshold.' + '\n\n')


#Script
try:
	cutoff=int(sys.argv[1])
except:
	cutoff=5	

print("Get sequences in a Dictionnary.")
libfasta=get_all_fasta_rep('sequences')
#building a inverted dictionnary
print("Building an inverted Dictionnary.")
libfasta_inv= {}
for key in libfasta:
    copie=libfasta[key]
    libfasta_inv[copie]=key
print("Add Patterns.")    
listepattern=[]
listepattern.append('GGCCTG')
listepattern.append('GGGGCC')
listepattern.append('CTG')
listepattern.append('CCTG')
listepattern.append('GAA')
listepattern.append('TGGAA')
listepattern.append('ATTCT')
listepattern.append('ATTTC')

print("Pattern analysis.")


#Create a repository "results" 
os.makedirs('results', exist_ok=True)
os.chdir(os.getcwd() + "/results")


results=open("Results.txt", "w")
delim="#"*70
results.write(delim+"\n")
results.write("##    "+'\t\t\t\t\t\t\t'+"RESULT FILE"+'\t\t\t\t\t\t\t'+"##"+"\n")
results.write(delim+"\n")
results.write('\n\n\n')
results.write(delim+"\n")
results.write("INPUT PARAMETERS:"+"\n")
results.write("Numbers of sequences:"+"\t"+str(len(libfasta))+"\n")
results.write("Numbers of searched patterns:"+"\t"+str(len(listepattern))+"\n")
results.write("Expansion's threshold: "+"\t"+str(cutoff)+"\t"+"# Repetitions under the threshold are ignored. #"+"\n")
results.write(delim+"\n\n")
for sequence in libfasta.values():
    results.write(delim+"\n")
    results.write(delim+"\n")
    results.write('\n' + '-> ID sequence : ' + libfasta_inv[sequence] + '\n')
    repetmotifseq(listepattern,sequence,cutoff)
    results.write(delim+"\n")
    results.write(delim+"\n")
results.close()
print("DONE.")
