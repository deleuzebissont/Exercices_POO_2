import random


# nous creeons la class Hero
class Hero:
    def __init__(self, nom):
        # je definis les attributs du hero
        self.nom = nom
        self.Nb_de_vie = 2 * random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_defense = random.randint(1, 6)

    def attaque(self, force_attaque):
        # la force de l attaque correspond a la force du personnage + un certain nombre
        return force_attaque + random.randint(1, 6)

    def recevoir_des_dommages(self, force_defense, nb_de_dommages, Nb_de_vie):
        # le nombre de dommages recu est egal a celui ci moins la defense du personnage
        Nb_de_vie -= nb_de_dommages - force_defense

    def est_vivant(self, Nb_de_vie):
        # si le nombre de vie est negatif, il est faux que le personnage est vivant
        if Nb_de_vie > 0:
            est_vivant = True
            return est_vivant
        else:
            est_vivant = False
            return est_vivant
