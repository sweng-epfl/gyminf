# Exercice : Modularisez ce code, sans changer ce que l'utilisateur voit/fait

while True:
    text = input("Calcul à faire ? (en notation polonaise inverse; ou 'sortir') ")
    if text == "sortir": break
    parts = text.split(" ")
    lst = []
    for p in parts:
        if p == '':
            continue
        elif p == '+':
            lst.append(lst.pop() + lst.pop())
        elif p == '-':
            r = lst.pop()
            l = lst.pop()
            lst.append(l - r)
        elif p == '*':
            lst.append(lst.pop() * lst.pop())
        elif p == '/':
            r = lst.pop()
            l = lst.pop()
            lst.append(l / r)
        else:
            try:
                n = int(p)
                lst.append(n)
            except ValueError:
                print("Erreur, je ne sais pas quoi faire avec : " + p)
                continue

    if len(lst) == 1:
        print(lst.pop())
    else:
        print("Calcul invalide")
