from datetime import date
import random
import threading
import time

class Model:
    # les deux callbacks prennent comme argument un string et ne retournent rien
    def get_weather(self, date, success_callback, error_callback):
        result = random.randrange(0, 4)
        def thread_main():
            wait = random.randrange(1, 6) # faisons semblant que c'est un appel distant
            time.sleep(wait)
            if result == 0:
                success_callback("Ensoleillé")
            elif result == 1:
                success_callback("Pluvieux")
            else:
                error_callback("Impossible d'obtenir la météo, réessayez plus tard")
        t = threading.Thread(target=thread_main)
        t.start()


class ViewModel:
    pass # TODO

class View:
    pass # TODO
