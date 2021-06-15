def creer_pile():
    '''pour cr�er une pile'''
    return []
    
def empiler(ma_pile,valeur):
    '''ajoute une valeur à la pile'''
    ma_pile.append(valeur)

def depiler(ma_pile):
    '''retire le dernier élément de la pile'''
    assert len(ma_pile)>0
    return ma_pile.pop()
    
def sommet(ma_pile):
    '''renvoie le sommet de la pile donc du dernier élément ajouter'''
    assert len(ma_pile)>0
    return ma_pile[-1]
    
def taille(ma_pile):
    '''retourne la longueur de la pile'''
    return len(ma_pile)
    
def est_vide(ma_pile):
    '''renvoie True si la pile est vide'''
    return taille(ma_pile)==0