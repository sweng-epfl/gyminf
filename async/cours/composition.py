# Exercice : lisez la documentation des fonctions en début de fichier avant le main(),
#            puis implémentez chacune des opérations décrites dans main(), dans l'ordre
#            N'oubliez pas la documentation d'asyncio : https://docs.python.org/3/library/asyncio-task.html

import asyncio
import threading

async def upload(text):
    await asyncio.sleep(1) # faisons semblant de travailler
    print("Uploadé : " + text)

async def slow():
    await asyncio.sleep(1) # idem
    return "Réponse lente"

def fast():
    return "Réponse rapide"


async def main():
    # 1: Imprimez avec `print` le résultat de `slow`

    # 2: Uploadez avec `upload` le résultat de `slow`

    # 3: Transformez le résultat de `fast` en un Future, et imprimez avec `print` son résultat

    # 4: Combinez `slow` et `fast` pour obtenir le résultat qui arrive le premier et imprimez-le avec `print`
    #    Astuce: `next(iter(s))` pour obtenir un élément d'un `set` nommé `s`

    # 5: Combinez `slow` et `fast` pour obtenir les 2 résultats en même temps, et imprimez-les avec `print`

    pass

if __name__ == "__main__":
    asyncio.run(main())
