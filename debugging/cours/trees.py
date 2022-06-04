# Exercice : Ce code a plusieurs bugs, trouvez-les en exécutant le code et debuggez-les à l'aide d'un debugger

class BinaryTree:
    def __init__(self, val, l, r):
        self.value = val
        self.left = l
        self.right = r

    @staticmethod
    def from_list(lst):
        mid = len(lst) // 2
        return BinaryTree(lst[mid], BinaryTree.from_list(lst[:mid]), BinaryTree.from_list(lst[mid+1:]))

    def to_list(self):
        result = []
        if self.left:
            result += self.left.to_list()
        result.append(self.value)
        if self.right:
            result += self.right.to_list()
        return result


lst = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU"]
tree = BinaryTree.from_list(lst)
lst2 = tree.to_list()

print("Liste : " + str(lst))
print("Liste après conversion aller-retour : " + str(lst2))
