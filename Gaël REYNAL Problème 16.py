def expo_rapide(n,p):
    """renvoie le nombre n**p"""
    if p == 1:
        return n
    elif p%2 == 0:
        resultat = expo_rapide(n,p/2)
        return resultat**2
    else:
        resultat = expo_rapide(n,(p-1)/2)
        return resultat**2*n

def somme_chiffres(n):
    """renvoie la somme des chiffres de n"""
    somme = 0
    while n != 0:
        somme+=n%10
        n=n//10
    return somme

assert somme_chiffres(expo_rapide(2,15)) == 26

print (somme_chiffres(expo_rapide(2,1000)))
