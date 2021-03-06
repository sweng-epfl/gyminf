# Exercice : Même code, cette fois ajoutez des pré/postconditions, invariants, et assertions
#            Pouvez-vous rendre les bugs plus facile à localiser, en devant passer moins de temps dans un debugger ?

class BinaryTree:
    def __init__(self, val, l, r):
        self.value = val
        self.left = l
        self.right = l

    @staticmethod
    def from_list(lst):
        mid = len(lst) // 2
        return BinaryTree(lst[mid], BinaryTree.from_list(lst[:mid]), BinaryTree.from_list(lst[mid:]))

    def to_list(self):
        result = []
        if self.left is not None:
            result += self.left.to_list()
        result.append(self.value)
        if self.right is not None:
            result += self.right.to_list()
        return result


lst = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU"]
tree = BinaryTree.from_list(lst)
lst2 = tree.to_list()

print("Liste : " + str(lst))
print("Liste après conversion aller-retour : " + str(lst2))
