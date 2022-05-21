# Exercice : Convertissez cette application pour utiliser le pattern MVP, donc :
#            un "model" qui contient la logique, une "view" dédiée à l'affichage et aux interactions utilisateur, et un "presenter" qui médie
"""Implémentation en MVP de la consultation de météo aléatoire.

    La Vue est le "centre" de l'application dans cette version. Elle peut
    communiquer de manière bidirectionnele avec le Presenter, donc les instances
    de chacune de ces classes auront une référence vers une instance de l'autre.

    Le Modèle, en revanche, n'a aucune connaissance de la Vue ou du Presenter, qui
    lui, en revanche, peut consulter le Modèle.
"""

from weather_model import WeatherModel


class WeatherView:
    """UI pour la météo (sous forme de CLI). """

    def __init__(self):
        """Initialiser la vue."""
        self.presenter = None

    def montrer(self, meteo_actuelle: str):
        """Montrer la météo actuelle."""
        print("Météo actuelle: " +
              meteo_actuelle if meteo_actuelle is not None else "???")

    def start(self, presenter):
        """Connecter la Vue à un Presenter et démarrer l'UI."""
        self.presenter = presenter
        assert self.presenter.view == self
        while True:
            input("Appuyez sur Entrée pour vérifier la météo")
            presenter.demander_meteo()


class WeatherPresenter:
    """Médiateur entre le Modèle et la Vue de la météo."""

    def __init__(self, model, view):
        """Initialiser l'application météo."""
        self.model = model
        self.view = view

    def demander_meteo(self):
        """Obtenir la météo actuelle puis en demander l'affichage."""
        meteo = self.model.lire_meteo()
        self.view.montrer(meteo)


if __name__ == "__main__":
    model = WeatherModel()
    view = WeatherView()
    presenter = WeatherPresenter(model, view)
    view.start(presenter)
