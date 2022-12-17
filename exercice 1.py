class StringFoo:
    # j utilise la fonction __innit__ pour prendre en argument le nom
    def __init__(self, name):
        self.name = name

    def set_string(self, name):
        self.name = name

    # j utilise la fonction print_string pour afficher le string sur l ecran en majuscule
    def print_string(self):
        print(self.name.upper())


# je donne l argument en question, le nom qui est Thomas
a = StringFoo("Thomas")
a.print_string()