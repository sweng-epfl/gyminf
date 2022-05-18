# Exercice : Ce code n'est pas top, mais concrètement quels problèmes a-t-il ? Qu'est-ce qui le rend difficile à lire ?

class planet:
  def __init__(s, x, d):
        s.planet_name = x
        s.distanceFromSun = d

def FindClosestPlanet(ps, d):
   # Trie les planètes
   sorted(ps, key=lambda s: s.distanceFromSun)
   tot = 0
   old = ps[0]
   for p in ps:
     #print(p.distance_from_sun)
     if (p.distanceFromSun - old.distanceFromSun) * 0.5 + old.distanceFromSun > d:
       return old.planet_name
     # Redéfinit old
     old = p
   return ps[-1]

xs = [
  planet("Mercure", 58), planet("Vénus", 108),
  planet("Terre", 150),
  planet("Mars", 228),
  planet("Jupiter", 778),
  planet("Saturne", 1427),
  planet("Uranus", 2871),
  planet("Neptune", 4497),
  #planet("Pluton", 5913)
]
i = input("Distance en millions de km du Soleil? ")
print("Planète la plus proche : " + FindClosestPlanet(xs, int(i)))
