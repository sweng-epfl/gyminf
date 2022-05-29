# Exercice : Ajoutez un cache et du prefetching pour diminuer la latence totale
# Indice : `threading.Thread(target=nom_de_la_fonction, args=[arguments]).start()` pour lancer une tâche en arrière-plan

import threading
import time

def get_item(n):
    # Simulation d'une opération qui prend du temps
    time.sleep(2)
    return "#" + str(n)


# Utilisation de l'opération, en simulant 2 endroits qui en ont besoin
for n in range(5):
    print(get_item(n))
for n in range(5):
    print(get_item(n))
