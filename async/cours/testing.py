# Exercice : lisez les fonctions en début de fichier avant le main(),
#            puis implémentez chacun des tests décrits, dans l'ordre
#            N'oubliez pas la documentation d'asyncio : https://docs.python.org/3/library/asyncio-task.html

import asyncio
import time
import threading

async def get_answer():
    await asyncio.sleep(1) # faisons semblant de travailler
    return 42

async def get_slow_answer():
    await asyncio.sleep(1000) # très lent !
    return 42

class View:
    def __init__(self):
        self.counter = 0

    def _increment_counter(self):
        time.sleep(1)
        self.counter = self.counter + 1

    def click_button(self):
        threading.Thread(target=self._increment_counter).start()


import unittest

class AsyncTests(unittest.IsolatedAsyncioTestCase):
    async def test_answer(self):
        # 8: Testez que get_answer retourne 42
        pass

    async def test_timeout(self):
        # 9: Testez get_slow_answer, mais le test doit échouer si cela prend plus de 5 secondes
        pass

    async def test_click(self):
        # 10: Testez que click_button incrémente le "counter" de View, *sans modifier la signature de View.click_button*
        pass
