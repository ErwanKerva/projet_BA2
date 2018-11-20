#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#a='le monde'
#print a.count('e')
#2

p='CTGCTGCTGATCATCGATTCTGGAATTCGAGAGAAGAATAGATCATTGGAATGGAACATCCGCCATACGAACTGGATCGCCATCGATCGAAGAAGAAATCATCATCGCCATCGGCCTGGGCCTGGGCCTG'
#pattern='ATC'
#print("Le motif ATC est répété ", p.count(pattern), " fois")
#pour compter des caract 1 à 19
#print("entre les caract 1 et 19, le motif est répété ", p.count(pattern,1,19), "fois")

listepattern=[]
listepattern.append('GGCCTG')
listepattern.append('GGGGCC')
listepattern.append('CTG')
listepattern.append('CCTG')
listepattern.append('GAA')
listepattern.append('TGGAA')
listepattern.append('ATTCT')
listepattern.append('ATTTC')
#print(listepattern)
results=open("Results.txt", "w")
for pattern in listepattern:
    print('')
    print(pattern)
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
            #nb[j]=nb[j]+1
            i=i+3
            #print("var1 : ", var, "est présente :", nb[j], "fois et sa position est", pos[j])
            var=p[i:i+len(pattern)]
            #print("var2 : ", var)
            #print("j = ", j)
            #print("nb en j =", nb[j])
            for i in range(i,len(p),3):
                if var!=pattern:
                    j=j+1
                    break
                var=p[i:i+len(pattern)]
                if var!=pattern:
                    j=j+1
                    break
                nb[j]=(nb[j]+1)
        i=i+1
    print(pos)
    print(nb)
    indice=0
    rep=False
    for indice in range(indice,len(nb)):
        if nb[indice]>1:
            rep=True
    indice=0
    if rep:
        for indice in range(len(nb)):
            if nb[indice]>1:
                #results.write('Le motif : ' + pattern)
                taille=(pos[indice]+nb[indice]*len(pattern))-(pos[indice])
                #print('taille de',taille, 'bases')
                results.write('\t\t' + ' est répété ' + str(nb[indice]) + ' fois de la position ' + str(pos[indice]) + ' à la position ' + str(pos[indice] + nb[indice]*len(pattern)) + ', la répétition a une taille de ' + str(taille) + ' bases.' + '\n\n')
    else:
        results.write('\t\t' + ' n\'a pas été trouvé répété dans la séquence' + '\n\n')
