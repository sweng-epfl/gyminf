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

    def get_potions(self, taille):
        """Revevoir une liste des petites potions restantes."""
        return [p for p in self.game.inventory() if p.name == f"{taille} potion"]

    def setUp(self):
        """Effectuer mise en place minimale avant chaque test."""
        self.game = Game()

    def consommer_potion_apres_comptage(self, taille):
        """Consommer une potion et retourner combien il y en avait avant."""
        potions = self.get_potions(taille)
        n_potions = len(potions)
        self.game.consume(potions[0])
        potions = self.get_potions(taille)
        return n_potions

    def test_consommation_effective_petite_potion(self):
        """Tester que la consommotion d'une potion l'enlève de l'inventaire."""
        taille = "Petite"
        n_potions = self.consommer_potion_apres_comptage(taille)
        assert_that(len(potions), equal_to(n_potions - 1),
                    f"il ne devrait pas rester de {taille} potion")

    def test_consommation_effective_grande_potion(self):
        """Tester que la consommotion d'une potion l'enlève de l'inventaire."""
        taille = "Grande"
        n_potions = self.consommer_potion_apres_comptage(taille)
        assert_that(len(potions), equal_to(n_potions - 1),
                    f"il ne devrait pas rester de {taille} potion")
