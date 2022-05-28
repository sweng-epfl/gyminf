# Exercices pendant le cours


# Partie 1 : `benchmark.py`

Commencez par installer `pytest-benchmark` :

    python3 -m pip install pytest-benchmark

Puis lancez `pytest` sur un fichier de benchmark :

    pytest benchmark.py



# Partie 2 : `profiling.py`

Le module de profiling est intégré à Python, mais il faut installer un module pour visualiser les résultats, comme `flameprof` :

    python3 -m pip install flameprof

Lancez le profiling en préfixant l'exécution par `-m cProfile -o prof.out` :

    # pour le lancer normalement, ça serait `python3 profiling.py`
    # (le deuxième argument est le nom du fichier de résultats, ne pas le spécifier = résumé en ligne de commande)
    python3 -m cProfile -o prof.out profiling.py

Ensuite, créez un SVG (image vectorielle) avec flameprof :

    python3 -m flameprof prof.out > prof.svg

Le résultat contient deux graphes.
En haut, un "flame graph" normal : la fonction la plus en bas est celle par laquelle Python commence, le niveau directement
au-dessus contient les fonction que cette fonction de base appelle directement, etc. ; si une fonction n'a pas de couche par dessus, c'est que la fonction elle-même prend du temps.
En bas, un "flame graph" inversé, dans lequel les fonctions apparaissent en haut en proportion du temps d'exécution total, et pour chaque fonction sa couche du dessous
contient les fonctions qui l'appellent en proportion des appels.
