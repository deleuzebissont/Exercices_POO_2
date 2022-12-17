class Rectangle:
    def __init__(self, largeur, longueur):
        # je definis la fonction init pour que je puisse plus tard donner des paramteres qui seront les valeurs
        self.largeur = largeur
        self.longueur = longueur

    def calcul_aire(self, largeur, longueur):
        # je fais la formule de l aire d un rectangle soit largeur * longueur
        return self.largeur * self.longueur

    def afficher_infos(self):
        # je print la phrase me permettant d afficher toutes les informations du rectangle
        print(f"Largeur = {self.largeur}, Longueur = {self.longueur}, Aire = {self.calcul_aire(self.largeur, self.longueur)}")


# je donne comme parametre la largeur et la longueur qui sont tous les deux de 5
a = Rectangle(5, 5)
a.afficher_infos()
