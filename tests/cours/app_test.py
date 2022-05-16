# Exercice optionnel : Testez la méthode main, avec des "end-to-end" tests donc simulation de l'input/output au lieu d'injecter des dépendances

from unittest import TestCase
from hamcrest import *

# permet de remplacer "input" par ce que l'on veut
# (consultez la doc si vous souhaitez en savoir plus)
from unittest.mock import patch

from app import main

class AppTests(TestCase):
    def test_1_joke(self):
        # on "mock" des fonctions/objets avec patch
        # "patch" avec 1 seul argument ajoute un argument à la fonction qui représente le "mock"
        # avec 2 arguments, il permet de rapidement patcher une fonction ou un objet sans explicitement représenter le "mock"
        @patch("builtins.print")
        @patch("builtins.input", lambda *args: '1')
        def core(mock_print):
            main()
            # TODO : tester plus que juste le nombre d'appels :-)
            assert_that(mock_print.call_args_list, has_length(3))
        core() # sans argument, ils sera fournis par le décorateur "patch"... c'est un peu magique mais ça marche

    # TODO : que se passe-t-il si on demande 0 blagues ? -10 ? un lézard ?
