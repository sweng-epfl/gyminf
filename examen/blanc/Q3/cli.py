#!/usr/bin/env python3
"""Interface CLI pour le prototype de jeu de rôle."""

from game import Game


class View:
    """Vue CLI du jeu - pas propre (ni MVC, ni MVP ni MVVM)."""

    def __init__(self, jeu):
        """S'attacher à un ViewModel."""
        self.game = jeu

    def montrer_personnage(self):
        """Montrer l'état actuel du personnage."""
        x, y = self.game.position()
        print(f"Position: ({x}, {y})")

    def montrer_inventaire(self):
        """Montrer l'inventaire actuel."""
        inventaire = self.game.inventory()
        print("Inventaire:")
        for thing in inventaire:
            print(thing)

    def se_deplacer(self, delta_x, delta_y):
        """Demander au jeu de déplacer le personnage."""
        self.game.move(delta_x, delta_y)

    def mainloop(self):
        """Boucle principale du CLI."""
        while True:
            self.montrer_personnage()
            print("Que voulez-vous faire?")
            print("(i) afficher l'inventaire")
            print("(n) se déplacer au nord")
            print("(s) se déplacer au sud")
            print("(e) se déplacer au est")
            print("(w) se déplacer à l'ouest")
            print("(q) quitter le jeu")
            reponse = input("> ")
            match(reponse):
                case "q": break
                case "i": self.montrer_inventaire()
                case "n": self.se_deplacer(0, 1)
                case "s": self.se_deplacer(0, -1)
                case "e": self.se_deplacer(1, 0)
                case "w": self.se_deplacer(-1, 0)


def main():
    """Jouer en CLI."""
    view = View(Game())  # instancier vue et s'attacher au jeu
    view.mainloop()



if __name__ == "__main__":
    main()
