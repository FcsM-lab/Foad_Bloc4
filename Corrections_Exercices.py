################STRUCTURE PILE################
def creer_pile():
    '''pour créer une pile'''
    return []
    
def empiler(ma_pile,valeur):
    '''ajoute une valeur Ã  la pile'''
    ma_pile.append(valeur)

def depiler(ma_pile):
    '''retire le dernier Ã©lÃ©ment de la pile'''
    assert len(ma_pile)>0
    return ma_pile.pop()
    
def sommet(ma_pile):
    '''renvoie le sommet de la pile donc du dernier Ã©lÃ©ment ajouter'''
    assert len(ma_pile)>0
    return ma_pile[-1]
    
def taille(ma_pile):
    '''retourne la longueur de la pile'''
    return len(ma_pile)
    
def est_vide(ma_pile):
    '''renvoie True si la pile est vide'''
    return taille(ma_pile)==0

#############EXERCICE 1##################

#Comme toujours lorsqu'il s'agit d'associer deux entités (ici, taille et prix), on utilisera un dictionnaire.

prix={'XS':8 , 'S':10 , 'M':12 , 'L':14 , 'XL':16 , 'XXL':18}

dico={}
tailles=['XS','S','M','L','XL','XXL']

for i in range (len(tailles)):
    if i==0:
        dico[tailles[i]]=8
    else:
        dico[tailles[i]]=round(dico.get(tailles[i-1])+dico.get(tailles[i-1])**0.5/2,2)
 
#print(dico)

       
#############EXERCICE 2##################
#Il suffit de parcourir l'expression E et d'effectuer des tests pour savoir si
#le caractère rencontré est un nombre, une opération ou un espace.
#On peut utiliser la méthode isdigit pour savoir si la caractre est un nombre.
        
def separe(E):
    nombres,operations=[],[]
    for i in E:
        if i.isdigit():
            nombres.append(i)
        if i in '+-*/':
            operations.append(i)
    return nombres,operations

#print(separe('3+5*9-6'))
 
    
#############EXERCICE 3##################
#Il s'agit ici d'empiler les crochets et les parenthèses ouvrant.e.s 
#et de dépiler quand on rencontre son équivalent fermant.e

def bien_parenth(E):
    pile=creer_pile()
    for i in E:
        if i=='(' or i=='[':
            empiler(pile,i)
        elif i==')':
            if sommet(pile)=='(':
                depiler(pile)
            else:
                return False
        elif i==']':
            if sommet(pile)=='[':
                depiler(pile)
            else:
                return False
    if est_vide(pile):
        return True
    
#print(bien_parenth('(3+4)*5+[2-(3+4)]/5'))
        
    
#############EXERCICE 5##################
def eval_npi(exp):
    p=creer_pile()
    #on commence par créer une pile p
    for c in exp:
        #on parcourt tous les éléments du tableau exp
        if c=='+' or c=='*':
            #si l'élément courant est un opérateur arithmétique, 
            #on dépile les deux opérandes x et y de p et on empile x+y ou x*y
            #selon la valeur de c
            y=depiler(p)
            x=depiler(p)
            empiler(p,x+y if c=='+' else x*y)
        else:
            #sinon c est un nombre et on l'empile dans p
            empiler(p,c)
    #quand on sort de la boucle for, il ne reste plus qu'à dépiler la valeur 
    #finale v et à vérifier que la pile p est bien vide
    v=depiler(p)
    assert est_vide(p)
    return v

#print(eval_npi([1,2,'+',3,'*']))

#print(eval_npi([1,2,'+',3,'+']))


