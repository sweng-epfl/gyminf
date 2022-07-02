from dataclasses import dataclass
import unittest
from hamcrest import assert_that, equal_to

@dataclass(frozen=True)
class Potion:
    name: str
    value: int

class Game:
    def __init__(self):
        self._inventory = {Potion("Petite potion", 20): 3, Potion("Grande potion", 50): 1}
        self._health = 100
        self._x = 0
        self._y = 0

    def move(self, delta_x, delta_y):
        """Retourne None si tout s'est bien passé, ou un message d'erreur."""

        if self._health <= delta_x + delta_y:
            return "Pas assez de santé pour se déplacer autant"

        new_x = self._x + delta_x
        if new_x < 0:
            return "Impossible d'aller autant à gauche"

        new_y = self._y + delta_y
        if new_y < 0:
            return "Impossible d'aller autant en bas"

        self._x = new_x
        self._y = new_y
        self._health = self._health - delta_x - delta_y
        return None

    def consume(self, potion):
        """Retourne None si tout s'est bien passé, ou un message d'erreur."""

        if potion not in self._inventory:
            return "Cette potion n'est pas dans l'inventaire"

        self._health = self._health + potion.value
        self._inventory[potion] = self._inventory[potion] - 1

        if self._inventory[potion] == 0:
            del self._inventory[potion]
        return None

    def health(self):
        return self._health

    def position(self):
        return (self._x, self._y)

    def inventory(self):
        return { p: n for (p, n) in self._inventory.items() }


class PotionGameTest(unittest.TestCase):
    """Tests visant 100% de couverture pour une utilisation minimale du prototype de jeu."""

    def setUp(self):
        """Effectuer mise en place minimale avant chaque test."""
        self.game = Game()

    def get_potions(self, taille):
        """Extraire de l'inventaire les potions d'une certaine taille."""
        return [p for p in self.game.inventory() if p.name == f"{taille} potion"]

    def consommer_potion_apres_comptage(self, taille):
        """Consommer une potion et retourner des données obtenues avant.

        Retour: (valeur de la potion, variation du nombre de potions [début - fin])
        """
        potions = self.get_potions(taille)
        n_potions_debut = len(potions)
        potion = potions[0]
        pv_par_potion = potion.value
        self.game.consume(potion)
        potions = self.get_potions(taille)
        n_potions_fin = len(potions)
        return pv_par_potion, n_potions_debut - n_potions_fin

    def test_choix_petite_potion(self):
        """Tester que la bonne potion est choisie."""
        taille = "Petite"
        potion = self.get_potions(taille)[0]
        assert_that(potion.name, equal_to(f"{taille} potion"),
                    f"On aurait du obtenir une {taille} potion")

    def test_consommation_effective_petite_potion(self):
        """Tester que la consommotion d'une potion l'enlève de l'inventaire."""
        taille = "Petite"
        _, delta_potions = self.consommer_potion_apres_comptage(taille)
        assert_that(delta_potions, equal_to(1),
                    f"il ne devrait pas rester de {taille} potion")

    def test_consommation_effective_grande_potion(self):
        """Tester que la consommotion d'une potion l'enlève de l'inventaire."""
        taille = "Grande"
        _, delta_potions = self.consommer_potion_apres_comptage(taille)
        assert_that(delta_potions, equal_to(1),
                    f"il ne devrait pas rester de {taille} potion")

    def test_guerison_petite_potion(self):
        """Tester que la consommotion d'une potion donne le bon nombre de pvs."""
        taille = "Petite"
        pvs = self.game.health()
        _, valeur = self.consommer_potion_apres_comptage(taille)
        assert_that(self.game.health(), equal_to(pvs + valeur),
                    f"la potion devrait ajouter {valeur} points de vie")

    def test_mouvement_x_possible(self):
        """Tester le mouvement horizontal."""
        DELTA_X = 10
        x_debut = self.game.position()[0]
        self.game.move(DELTA_X, 0)
        assert_that(self.game.position()[0], equal_to(x_debut + DELTA_X),
                    f"le mouvement devrait ajouter {DELTA_X} unités à x")

    def test_mouvement_y_possible(self):
        """Tester le mouvement vertical."""
        DELTA_Y = 10
        y_debut = self.game.position()[1]
        self.game.move(0, DELTA_Y)
        assert_that(self.game.position()[1], equal_to(y_debut + DELTA_Y),
                    f"le mouvement devrait ajouter {DELTA_Y} unités à y")

    def test_mouvement_x_impossible(self):
        """Tester le mouvement horizontal interdit."""
        DELTA_X = -10
        x_debut = self.game.position()[0]
        self.game.move(DELTA_X, 0)
        assert_that(self.game.position()[0], equal_to(x_debut),
                    f"le mouvement devrait être impossible")

    def test_mouvement_y_impossible(self):
        """Tester le mouvement vertical interdit."""
        DELTA_Y = -10
        y_debut = self.game.position()[1]
        self.game.move(0, DELTA_Y)
        assert_that(self.game.position()[1], equal_to(y_debut),
                    f"le mouvement devrait être impossible")

    def test_mouvement_long_impossible(self):
        """Tester le mouvement au-delà de la santé."""
        DELTA_X = 1000
        DELTA_Y = 1000
        pos_debut = self.game.position()
        self.game.move(DELTA_X, DELTA_Y)
        assert_that(self.game.position(), equal_to(pos_debut),
                    f"le mouvement devrait être impossible")
