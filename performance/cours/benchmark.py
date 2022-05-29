# Exercice : Essayez de benchmarker d'autres opérations sur une liste, ou dans d'autres contextes
#            Par exemple, est-ce qu'appendre une liste vide est plus rapide qu'une liste avec 1 élément ? avec 10 éléments ?
#            En fait, les 2 benchmarks existant font plus que simplement comparer appendre/prépendre ; pourquoi ?


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Opération à benchmarker 1 : appendre à une liste
def append_to_list():
    return lst + [0]

# Benchmark 1
def test_list_append(benchmark):
    benchmark(append_to_list)


# Opération à benchmarker 2 : préprendre à une liste
def prepend_to_list():
    return [0] + lst

# Benchmark 2
def test_list_prepend(benchmark):
    benchmark(prepend_to_list)


# TODO
