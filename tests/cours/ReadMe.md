# Exercices pendant le cours

Installez Hamcrest d'abord :

    python3 -m pip install pyhamcrest

Puis créez un fichier avec vos tests, p.ex., `my_tests.py`, qui commencera par :

    from unittest import TestCase
    from hamcrest import *

    # idéalement avec un meilleur nom que "MyTests" :-)
    class MyTests(TestCase):
        ...

Enfin, lancez les tests :

    python3 -m unittest my_tests.py

Vous pouvez aussi lancer les tests depuis un IDE, souvent via un clic droit sur le fichier de tests ou sur une fonction de test.


Pour la couverture de code, installez Coverage :

    python3 -m pip install coverage

Puis utilisez-le en remplaçant `python3` par `coverage run` pour lancer les tests :

    coverage run -m unittest my_tests.py

Enfin, affichez les résultats (en filtrant pour ne voir que les fichiers dans ce dossier, pas dans la librairie standard Python) :

    coverage report --include=./*

Vous pouvez remplacer `report` par `html` pour générer un fichier HTML avec le code source annoté.

Pour la couverture de branches, ajoutez ` --branch` après `run`.

Là aussi votre IDE vous permet normalement d'exécuter les tests avec couverture et de visualiser le résultat directement sur le code.
