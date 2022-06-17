# Exercice : Convertissez cette application pour utiliser le pattern MVP, donc :
#            un "model" qui contient la logique, une "view" dédiée à l'affichage et aux interactions utilisateur, et un "presenter" qui médie

"""Implémentation en MVVM de la consultation de météo aléatoire.
"""
from weather_model import WeatherModel


class WeatherView:
    """UI pour la météo (sous forme de CLI).

    Attributs:
    - callback_demande: fonction de callback à appeler lorsqe l'utilisiteur demande la météo
    """

    def __init__(self):
        """Initialiser l'instance."""
        self.callback_demande = None

    def montrer(self, meteo_actuelle: str):
        """Montrer la météo actuelle."""
        print("Météo actuelle: " +
              meteo_actuelle if meteo_actuelle is not None else "???")

    def check_input(self):
        """Vérifier si l'utilisateur veut une nouvelle météo."""
        input("Appuyez sur Entrée pour vérifier la météo")
        if self.callback_demande is not None:
            self.callback_demande()
        else:
            print("Aucun modèle de météo n'est disponible.")

    def connecter_demande(self, callback_demande):
        """Connecter une fonction de callback pour la demande de météo."""
        self.callback_demande = callback_demande


class WeatherModelView:
    """UI virtuel."""

    def __init__(self, model, view):
        """Initialiser l'application météo."""
        self.model = model
        self.view = view
        self.view.connecter_demande(self.demander_meteo)

    def demander_meteo(self):
        """Obtenir la météo actuelle puis en demander l'affichage."""
        meteo = self.model.lire_meteo()
        self.view.montrer(meteo)

    def start(self):
        """Lancer l'application."""
        while True:
            self.view.check_input()


if __name__ == "__main__":
    WeatherModelView(
        WeatherModel(), WeatherView()
    ).start()
