L = open ("names.txt")
for ligne in L:
    liste_noms_texte = ligne
    liste_noms=liste_noms_texte.split(",")
L.close()

liste_noms = sorted(liste_noms)

def valeur_liste(liste):
    liste_valeurs=[]
    
    #détermination de la valeur des noms
    
    valeur = 0
    for nom in liste:
        somme=0
        for lettre in nom:
            if lettre != '"':
                somme+=ord(lettre)-64
        liste_valeurs.append(somme)
    
    #détermination de la valeur finale
    for k in range (len(liste_valeurs)):
        valeur += liste_valeurs[k]*(k+1)
    
    return valeur

#On considère en exemple la liste ["ABBA","BEATLES","METALLICA"] dont la valeur est
#v = 6*1 + 64*2 + 76*3 = 362

assert valeur_liste(["ABBA","BEATLES","METALLICA"]) == 362

print(valeur_liste(liste_noms))