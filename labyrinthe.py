from random import randint

n=50
atteinte=[[False]*n for i in range(n)]

def creer_pile(c):
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
    (x,y)=c
    if x<0 or x>=n or y<0 or y>=n:
        return
    atteinte[x][y]=True
    
def est_atteinte(c):
    (x,y)=c
    if x<0 or x>=n or y<0 or y>=n:
        return True
    else:
        return atteinte[x][y]
    
def choix(c):
    (x,y)=c
    r=[]
    def ajouter(p):
        if not est_atteinte(p):
            r.append(p)
    ajouter((x-1,y))
    ajouter((x+1,y))
    ajouter((x,y-1))
    ajouter((x,y+1))
    return r

def tirage(tableau):
    n=len(tableau)
    assert n>0
    return tableau[randint(0,n-1)]

def labyrinthe():
    pile=creer_pile(n*n)
    empiler(pile,(0,0))
    visiter((0,0))
    while not est_vide(pile):
        cellule=depiler(pile)
        c=choix(cellule)
        print(cellule)
        if len(c)>0:
            suivante=tirage(c)
            #c'est ici qu'on relie les cases cellule et suivante
            visiter(suivante)
            empiler(pile,cellule)
            empiler(pile,suivante)