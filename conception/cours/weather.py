# Exercice : Convertissez cette application pour utiliser le pattern MVP, donc :
#            un "model" qui contient la logique, une "view" dédiée à l'affichage et aux interactions utilisateur, et un "presenter" qui médie

import random

while True:
    input("Appuyez sur Entrée pour vérifier la météo")
    weather = random.randrange(0, 4)
    if weather == 0:
        print("Météo actuelle : Ensoleillé")
    elif weather == 1:
        print("Météo actuelle : Pluvieux")
    else:
        print("Météo actuelle : ???")
