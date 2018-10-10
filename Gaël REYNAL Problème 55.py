def retourne(n):
    n_reverse=0
    chiffres_n=[]
    while n != 0:
        chiffres_n.append(n%10)
        n=n//10
    chiffres_n = chiffres_n[::-1]
    for k in range(len(chiffres_n)):
        n_reverse+=chiffres_n[k]*10**k
    return n_reverse

def verifie_palindrome(n):
    n1=retourne(n)
    if n1==n:
        return True
    else:
        return False
        
def iteration_lychrel(n):
    n1=retourne(n)
    return n+n1
    
def lychrel(n):
    """renvoie le nombre de nombres de lychel inférieurs à n"""
    liste_lychrel=[]
    for k in range(n+1):
        nombre_en_cours = k
        nombre_en_cours=iteration_lychrel(nombre_en_cours)
        compteur=1
        while compteur <= 50 and not verifie_palindrome(nombre_en_cours):
            nombre_en_cours=iteration_lychrel(nombre_en_cours)
            compteur+=1
        if compteur==51:
            liste_lychrel.append(k)
    return len(liste_lychrel)

#On sait que le premier nombre de lychrel est 196. On vérifie donc que la fonction lychrel(196) renvoie bien 1.

assert lychrel(196)==1
print(lychrel(10000))
