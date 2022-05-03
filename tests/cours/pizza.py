class Pizza:
    # Crée une Pizza avec le nom donné, qui peut être un calzone, et avec les toppings donnés
    def __init__(self, name, is_calzone, toppings):
        # NOTE: Pour cet exercice, pas de vérification de type, pour None, etc. ;
        #       une vraie application devrait probablement l'inclure
        self.name = name
        self.is_calzone = is_calzone
        self.toppings = toppings

    # Crée une représentation textuelle de la pizza, au format "[Pizza/Calzone] [nom], [topping, ...]", utilisable via "str"
    # p.ex. str(Pizza("Diavola", False, ["piments"])) -> "Pizza Diavola, piments"
    def __str__(self):
        result = ""
        if self.is_calzone:
            result += "Calzone"
        else:
            result += "Pizza "
        for topping in self.toppings:
            result += ", "
            result += topping
            if topping == "ketchup":
                result += " (Mamma mia... pourquoi??)"
        return result
