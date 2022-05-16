# Exercice : Testez ces fonctions

import random

# Retourne le nombre 'n' de Fibonacci, ou lance une exception si n < 0
# p.ex. 0 -> 0, 5 -> 8
def fibonacci(n):
    if n < 0:
        raise ValueError("n doit être au moins 0")
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Sépare le string 'str' en utilisant le séparateur 'sep'
# p.ex. ("aXb", "X") -> ["a", "b"]
def split_string(str, sep):
    results = []
    current = ""
    for c in str:
        if c == sep:
            results.append(current)
            current = ""
        else:
            current += c
    results.append(current)
    return results

# Mélange le tableau 'arr' au hasard en le modifiant
# p.ex. avec [1, 2, 3] le tableau peut devenir [3, 1, 2] ou [2, 1, 3] ou ...
def shuffle(arr):
    for n in range(len(arr) - 2):
        m = random.randrange(0, len(arr) - n) + n
        arr[n], arr[m] = arr[m], arr[n]
