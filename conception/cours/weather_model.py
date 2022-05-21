"""Modèle pour l'application de météo aléatoire.

Le Modèle est totalement indépendant de la vue et des intermédiaires vers la
Vue. Il peut être exactement le même que le reste de l'application soit
implémenté en suivant le pattern MVC, MVP, MMVV ou autre chose.

Un "Middleware" est aussi rendu disponible pour essayer jusqu'à 5 appels d'une
fonction sans argument pouvant retourner None, dans l'espoir d'obtenir autre
chose.
"""

import random
from typing import Optional


class WeatherModel:
    """Modèle de météo aléatoire.

    Attributs publics:
    - meteo: Optional[str] -- la météo actuelle
    """

    def lire_meteo(self) -> Optional[str]:
        """Fournir une nouvelle météo du jour."""
        weather = random.randrange(0, 4)
        if weather == 0:
            return "Ensoleillé"
        if weather == 1:
            return "Pluvieux"
        return None


def retry_five(foo):
    """Appeller une fonction sans argument jusqu'à 5 fois pour éviter None."""
    result = None
    for _ in range(5):
        result = foo()
        if result is not None:
            break
    return result
