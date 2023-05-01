# Débogage et écriture de tests de régression

Cet exercice vous apprendra à utiliser un debugger pour inspecter l'état d'un programme. A cette fin,
on vous donne un programme qui contient un bug. Votre tâche est de trouver le bug et de le corriger.

Dans cet exercice, vous travaillez sur un programme qui gère une liste d'étudiants en informatique.
Le programme simule la journée de travail d'un groupe d'étudiants qui étudient dans des bâtiments à l'EPFL.

Malheureusement, cette fonctionnalité ne fonctionne actuellement pas. Votre tâche est de la réparer.
Le code de cette fonctionnalité se trouve dans [App.java](src/main/java/ch/epfl/sweng/App.java).

## Tâche : Inspection de la mémoire

Votre tâche consiste à examiner les problèmes liés à la fonctionnalité de simulation. La simulation
est définie dans [App.java](src/main/java/ch/epfl/sweng/App.java) dans la méthode `simulate()`. Bien que la simulation
semble se dérouler correctement, ce n'est pas le cas, car certaines pièces sont toujours occupées
après la fin de la simulation. Votre tâche consiste à :

1. Identifier le bug dans le code ;
2. Écrire un test de régression pour le bug que vous avez trouvé ; et
3. Corriger le bug.

Voici quelques conseils spécifiques à cette tâche :

- Votre IDE dispose probablement d'outils permettant d'explorer l'état du programme au moment de l'exécution. Par exemple,
  IntelliJ dispose d'un "Memory View" qui vous permet d'inspecter l'état de la mémoire au moment de l'exécution. Vous pouvez y
  Vous pouvez y accéder en cliquant sur le menu "Debug" lorsque le programme est en pause avec un point d'arrêt.
- Pouvez-vous identifier un point commun entre les étudiants qui ne parviennent pas à sortir ?
