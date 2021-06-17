from random import randint

n=50
#on commence par donner une taille pour notre labyrinthe ici 50*50
atteinte=[[False]*n for i in range(n)]
#atteinte correspont à une matrice (n,n) de booléens indiquant pour chaque case
#si elle a déjà été atteinte par un chemin (initialement False) 

# On "importe" notre structure pile
def creer_pile():
    return[]

def depiler(p):
    assert len(p)>0
    return p.pop()

def empiler(p,v):
    p.append(v)

def taille(p):
    return len(p)

def est_vide(p):
    return taille(p)==0

def visiter(c):
    '''prend en paramètre c=(x,y) une "position" de la matrice et modifie le contenu de la matrice atteinte'''
    (x,y)=c
    if x<0 or x>=n or y<0 or y>=n:
        return
    atteinte[x][y]=True
    
def est_atteinte(c):
    '''prend en paramètre c=(x,y) une "position" de la matrice et consulte le contenu de la matrice atteinte'''
    (x,y)=c
    if x<0 or x>=n or y<0 or y>=n:
        return True
    else:
        return atteinte[x][y]
    
def choix(c):
    '''étant donné une position c=(x,y) détermine les positions adjacentes non encore visitées et retourne un tableau de valeurs de 0 à 4 éléments'''
    (x,y)=c
    r=[]
    def ajouter(p):
        #ici le tableau r est rempli par la fonction locale ajouter
        if not est_atteinte(p):
            r.append(p)
    ajouter((x-1,y))
    ajouter((x+1,y))
    ajouter((x,y-1))
    ajouter((x,y+1))
    return r

def tirage(tableau):
    '''choisit aléatoirement parmi les directions possibles renvoyés par la fonction choix'''
    n=len(tableau)
    assert n>0
    return tableau[randint(0,n-1)]

def labyrinthe():
    pile=creer_pile()
    #on utilise une pile pour contenir les emplacements à partir desquels
    #on est susceptible de se déplacer depuis la position (0,0)
    empiler(pile,(0,0))
    visiter((0,0))
    while not est_vide(pile):
        #tant que cette pile n'est pas vide, on extrait le sommet cellule
        cellule=depiler(pile)
        #on examine les déplacements encore possible à partir de la position
        #cellule donnés par la fonction choix qu'on choisit au hasard avec tirage
        c=choix(cellule)
        print(cellule)
        if len(c)>0:
            suivante=tirage(c)
            #on relie les positions cellule et suivante
            visiter(suivante)
            #on marque la position suivante comme étant atteinte avec visiter
            empiler(pile,cellule)
            #on remet cellule dans la pile
            empiler(pile,suivante)
            #on ajoute suivante dans la pile ainsi le parcours reprendra à partir de suivante


labyrinthe()