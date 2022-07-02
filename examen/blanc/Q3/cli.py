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


    def mainloop(self):
        """Boucle principale du CLI."""
        while True:
            self.montrer_personnage()
            print("Que voulez-vous faire?")
            print("(0) quitter le jeu")
            print("(1) afficher l'inventaire")
            reponse = input("> ")
            match(reponse):
                case "0": break
                case "1": self.montrer_inventaire()


def main():
    """Jouer en CLI."""
    view = View(Game())  # instancier vue et s'attacher au jeu
    view.mainloop()



if __name__ == "__main__":
    main()
