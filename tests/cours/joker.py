# Exercice : Modifiez cette classe pour qu'elle soit testable, puis testez-là

from urllib.request import Request, urlopen

class Joker:
    def get_jokes(self, count):
        for n in range(count):
            req = Request("https://icanhazdadjoke.com", headers={"Accept": "text/plain", "User-Agent": "joker"})
            with urlopen(req) as response:
                content = response.read().decode('utf-8')
                print("Blague numéro", n, ":", content)
