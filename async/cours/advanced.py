# Exercice : lisez les fonctions en début de fichier avant le main(),
#            puis implémentez chacune des opérations décrites dans main(), dans l'ordre
#            N'oubliez pas la documentation d'asyncio : https://docs.python.org/3/library/asyncio-task.html
import asyncio
import threading
import time

def old_async_add(a, b, callback):
    time.sleep(1)
    callback(a + b)

async def count_sheep(flag_holder):
    # TODO: ajouter l'annulation si flag_holder[0] devient True, avec asyncio.CancelledError
    sum = 0
    for n in range(1_000_000_000):
        if flag_holder[0]: raise asyncio.CancelledError()
        await asyncio.sleep(1) # chaque étape prend du temps
        sum += n
    return sum

async def main():
    # 5: Écrivez une fonction qui réutilise "old_async_add" mais retourne une future, puis "await"-ez l'ajout de 1 + 1 ici et "print"-ez le résultat

    # 6: Lancez `count_sheep` mais si cela ne se termine pas avant 5 seconds, annulez-le
    #    Indice: pour convertir la coroutine `count_sheep` en un Future, utilisez `asyncio.create_task`

    pass

if __name__ == "__main__":
    asyncio.run(main())
