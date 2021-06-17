from collections import deque

def creer_file(ma_file):
   '''pour créer une file'''
   ma_file=deque()
    
def enfiler(ma_file,valeur):
     '''ajoute une valeur à la file'''
     ma_file.appendleft(valeur)
    
def defiler(ma_file):
    '''retire le premier élément de la file'''
    ma_file.pop()
    
def sommet(ma_file):
    '''renvoie le premier élément ajouté dans la file'''
    return ma_file[-1]
    
def taille(ma_file):
    '''retourne la longueur de la pile'''
    return len(ma_file)
    
def est_vide(ma_file):
    '''renvoie True si la pile est vide'''
    return taille(ma_file)==0