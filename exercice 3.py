from math import pi


# nous importons pi de la librairie math

class Cercle:
    def __init__(self, rayon):
        # nous pourrons definir la valeur du rayon plus tard dans le code lorsque nous allons creer les differents
        # cercles
        self.rayon = rayon

    def calcul_aire(self):
        # nous retournons la formule de l aire d un cercle
        return self.rayon ** 2 * pi

    def calcul_circonference(self):
        # nous retournons la formule de la circonference d un cercle
        return self.rayon * 2 * pi
