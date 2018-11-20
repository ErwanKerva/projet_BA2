#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def repetmotifseq(listepattern,p): #p doit être renommé sequence ou autre
    for pattern in listepattern:
        #print('')
        #print(pattern)
        results.write('Le motif : ' + pattern + '\n')
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
        #print(pos)
        #print(nb)
        indice=0
        rep=False
        for indice in range(indice,len(nb)):
            #!!! 1 a été modifié en 10 pour simplifier les tests
            if nb[indice]>10:#!!! 1 a été modifié en 10 pour simplifier les tests
                rep=True
        indice=0
        if rep:
            for indice in range(len(nb)):
                #!!! 1 a été modifié en 10 pour simplifier les tests
                if nb[indice]>10:#!!! 1 a été modifié en 10 pour simplifier les tests
                    taille=(pos[indice]+nb[indice]*len(pattern))-(pos[indice])
                    results.write('\t\t' + ' est répété ' + str(nb[indice]) + ' fois de la position ' + str(pos[indice]) + ' à la position ' + str(pos[indice] + nb[indice]*len(pattern)) + ', la répétition a une taille de ' + str(taille) + ' bases.' + '\n\n')
        else:
            results.write('\t\t' + ' n\'a pas été trouvé répété dans la séquence' + '\n\n')

import os

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

libfasta=get_all_fasta_rep('sequences')
#building a inverted dictionnary
libfasta_inv= {}
for key in libfasta:
    copie=libfasta[key]
    libfasta_inv[copie]=key
listepattern=[]
listepattern.append('GGCCTG')
listepattern.append('GGGGCC')
listepattern.append('CTG')
listepattern.append('CCTG')
listepattern.append('GAA')
listepattern.append('TGGAA')
listepattern.append('ATTCT')
listepattern.append('ATTTC')
results=open("Results.txt", "w")
for sequence in libfasta.values():
    print(libfasta_inv[sequence])
    results.write('\n' + '!!! n\'apparaissent pas ici les répétitions inférieures ou égales à 1')
    results.write('\n' + '-> ID sequence : ' + libfasta_inv[sequence] + '\n')
    repetmotifseq(listepattern,sequence)
results.close()
