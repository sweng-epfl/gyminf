"""Implémentation en MVC de la consultation de météo aléatoire.

    Le Contrôle est le "centre" de l'application dans cette version.
    Il possède des références vers le Modèle et la Vue, qu'il peut
    respectivement consulter et mettre à jour.

    C'est du coup au Contrôle de gérer les entrées (donc la partie "input" de la
    communication avec l'utilisateur).
"""

from weather_model import WeatherModel, retry_five


class WeatherView:
    """UI pour la météo (sous forme de CLI)."""

    def montrer(self, meteo_actuelle: str):
        """Montrer la météo actuelle."""
        print("Météo actuelle: " + (meteo_actuelle
                                    if meteo_actuelle is not None
                                    else "???"))


class WeatherControl:
    """Contrôle de l'application."""

    def __init__(self):
        """Initialiser l'application météo."""
        self.model = WeatherModel()
        self.view = WeatherView()

    def demander_meteo(self):
        """Obtenir la météo actuelle puis en demander l'affichage."""
        meteo = retry_five(self.model.lire_meteo)
        self.view.montrer(meteo)

    def mainloop(self):
        """Démarrer l'App."""
        while True:
            input("Appuyez sur Entrée pour vérifier la météo")
            self.demander_meteo()


if __name__ == "__main__":
    WeatherControl().mainloop()
