# Conception et refactoring

Cet exercice vous apprendra à extraire des abstractions du code existant. A cette fin, on vous fournit
un programme qui contient de nombreuses mauvaises pratiques de conception. Vous devrez remanier le code pour le rendre plus lisible et plus facile à maintenir.

## Tâche

Dans cet exercice, vous travaillez sur un programme qui vous permet de gérer le solde d'un compte bancaire.
Le solde du compte peut être augmenté ou diminué par des montants arbitraires dans différentes unités monétaires.
Le programme vous permet également de convertir le solde dans une autre unité monétaire.

Cependant, ce programme souffre de plusieurs mauvaises pratiques de conception. Votre tâche consiste à remanier le code
afin d'éliminer les problèmes de code présents dans [src/main/java/App.java](src/main/java/App.java).
En particulier, vous devez :

1. Identifier les motifs répétitifs dans le code ; et
2. Refactorer soigneusement le code pour introduire de meilleures abstractions.
