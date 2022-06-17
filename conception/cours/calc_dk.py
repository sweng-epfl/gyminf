# Exercice : Modularisez ce code, sans changer ce que l'utilisateur voit/fait

OPS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


def operer(operateur: str, arg1: int, arg2: int = 0) -> int:
    """Effectuer une opération"""
    return OPS[operateur](arg1, arg2)


def entier_ou_null(nombre: str) -> int:
    """Transformer en entier ou signaler que ce n'est pas possible et retourner None."""
    try:
        n = int(p)
        return n
    except ValueError:
        print("Erreur, je ne sais pas quoi faire avec : " + p)
        return None


def pol_calc(ordre: str):
    """Calculer à partir d'un ordre fourni en notation polonaise inverse."""
    parts = text.split(" ")
    lst = []
    for p in parts:
        if p == '':
            continue
        elif p in OPS:
            lst.append(operer(p, lst.pop(), lst.pop()))
        else:
            n = entier_ou_null(p)
            if n is not None:
                lst.append(n)
    if len(lst) == 1:
        print(lst.pop())
    else:
        print("Calcul invalide")


if __name__ == "__main__":
    while True:
        text = input("Calcul à faire ? (en notation polonaise inverse; ou 'sortir') ")
        if text == "sortir": break
        pol_calc(text)
