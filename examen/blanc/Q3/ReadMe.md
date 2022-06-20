# Question 3 : Jeu de rôle [56 points]

Votre équipe développe un jeu de rôle.
Le projet en est à ses débuts, et vous êtes l'un des deux programmeurs de l'équipe.
La première tâche est de créer un produit minimum viable.

_**Note**: Les deux parties de cette question sont indépendantes._


## Partie 1 : Tester la logique [24 points]

L'autre programmeur a écrit la logique principale du code, puis est parti en vacances.
Pour éviter une mauvaise surprise, votre équipe décide qu'il faut écrire des tests pour ce code.
Cependant, les messages d'erreurs et le contenu de l'inventaire au départ ne sont pas encore complètement décidés,
si ce n'est que le joueur commencera avec au moins une potion dans son inventaire.

Écrivez des tests pour `Game` dans `game.py` qui obtiennent 100% de couverture d'instructions.

_Vous obtiendrez 10 points pour au moins 50% de couverture avec du code de test propre._
_Vous obtiendrez 14 points de plus pour 100% de couverture._

_**Rappel**: Suivez les instructions [vues en cours](../../../tests/cours/ReadMe.md) pour mesurer la couverture de code._


## Partie 2 : Interface utilisateur [32 points]

Il est maintenant temps d'ajouter une interface utilisateur.
Pour ce produit minimum, le jeu n'aura qu'une interface en ligne de commande basée sur des commandes à entrer,
mais une interface graphique est déjà prévue.

Les récits utilisateurs à implémenter sont les suivants :

1. En tant que joueur, je veux voir à tout instant la position de mon personnage, afin de pouvoir faire des choix appropriés à la situation
2. En tant que joueur, je veux pouvoir afficher les objets actuellement dans mon inventaire, afin de savoir quelles actions je peux prendre
3. En tant que joueur, je veux pouvoir faire un pas dans une des quatres directions cardinales, afin d'explorer le monde
4. En tant que joueur, je veux pouvoir quitter le jeu, afin de ne pas en devenir dépendant

Implémentez ces récits. Vous pouvez le faire de la manière que vous voulez, en créant ou non de nouveaux fichiers.

_Vous obtiendrez 4 points par récit utilisateur implémenté, plus 4 points par récit implémenté de manière propre et adaptée à la situation._
