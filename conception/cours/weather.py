# Exercice : Convertissez cette application pour utiliser le pattern MVP
# donc : un "model" qui contient la logique, une "view" dédiée à l'affichage
# et aux interactions utilisateur, et un "presenter" qui médie

import random


class Modele():

    def getMeteo(self):
        meteo = random.randrange(0, 4)
        if meteo == 0:
            return "Ensoleillé"
        elif meteo == 1:
            return "Pluvieux"
        else:
            return "???"


class Vue():

    def affiche(self, meteo):
        print("Météo actuelle : " + meteo)

    def attend_entree(self, presenter):
        input("Appuyez sur Entrée pour vérifier la météo ")
        presenter.rend_entree()


class Presenteur():

    def __init__(self):
        self.modele = Modele()
        self.vue = Vue()
        self.run()

    def run(self):
        while True:
            self.vue.attend_entree(self)

    def rend_entree(self):
        self.vue.affiche(self.modele.getMeteo())

Presenteur()
