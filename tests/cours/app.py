from joker import Joker

# Méthode principale séparée afin de pouvoir la tester
def main():
    print("Bonjour ! Combien de blagues voulez-vous ? (en anglais, désolé, pas de bonne API pour blagues française...)", end=" ")
    count = int(input())
    Joker().get_jokes(count)
    print("J'espère que vous avez bien ri ! Au revoir !")

if __name__ == "__main__":
    main()
