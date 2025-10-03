'''Fonctions itérative et récursive qui permet d'encoder une chaine de
caractères par une liste de tuples'''
#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    n = len(s)
    c = [s[0]]
    o=[1]
    k=1
    while k<n:
        if s[k] == s[k-1]:
            o[-1] += 1
        else:
            o.append(1)
            c.append(s[k])
        k += 1
        l=list(zip(c,o))
    return l



def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    n = len(s)
    k=1
    if s == '':
        return []
    while k<n and s[k] == s[0]:
        k += 1
    sr = s[k:]
    return [(s[0],k)] + artcode_r(sr)



#### Fonction principale


def main():
    '''
    tester les fonctions artcode_i et artcode_r
    '''
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
