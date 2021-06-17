# ======================    Pile    ==============================================
class Pile :
    def __init__(self, L):
        self.liste = L

    def afficher(self): 
        s = 'pile: '
        for e in self.liste:
            s += str(e) + ' '
        print(s)

    def empiler(self, e):
        self.liste.insert(0, e)

    def depiler(self):
        del self.liste[0]

    def sommet(self):
        return self.liste[0]

    def estVide(self):
        return len(self.liste) == 0

    def taille(self):
        return len(self.liste)

    def traiter(self):
        e = self.liste[0]
        del self.liste[0]
        return e

# ======================    File    ==============================================
class File :
    def __init__(self, L):
        self.liste = L

    def afficher(self):  # ou __str__
        s = 'file: '
        for e in self.liste:
            s += str(e) + ' '
        return s

    def traiter(self):
        e = self.liste[-1]
        del self.liste[-1]
        return e

    def enfiler(self, e):
        self.liste.insert(0, e)

    def estVide(self):
        return len(self.liste) == 0

    def longueur(self):
        return len(self.liste)

