# Infrastructure

**Prérequis** : Avant de suivre cette conférence, vous devez :
> - Installer Git. Sous Windows, utilisez [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) car Git est principalement conçu pour Linux.
>   Sur macOS, voir [la documentation de git] (https://git-scm.com/download/mac). Sous Linux, Git est peut-être déjà installé, ou utilisez la gestionnaire de paquets de votre distribution.
>   Si vous avez installé Git avec succès, l'exécution de `git --version` dans la ligne de commande devrait afficher un numéro de version.
> - Créer un compte GitHub (vous n'êtes pas obligé d'utiliser un compte GitHub existant, vous pouvez en créer un uniquement pour ce cours si vous le souhaitez)
> - Configurer une clé SSH pour GitHub en suivant [leur documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
> - Dites à Git qui vous êtes en lançant `git config --global user.name 'votre_nom'` avec votre nom et `git config --global user.email 'votre_email'` avec l'e-mail que vous avez utilisé pour GitHub.
> - Choisissez un éditeur que Git ouvrira pour écrire un résumé de vos changements avec `git config --global core.editor 'votre_editeur'`,
>   puisque Git utilise par défaut `vi` qui est difficile à utiliser pour les nouveaux venus.
>   Sous Windows avec WSL, vous pouvez utiliser `notepad.exe`, qui ouvrira le Notepad de Windows.
>   Sous macOS, vous pouvez utiliser `open -e -W -n` qui ouvrira une nouvelle fenêtre TextEdit.
>   Sous Linux, vous pouvez utiliser l'éditeur de texte graphique intégré à votre distribution, ou `nano`.
>
> Si vous utilisez Windows avec WSL, notez que l'exécution de `explorer.exe .` à partir de la ligne de commande Linux
> ouvrira l'explorateur de Windows dans le dossier de votre ligne de commande, ce qui est pratique.
>
> Si vous le souhaitez, vous pouvez définir le paramètre de configuration de Git `core.autocrlf` à `true` sur Windows et `input` sur Linux et macOS,
> pour que Git convertisse automatiquement les fins de lignes à la manière d'Unix (`\n`) et les séparateurs de lignes à la manière de Windows (`\r\n`).


Où stockez-vous votre code et comment le modifiez-vous ?
Si vous écrivez votre propre logiciel, ce n'est pas un problème, car vous pouvez utiliser votre propre machine et modifier les fichiers que vous voulez quand vous le voulez.
Mais si vous travaillez avec quelqu'un d'autre, cela devient problématique.
Vous pouvez utiliser un service de cloud en ligne où vous stockez des fichiers et coordonnez qui modifie quel fichier et à quel moment.
Vous pouvez vous envoyer par courrier électronique des modifications apportées à des ensembles de fichiers.
Mais cela ne fonctionne pas aussi bien lorsque vous avez plus de personnes,
et c'est complètement inutilisable lorsque vous avez des dizaines ou des centaines de personnes qui travaillent sur la même base de code.
C'est là que l'infrastructure entre en jeu.


## Objectifs

- Contraster les anciens et les nouveaux systèmes de _gestion de version_
- Organiser votre code avec le système de gestion de version _Git_.
- Rédiger des descriptions utiles des modifications du code
- Éviter les erreurs avec l'_intégration continue_


## Qu'est-ce que la gestion de version ?

Avant de parler de la gestion du code à l'aide d'un système de gestion de version, il convient de définir certains termes.

Un _dépôt_ ("repository" en anglais) est un emplacement dans lequel vous stockez une base de code, par exemple un dossier sur un serveur distant.
Lorsque vous apportez un ensemble de modifications à un dépôt, vous _poussez_ ("push") des modifications.
Lorsque vous récupérez les modifications apportées par d'autres personnes dans le dépôt, vous _tirez_ ("pull") des modifications.

Un ensemble de modifications est appelé _commit_.
Un cimmit a quatre composantes principales : qui, quoi, quand et pourquoi.
"Qui" est l'auteur du commit, la personne qui a effectué les modifications.
Le "quoi" est le contenu du commit, les modifications elles-mêmes.
"Quand" est la date et l'heure à laquelle le commit a été effectué. Cette date peut être antérieure à la date à laquelle le commit a été poussé dans le dépôt.
Le "Pourquoi" est un message associé au commit qui explique pourquoi les modifications ont été apportées,
par exemple en expliquant pourquoi il y avait un bug et pourquoi le nouveau code corrige le bug.
Le "pourquoi" est particulièrement important, car vous devrez souvent revenir sur d'anciennes modifications et comprendre pourquoi elles ont été effectuées.

Il arrive parfois qu'une modification entraîne des problèmes. Il se peut qu'une modification censée améliorer les performances introduise un bug.
Les systèmes de gestion de version vous permettent d'inverser ("revert") ce commit, ce qui crée un nouveau commit dont le contenu est l'inverse de celui d'origine.
En d'autres termes, si le commit original a remplacé "X" par "Y", un commit inversé remplace "Y" par "X".
Il est important de noter que le commit original n'est pas perdu ou détruit, mais qu'un nouveau commit est créé.

Les modifications sont rassemblées dans un _historique_ des changements.
Au départ, un dépôt est vide. Ensuite, quelqu'un ajoute du contenu dans un commit, puis plus de contenu dans un autre commit, et ainsi de suite.
L'historique d'un dépôt contient donc toutes les modifications nécessaires pour passer de rien à l'état actuel.
Certaines de ces modifications peuvent faire l'objet d'allers-retours, comme les commits inversés, ou les commits qui remplacent le code qu'un commit précédent a ajouté.
À tout moment, n'importe quel développeur ayant accès au dépôt peut consulter l'historique complet pour savoir qui a effectué quelles modifications, quand et pourquoi.

Les systèmes de gestion de version de la première génération étaient essentiellement une couche d'automatisation sur la gestion manuelle des versions.
Comme nous l'avons mentionné précédemment, si vous développez avec quelqu'un d'autre, vous pouvez mettre vos fichiers quelque part et coordonner qui modifie quoi et quand.
Un système de première génération vous aide à faire cela avec moins d'erreurs, mais utilise toujours fondamentalement le même modèle.

Avec la gestion de version de première génération, si Alice veut travailler sur le fichier A, elle réserve ("check out") le fichier.
À ce moment-là, le fichier est verrouillé : Alice peut le modifier, mais personne d'autre ne peut le faire. Si Bob veut également réserver le fichier A, le système rejettera sa tentative.
Bob peut toutefois réserver le fichier B si personne d'autre ne l'utilise.
Une fois qu'Alice a terminé son travail, elle crée un commit avec ses modifications et libère la réservation. À ce moment-là, Bob peut réserver le fichier A et y apporter ses modifications.

Les systèmes de gestion de version de première génération agissent donc comme des verrous à la granularité des fichiers.
Ils empêchent les développeurs d'apporter des modifications parallèles au même fichier, ce qui permet d'éviter certaines erreurs mais n'est pas très pratique.
Par exemple, Alice peut vouloir modifier la fonction X dans le fichier A, tandis que Bob veut modifier la fonction Y dans le fichier A.
Ces modifications n'entreront pas en conflit, mais elles ne pourront toujours pas être effectuées en parallèle,
car les verrous de la première génération de gestion de version sont sur des fichiers entiers.

Les développeurs ont abandonné les systèmes de première génération parce qu'ils voulaient mieux contrôler les _conflits_.
Lorsque deux développeurs veulent travailler sur le même fichier en même temps,
ils devraient pouvoir le faire, à condition qu'ils puissent ensuite _fusionner_ ("merge") leurs modifications dans une version unifiée.
La fusion des modifications n'est pas toujours possible automatiquement.
Si deux développeurs ont modifié la même fonction de manière différente, par exemple, ils devront probablement discuter pour décider quelles modifications doivent être conservées.

Les _branches_ sont une autre fonctionnalité qui a du sens si un système peut gérer les conflits et les fusions.
Parfois, les développeurs souhaitent travailler en parallèle sur plusieurs copies de la base de code.
Par exemple, vous êtes peut-être en train de travailler sur des modifications visant à améliorer les performances, lorsqu'un client vous fait part d'un rapport de bug.
Vous pourriez corriger le bug et créer un commit avec la correction et vos modifications de performance, mais le commit résultant n'est pas pratique.
Si, par la suite, vous devez revenir sur les modifications de performance, par exemple, vous devrez également revenir sur la correction de bugs car elle se trouve dans le même commit.
Au lieu de cela, vous créez une branche pour vos changements de performance, puis vous passez à une branche pour la correction des bugs, et vous pouvez travailler sur les deux en parallèle.
Lorsque votre correction de bug est prête, vous pouvez la _fusionner_ dans la branche "principale" du dépôt, et il en va de même pour les changements de performance.
Une utilisation courante des branches concerne les versions : vous pouvez par exemple publier la version 1.0 de votre logiciel et créer une branche représentant l'état du dépôt pour cette version.
Vous pouvez alors travailler sur la future version 2.0 dans la branche "principale".
Si un client signale un bug dans la version 1.0, vous pouvez passer à la branche de la version 1.0, corriger le bug et publier la correction,
puis reprendre votre travail sur la version 2.0. Vos modifications pour la version 1.0 n'ont pas affecté votre branche principale, car vous les avez effectuées dans une autre branche.

Dans les logiciels modernes, le processus habituel de création de branches consiste à créer une branche à partir de la branche principale du dépôt,
puis ajouter des commits à la branche pour corriger un bug, ajouter une fonctionnalité ou effectuer toute autre tâche pour laquelle la branche a été créée,
et demander ensuite à un collègue de le réviser. Si le collègue demande des modifications, comme l'ajout de commentaires de code, vous pouvez ajouter un commit à la branche avec ces modifications.
Une fois que votre collègue est satisfait, vous pouvez fusionner les commits de la branche dans la branche principale.
Vous pouvez ensuite créer une autre branche pour travailler sur quelque chose d'autre, et ainsi de suite. Vos collègues travaillent eux aussi sur leurs propres branches.
Ce flux de travail permet à chacun de pousser les commits qu'il souhaite sur sa branche sans entrer en conflit avec les autres, même si son travail n'est pas encore tout à fait terminé.
Souvent, il est judicieux d'écraser les commits d'une branche en un seul commit et de fusionner le commit résultant dans la branche principale.
Cela permet de combiner toutes les modifications de la branche en un seul commit propre dans l'historique de la branche principale, plutôt que d'avoir un tas de commits qui font quelques petites modifications chacun mais qui n'ont aucun sens l'un sans l'autre.

Dans le cas de branches représentant des versions, il est parfois nécessaire d'appliquer les mêmes modifications à plusieurs branches.
Par exemple, en développant la version 2.0 dans la branche principale, vous pouvez trouver un bug et vous rendre compte que ce bug existe également dans la version 1.0.
Vous pouvez faire un commit corrigeant le bug dans la version 2.0, et ensuite "_cherry pick_" le commit dans la branche pour la version 1.0.
Tant que la modification n'entre pas en conflit avec d'autres modifications apportées à la branche de la version 1.0,
le système de contrôle de la version peut copier votre commit de correction de bug dans une commit pour une autre branche.

Les systèmes de gestion de version de deuxième génération avaient pour but de permettre aux développeurs de gérer les conflits.
Alice peut travailler sur le fichier A sans avoir besoin de le verrouiller, et Bob peut également travailler sur le fichier A en même temps.
Si Alice apporte ses modifications en premier, le système les acceptera, et lorsque Bob voudra ensuite appliquer ses modifications, deux choses pourront se produire.
Il est possible que les modifications soient fusionnées automatiquement, par exemple parce qu'elles concernent deux parties différentes du fichier.
L'autre possibilité est que les modifications soient contradictoires et doivent être fusionnées manuellement. Bob doit alors choisir ce qu'il faut faire, éventuellement en demandant à Alice, et produire une version "fusionnée" du fichier qui peut être transmise.

Le principal inconvénient du gestion de version de deuxième génération est sa centralisation.
Les développeurs travaillent avec un dépôt unique, hébergé sur un serveur.
La validation des modifications nécessite une connexion Internet à ce serveur.
C'est un problème si le serveur est en panne, si le développeur se trouve dans un endroit où il n'a pas accès à Internet, ou pour toute autre raison qui empêche le développeur d'atteindre le serveur.

Les systèmes de gestion de version de troisième génération sont axés sur la décentralisation.
Chaque machine possède son propre dépôt. Il ne s'agit pas d'une "sauvegarde" ou d'une "réplique" d'un dépôt "principal", mais simplement d'un autre clone du dépôt.
Les développeurs peuvent effectuer des modifications localement sur leur propre dépôt, puis transférer ces modifications vers d'autres clones du dépôt, par exemple sur un serveur.
Les développeurs peuvent également avoir plusieurs branches localement, avec des commits différents dans chacune d'entre elles, et pousser tout ou partie de ces branches vers d'autres clones du dépôt.
Tout cela fonctionne tant que les dépôts ont des historiques compatibles.
En d'autres termes, il n'est pas possible d'apporter une modification à un dépôt qui n'est pas basé sur le même historique que le dépôt local.

Dans la pratique, les équipes se mettent d'accord sur un dépôt "principal" vers lequel elles vont toutes envoyer des commits, et travaillent localement sur leur clone de ce dépôt.
Bien que, du point de vue du système de gestion de version, tous les clones du dépôt soient égaux,
il est pratique pour les développeurs de se mettre d'accord sur un seul endroit où tout le monde place ses modifications.

Le principal système de gestion de version utilisé aujourd'hui est _Git_.
Git a été inventé par Linus Torvalds, qui a inventé Linux, parce qu'il était fatigué des problèmes posés par le précédent système de gestion de version qu'il utilisait pour Linux.
Il existe également d'autres systèmes de gestion de version de troisième génération, tels que Mercurial et Bazaar, mais Git est de loin le plus utilisé.

De nombreux développeurs utilisent des sites web publics pour héberger le clone du dépôt "principal" de leurs projets.
Le plus connu aujourd'hui est GitHub, qui utilise Git mais n'y est pas techniquement lié.
GitHub ne se contente pas de stocker un clone de dépôt, mais peut également héberger une
liste de "problèmes" ("issues") pour le dépôt, tels que les bugs et les demandes de fonctionnalités, ainsi que d'autres données telles qu'un wiki pour la documentation.
Il existe également d'autres sites web présentant des caractéristiques similaires, tels que GitLab et BitBucket, bien qu'ils ne soient pas aussi populaires.

Un exemple de projet développé sur GitHub est [le runtime .NET](https://github.com/dotnet/runtime), qui est développé principalement par des employés de Microsoft et entièrement sur GitHub.
Les conversations sur les bugs, les demandes de fonctionnalités et les révisions de code se déroulent au grand jour, sur GitHub.


## Comment utiliser Git ?

Maintenant que nous avons vu la théorie, passons à la pratique !
Vous allez créer un dépôt, y apporter quelques modifications et le publier en ligne. Nous verrons ensuite comment contribuer à un dépôt en ligne existant.

Git possède quelques commandes de base quotidiennes que nous allons voir maintenant, et de nombreuses commandes avancées que nous n'aborderons pas ici.
Vous pouvez toujours rechercher des commandes sur Internet, qu'elles soient basiques ou avancées.
Vous finirez par vous souvenir des principes de base après les avoir suffisamment utilisés, mais il n'y a aucune honte à chercher ce qu'il faut faire.

Nous utiliserons Git en ligne de commande pour ce tutoriel, car il fonctionne de la même manière partout.
Cependant, pour les tâches quotidiennes,
vous préférerez peut-être utiliser des interfaces graphiques telles que [GitKraken](https://www.gitkraken.com/), [GitHub Desktop](https://desktop.github.com/), ou le support Git de votre IDE favori.

Commencez par créer un dossier et _initialiser_ un dépôt dans ce dossier :

```sh
~$ mkdir exemple
~$ cd exemple
~/exemple$ git init
```

Git vous dira que vous avez initialisé un dépôt Git vide dans `~/example/.git/`.
Ce dossier `.git/` est un dossier spécial que Git utilise pour stocker les métadonnées. Il ne fait pas partie du dépôt lui-même, même s'il se trouve dans le dossier du dépôt.

Créez un fichier :

```sh
$ echo 'Hello' > hello.txt"
```

Nous pouvons maintenant demander à Git ce qu'il pense qu'il se passe :

```sh
$ git status
...
Fichiers non suivis :
        hello.txt
```

Git nous dit qu'il voit que nous avons ajouté `hello.txt`, mais ce fichier n'est pas encore suivi.
C'est-à-dire que Git ne l'inclura pas dans un commit à moins que nous ne le demandions explicitement. C'est exactement ce que nous allons faire :

```sh
$ git add -A
```

Cette commande demande à Git d'inclure toutes les modifications actuelles dans le dépôt lors du prochain commit.
Si nous apportons d'autres modifications, nous devrons demander que ces nouvelles modifications soient également suivies.
Mais pour l'instant, demandons à Git ce qu'il en pense :

```sh
$ git status
...
Changements à commit :
        nouveau fichier : hello.txt
```

Maintenant, Git sait que nous voulons inclure ce fichier dans un commit. Faisons donc exactement cela :

```sh
$ git commit
```

Cela ouvrira un éditeur de texte dans lequel vous pourrez saisir le message de validation. Comme nous l'avons vu précédemment, le message de validation doit être une description de la raison pour laquelle les changements ont été effectués.
Souvent, le tout premier commit d'un dépôt met en place la structure de base du fichier en tant que commit initial,
vous pourriez donc écrire `Commit initial mettant en place le fichier` ou quelque chose de similaire.
Vous obtiendrez alors un résultat comme celui-ci :

```sh
[...] Commit initial.
 1 fichier modifié, 1 insertion(+)
 create mode 100644 hello.txt
```

Git répète le message de commit que vous avez mis, ici `Commit initial.`,
et vous dit ensuite quels changements ont eu lieu. Ne vous inquiétez pas de ce `mode 100644`, c'est plus un détail d'implémentation.

Modifions maintenant les choses en ajoutant une ligne :

```sh
$ echo 'Goodbye' >> hello.txt
```

Nous pouvons demander à git les détails des changements que nous avons effectués :

```sh
$ git diff
```

Cela affichera une liste détaillée des différences entre l'état du dépôt à partir du dernier commit et l'état actuel du dépôt, c'est-à-dire que nous avons ajouté une ligne disant `Goodbye`.

Ajoutons les modifications que nous venons d'apporter :

```sh
$ git add -A
```

Que se passe-t-il si nous demandons à nouveau une liste de différences ?

```sh
$ git diff
```

...Rien ! Pourquoi ? Parce que `diff` montre par défaut les différences qui ne sont pas suivies pour le prochain commit.
Il existe trois états pour les modifications de fichiers dans Git : modifié, suivi ("staged") et committed.
Par défaut, les changements sont modifiés, puis avec `git add -A` ils sont suivis, et avec `git commit` ils sont validés.
Nous avons utilisé `-A` avec `git add` pour signifier "tous les changements",
mais nous pourrions en fait n'ajouter que des changements spécifiques, comme des fichiers spécifiques ou même des parties de fichiers.

Pour voir les changements suivis, nous devons les demander :

```sh
$ git diff --staged
```

Nous pouvons maintenant valider nos modifications.
Comme il s'agit d'un petit commit qui ne nécessite pas beaucoup d'explications, nous pouvons utiliser `-m` pour écrire le message de commit directement dans la commande :

```sh
$ git commit -m 'Say goodbye'
```

Essayons maintenant les branches, en créant une branche et en y basculant :

```sh
git switch -c feature/today
```

La barre oblique dans le nom de la branche n'a rien de spécial pour Git, il s'agit seulement d'une convention de nommage courante pour distinguer le but des différentes branches.
Par exemple, vous pouvez avoir des branches nommées `feature/delete-favorites` ou `bugfix/long-user-names`.
Mais vous pouvez aussi nommer votre branche `delete-favorites` ou `bugfix/long/user/names` si vous le souhaitez,
tant que tous ceux qui utilisent le dépôt se mettent d'accord sur une convention pour les noms.

Modifiez maintenant la seule ligne du fichier, en remplaçant par exemple "Hello" par "Hello today".
Ensuite, ajoutez vos modifications et validez-les :

```sh
$ git add -A && git commit -m 'Change greeting'
```

Vous remarquerez que Git vous dit qu'il y a `1 insertion (+), 1 suppression (-)`.
C'est un peu bizarre, nous avons changé une ligne, pourquoi y a-t-il deux changements ?
La raison en est que Git considère les modifications à la granularité des lignes.
Lorsque vous éditez une ligne, Git voit cela comme "vous avez supprimé la ligne qui était là, et vous avez ajouté une nouvelle ligne".
Le fait que les lignes "supprimées" et "ajoutées" soient similaires n'est pas pertinent.

Si vous avez déjà utilisé Git, vous avez peut-être entendu parler du `-a` de `git commit`, qui pourrait remplacer le `git add -A` explicite dans notre cas.
La raison pour laquelle nous ne l'utilisons pas ici, et la raison pour laquelle vous devriez être prudent si vous l'utilisez, est que `-a` ne fait qu'ajouter des changements à des fichiers existants.
Il n'ajoute pas de modifications aux nouveaux fichiers ou aux fichiers supprimés.
Il est donc très facile d'oublier accidentellement d'inclure certains fichiers nouveaux ou supprimés dans le commit,
et de devoir alors effectuer un autre commit avec ces seuls fichiers, ce qui est ennuyeux.

Quoi qu'il en soit, nous avons fait un commit sur notre branche `feature/today`.
Si nous voulons nous assurer que nous sommes bien sur cette branche, nous pouvons le demander à Git :

```sh
$ git branch
```

Cela produira une liste de branches, avec un astérisque `*` à côté de celle sur laquelle nous nous trouvons.

Passons maintenant à notre branche principale.
Selon votre version de Git, cette branche peut avoir des noms différents, donc regardez la sortie de la commande précédente et utilisez le bon, comme `master` ou `main` :

```sh
$ git switch main
```

Pour voir ce qui se passe lorsque deux commits entrent en conflit, apportons une modification à notre fichier `hello.txt` qui entre en conflit avec l'autre branche que nous venons de créer.
Par exemple, remplacez "Hello" par "Hello everyone".
Ensuite, suivez la modification et validez-la comme précédemment.

A ce stade, nous avons deux branches, notre branche principale et `feature/today`, qui ont divergé : elles ont toutes deux un commit qui n'est pas dans l'autre.
Demandons à Git de fusionner les branches, c'est-à-dire d'ajouter les commits de la branche spécifiée à la branche courante :

```sh
$ git merge feature/today
```

Git commencera de manière optimiste avec `Fusion automatique de hello.txt`, mais cela échouera rapidement avec un `Conflit de fusion dans hello.txt`.
Git nous demandera de corriger les conflits et de livrer le résultat manuellement.

A quoi ressemble `hello.txt` maintenant ?

```sh
$ cat hello.txt
<<<<<<< HEAD
Bonjour à tous
=======
Bonjour aujourd'hui
>>>>>>> feature/today
Au revoir
```

Prenons le temps de comprendre. La dernière ligne n'a pas changé, car elle ne fait pas partie du conflit.
La première ligne a été étendue pour inclure les deux versions : entre les `<<<` et `===` se trouve la version dans `HEAD`, c'est-à-dire la "tête", le dernier commit, dans la branche courante.
En effet, sur notre branche principale, la première ligne était "Bonjour à tous".
Entre le `===` et le `>>>` se trouve la version dans `feature/today`.
Ce que nous devons faire, c'est fusionner manuellement les changements, c'est-à-dire éditer le fichier pour remplacer le conflit comprenant les lignes `<<`, `===`, et `>>>` par les changements fusionnés que nous voulons.
Par exemple, nous pourrions nous retrouver avec un fichier contenant ce qui suit :

```sh
$ cat hello.txt
Bonjour à tous
Au revoir
```

C'est une façon de fusionner le fichier.
Nous aurions également pu choisir une seule des deux lignes.
Ou peut-être voulons-nous encore un autre changement, nous pourrions avoir `Hello hello` à la place. Git ne s'en préoccupe pas, il veut seulement que nous décidions quelle sera la version fusionnée.

Une fois que nous avons effectué nos modifications de fusion, nous devons ajouter les modifications et effectuer un commit comme précédemment :

```sh
$ git add -A && git commit -m 'Merge'
```

Très bien. Attendez, non, en fait, pas si bien que ça. C'est un message de commit assez mauvais. Il est beaucoup trop court et pas assez descriptif.
Heureusement, _parce que nous n'avons pas encore publié nos changements sur un autre clone du dépôt_, nous pouvons apporter des modifications à nos commits !
C'est comme la chute d'un arbre qui ne fait aucun bruit s'il n'y a personne pour l'entendre. Si personne ne l'entend, c'est qu'il ne s'est pas produit.
Nous pouvons modifier notre commit maintenant, et lorsque nous le pousserons vers un autre clone, ce dernier ne verra que notre commit modifié.
Cependant, si nous avions déjà poussé notre commit vers un clone, notre commit serait visible, nous ne pourrions donc plus le modifier car le clone serait confus par un commit changeant puisque les commits sont supposés être immuables.

Pour modifier notre commit, ce qui ne devrait être fait que si le commit n'a pas encore été poussé, nous le "modifions" :

```sh
$ git commit --amend -m 'Fusionner la branche feature/today'
```

Nous n'avons modifié ici que le message de commit, mais nous pourrions également modifier le contenu du commit, c'est-à-dire les modifications elles-mêmes.

Parfois, nous apportons des modifications que nous ne voulons pas vraiment, par exemple des modifications temporaires pendant que nous déboguons un code.
Effectuons un "mauvais" changement :

```sh
$ echo 'asdf' >> hello.txt
```

Nous pouvons restaurer le fichier dans l'état où il se trouvait lors du dernier commit afin d'annuler cette modification :

```sh
$ git restore hello.txt
```

C'est fait ! Nos modifications temporaires ont disparu.
Vous pouvez également utiliser `.` pour restaurer tous les fichiers du répertoire actuel, ou de tout autre chemin.
Cependant, gardez à l'esprit que "disparu" signifie réellement "disparu".
C'est comme si nous n'avions jamais modifié le fichier, puisqu'il est maintenant dans l'état où il se trouvait après le dernier commit.
N'utilisez pas `git restore` à moins que vous ne vouliez vraiment perdre vos changements.

Il arrive que nous ajoutions accidentellement des fichiers dont nous ne voulons pas. Il se peut qu'un script se soit détraqué ou que nous ayons copié des fichiers par accident.
Par exemple, si vous créez un fichier par erreur :

```sh
$ echo 'asdf' > mistake.txt
```

Nous pouvons demander à Git de "nettoyer" le dépôt, c'est-à-dire de supprimer tous les fichiers et répertoires non suivis.
Cependant, comme cela va supprimer des fichiers, nous ferions mieux de l'exécuter d'abord en mode "dry run" en utilisant `-n` :

```sh
$ git clean -fdn
```

Ceci affichera une liste de fichiers qui _seraient_ supprimés si nous n'avions pas inclus `-n`.
Si nous sommes d'accord avec la suppression proposée, faisons-la :

```sh
$ git clean -fd
```

Maintenant notre `mistake.txt` a disparu.

Enfin, avant de passer à GitHub, une dernière chose : gardez à l'esprit que Git ne suit que les _fichiers_, pas les _dossiers_.
Git ne garde trace des dossiers que s'ils font partie du chemin d'accès d'un fichier.

Ainsi, si nous créons un dossier et demandons à Git ce qu'il voit, il nous dira qu'il n'y a rien, car le dossier est vide :

```sh
$ mkdir folder
$ git status
```

Si vous avez besoin d'inclure un dossier "vide" dans un dépôt Git pour une raison quelconque, vous devez y ajouter un fichier vide afin que Git puisse suivre le dossier en tant que partie de ce fichier.

Publions maintenant notre dépôt. Allez sur [GitHub](https://github.com) et créez un dépôt en utilisant le bouton "New" sur la page d'accueil.
Vous pouvez le rendre public ou privé, mais ne créez pas de fichiers tels que des fichiers "Read Me" ou quoi que ce soit d'autre, juste un dépôt vide.

Ensuite, suivez les instructions de GitHub pour un dépôt existant à partir de la ligne de commande. Copiez et collez les commandes que GitHub vous donne.
Ces commandes ajouteront le dépôt GitHub nouvellement créé en tant que "remote" à votre dépôt local, c'est-à-dire un autre clone du dépôt que Git connaît.
Puisque ce sera le seul remote, ce sera aussi le remote par défaut. Le remote par défaut est traditionnellement nommé `origin`.
Les commandes fournies par GitHub pousseront également vos modifications vers ce serveur distant.
Une fois les commandes exécutées, vous pouvez rafraîchir la page de votre dépôt GitHub et voir vos fichiers.

Maintenant, faites un changement dans votre `hello.txt`, suivez le changement, et livrez-le.
Vous pouvez ensuite synchroniser le commit avec le clone du dépôt GitHub :

```sh
$ git push
```

Vous pouvez également récupérer les changements sur GitHub :

```sh
$ git pull
```

Cette commande n'a ici aucun effet, puisque personne d'autre n'utilise ce dépôt.
Dans un scénario réel, d'autres développeurs disposeraient également d'un clone du dépôt sur leur machine et utiliseraient GitHub comme leur serveur distant par défaut.
Ils apportaient leurs modifications et vous les récupéreriez.

Il est important de noter que `git pull` ne synchronise que la branche courante.
Si vous souhaitez synchroniser les commits d'une autre branche, vous devez d'abord `git switch` vers cette branche.

De même, `git push` ne synchronise que la branche courante, et si vous créez une nouvelle branche, vous devez lui indiquer où pousser avec `-u` en passant à la fois le nom distant et le nom de la branche :

```sh
$ git switch -c exemple
$ git push -u origin exemple
```

Publier votre dépôt en ligne est une bonne chose, mais il y a parfois des fichiers que vous ne voulez pas publier.
Par exemple, les fichiers binaires compilés à partir du code source dans le dépôt ne devraient probablement pas se trouver dans le dépôt, 
car ils peuvent être recréés facilement et ne feraient qu'occuper de l'espace.
Les fichiers contenant des données sensibles telles que des mots de passe ne doivent pas non plus se trouver dans le dépôt, surtout s'il est public.
Simulons un fichier sensible :

```sh
$ echo '1234' > password.txt
```

Nous pouvons dire à Git de faire comme si ce fichier n'existait pas en ajoutant une ligne avec son nom dans un fichier spécial appelé `.gitignore` :

```sh
$ echo 'password.txt' >> .gitignore
```

Maintenant, si vous essayez `git status`, il vous dira que `.gitignore` a été créé mais pas `password.txt` puisque vous avez dit à Git de l'ignorer.

Vous pouvez également ignorer des répertoires entiers.
Notez que cela ne fonctionne que pour les fichiers qui n'ont pas encore été livrés au dépôt.
Si vous avez déjà fait un commit dans lequel `password.txt` existe, ajouter son nom à `.gitignore` n'ignorera que les changements futurs, pas ceux passés.
Si vous poussez accidentellement sur un dépôt public un commit avec un fichier contenant un mot de passe, vous devez supposer que le mot de passe est compromis et le changer immédiatement.
Il existe des robots qui analysent GitHub à la recherche de mots de passe qui ont été accidentellement inclus dans un commit,
et ils trouveront votre mot de passe si vous le mettez dans un dépôt public, même pendant quelques secondes.

Maintenant que vous avez vu les bases de Git, il est temps de contribuer à un projet existant !
Vous le ferez par le biais d'une _pull request_, qui est une demande adressée aux responsables d'un projet existant pour qu'ils intègrent vos modifications dans leur projet.
Il s'agit d'un concept GitHub, car du point de vue de Git, il s'agit simplement de synchroniser les modifications entre les clones d'un dépôt.

Allez sur <https://github.com/sweng-example/hello> et cliquez sur le bouton "Fork".
Un _fork_ est un clone du dépôt sous votre propre nom d'utilisateur GitHub,
dont vous avez besoin ici parce que vous n'avez pas d'accès en écriture à `sweng-example/hello` et que vous ne pouvez donc pas y apporter de modifications.
Au lieu de cela, vous allez pousser les changements vers votre fork, sur lequel vous avez un accès en écriture,
et ensuite demander aux mainteneurs de `sweng-example/hello` d'accepter le changement.
Vous pouvez également créer des branches à l'intérieur d'un fork, car un fork est simplement un autre clone du dépôt.
En règle générale, si vous êtes un collaborateur d'un projet, vous utiliserez une branche dans le dépôt principal du projet, tandis que si vous êtes une personne extérieure souhaitant proposer une modification, vous créerez d'abord un fork.

Maintenant que vous avez une version forkée du projet sur GitHub, cliquez sur le bouton "Code" et copiez l'URL SSH, qui devrait commencer par `git@github.com:`.
Ensuite, demandez à Git de créer un clone local de votre fork, bien que vous deviez d'abord retourner dans votre répertoire d'origine, car la création d'un dépôt dans un dépôt pose des problèmes :

```sh
$ cd ~
$ git clone git@github.com :...
```

Git va cloner votre fork localement, ce qui vous permettra d'effectuer une modification, de la valider et de la pousser vers votre fork.
Une fois que c'est fait, si vous allez sur votre fork sur GitHub,
il devrait y avoir une bannière au-dessus du code vous indiquant que la branche de votre fork est en avance d'un commit par rapport à la branche principale du dépôt original.
Cliquez sur le bouton "Contribute" et sur le bouton "Open pull request" qui s'affiche, puis confirmez que vous voulez ouvrir une pull request, et écrivez une description pour celle-ci.

Félicitations, vous avez apporté votre première contribution à un projet open source !

La meilleure façon de s'habituer à Git est de l'utiliser souvent. Utilisez Git même pour vos propres projets, même si vous n'avez pas l'intention d'utiliser des branches.
Vous pouvez utiliser des dépôts privés sur GitHub comme sauvegardes, de sorte que même si votre ordinateur portable tombe en panne, vous ne perdrez pas votre code.

Il existe de nombreuses fonctionnalités avancées dans Git qui peuvent être utiles dans certains cas, comme `bisect`, `blame`, `cherry-pick`, `stash`, et bien d'autres.
Lisez la [documentation officielle](https://git-scm.com/docs/) ou trouvez des tutoriels avancés en ligne pour en savoir plus si vous êtes curieux !


## Comment écrire de bons messages de commit ?

Imaginez que vous soyez archéologue et que vous deviez comprendre ce qui s'est passé dans le passé en vous basant uniquement sur des dessins à moitié effacés, des fossiles et des traces.
Vous finirez par trouver ce qui a pu se produire pour provoquer tout cela, mais cela prendra du temps et vous ne saurez pas si votre supposition est correcte.
Ne serait-ce pas bien s'il existait à la place un journal que quelqu'un aurait rédigé, décrivant tout ce qu'il a fait d'important et pourquoi il l'a fait ?

C'est à cela que servent les messages de commit : garder une trace de ce que vous faites et de la raison pour laquelle vous l'avez fait,
afin que d'autres personnes le sachent même des années après.
Les messages de commit sont utiles aux personnes qui examinent votre code avant de l'approuver pour le fusionner dans la branche principale, 
ainsi qu'à vos collègues qui recherchent des bugs plusieurs mois après l'écriture du code.
Dans ce contexte, vos collègues incluent le "futur vous".
Même si les changements vous semblent "évidents" ou "clairs" au moment où vous les effectuez, quelques mois plus tard, vous ne vous souviendrez plus de la raison pour laquelle vous avez agi de la sorte.

Le format typique d'un message de validation est un résumé d'une ligne suivi d'une ligne vide et d'autant de lignes que nécessaire pour les détails. Par exemple, voici un bon message de commit :

```
Correction de l'ajout de favoris sur les petits téléphones

L'écran des favoris comportait trop de boutons empilés sur la même ligne.
Sur les téléphones à petit écran, il n'y avait pas assez d'espace pour les afficher tous,
et le bouton "ajouter" était hors de vue.

Cette modification ajoute une logique permettant d'utiliser plusieurs rangées de boutons si nécessaire.
```

Comme nous l'avons vu précédemment, l'écrasement des commits est une option lors de la fusion de votre code dans la branche principale,
de sorte que tous les commits d'une branche n'ont pas besoin d'avoir des messages aussi détaillés.
Parfois, un commit se résume à "Corriger une coquille" ou "Ajouter un commentaire selon le feedback des collègues". Ces modifications ne sont pas importantes pour comprendre les changements,
leurs messages seront donc supprimés une fois que la branche sera réduite à un seul commit lors de la fusion.

Le résumé d'une ligne est utile pour avoir une vue d'ensemble de l'histoire sans avoir à en voir tous les détails.
Vous pouvez le voir sur des dépôts en ligne tels que GitHub, mais aussi localement.
Git dispose d'une commande `log` pour afficher l'historique, et `git log --oneline` n'affichera que le résumé d'une ligne de chaque commit.

Un bon résumé doit être court et à l'impératif.
Par exemple :
- "Corriger le bug #145"
- "Ajouter une version HD du fond d'écran"
- "Supporter Unicode 14.0"

Les détails doivent décrire _ce que_ les changements font et _pourquoi_ vous les avez faits, mais pas _comment_.
Il est inutile de décrire comment, car le message de commit est associé au contenu du commit, et celui-ci décrit déjà la manière dont vous avez modifié le code.


## Comment éviter de fusionner du code bogué ?

La fusion de code bogué dans la branche principale d'un dépôt est une gêne pour tous les contributeurs de ce dépôt.
Ils devront corriger le code avant de faire le travail qu'ils veulent réellement faire, et ils ne le corrigeront peut-être pas tous de la même manière, ce qui entraînera des conflits.

Idéalement, nous n'accepterions les demandes de retrait que si le code résultant compile, est "propre" selon les normes de l'équipe et a été testé.
Chaque équipe a une idée différente de ce qu'est un code "propre", ainsi que de ce que signifie le terme "test", qui peut être manuel, automatisé, effectué sur une ou plusieurs machines, etc.

Lorsque l'on travaille dans un IDE, il existe généralement des options de menu permettant d'analyser le code
pour en vérifier la propreté, le compiler, l'exécuter et lancer des tests automatisés si les développeurs en ont écrit.
Cependant, tout le monde n'utilise pas le même IDE, ce qui signifie qu'ils peuvent avoir des définitions différentes de ce que ces opérations signifient.

Le principal problème lié à l'utilisation d'opérations dans un IDE pour vérifier les propriétés du code est que les humains font des erreurs.
Dans les projets de grande envergure, les erreurs humaines sont fréquentes.
Par exemple, il n'est pas raisonnable de s'attendre à ce que des centaines de développeurs n'oublient jamais, ne serait-ce qu'une fois, de vérifier que le code se compile et s'exécute.
Vérifier les erreurs de base est également une mauvaise utilisation du temps des gens.
L'examen du code devrait porter sur la logique du code, et non sur la validité syntaxique de chaque ligne, ce qui est du ressort du compilateur.

Nous aimerions plutôt _automatiser_ les étapes nécessaires à la vérification du code.
Cela se fait à l'aide d'un _système de build_, tel que CMake pour C++, MSBuild pour C#, ou Gradle pour Java.
Il existe de nombreux systèmes de build, dont certains prennent en charge plusieurs langues, mais ils offrent tous fondamentalement la même fonctionnalité : l'automatisation de tâches.
Un système de build peut invoquer le compilateur sur les bons fichiers avec les bons drapeaux pour compiler le code, et invoquer le binaire résultant pour exécuter le code,
et même effectuer des opérations plus complexes telles que le téléchargement de dépendances sur la base de leur nom si elles n'ont pas déjà été téléchargées.

Les systèmes de build sont configurés avec du code. Ils disposent généralement d'un langage déclaratif personnalisé intégré dans un autre langage tel que le XML.
Voici un exemple de code de construction pour MSBuild :
```xml
<Projet Sdk="Microsoft.NET.Sdk">
  <ItemGroup>
    <PackageReference Include="Microsoft.Z3" Version="4.10.2" />
  </ItemGroup>
</Projet>
```
Ce code indique à MSBuild que (1) il s'agit d'un projet .NET, qui est le runtime typiquement associé à C#, et (2) qu'il dépend de la librairie `Microsoft.Z3`, en particulier de sa version `4.10.2`.
On peut alors lancer MSBuild avec ce fichier à partir de la ligne de commande, et MSBuild compilera le projet après avoir téléchargé la librairie dont il dépend, si elle n'a pas déjà été téléchargée.
Dans ce cas, le nom de la librairie est associé à une librairie réelle en recherchant le nom sur [NuGet](https://www.nuget.org/), le catalogue de librairies associé à MSBuild.

Les systèmes de build suppriment la dépendance à l'égard d'un IDE pour la construction et l'exécution du code, ce qui signifie que chacun peut utiliser l'éditeur de son choix à condition d'utiliser le même système de build.
La plupart des IDE peuvent utiliser le code du système de build comme base pour leur propre configuration. Par exemple, le fichier ci-dessus peut être utilisé tel quel par Visual Studio pour configurer un projet.

Les systèmes de build permettent aux développeurs de construire, d'exécuter et de vérifier leur code n'importe où.
Mais il faut bien qu'il soit quelque part, alors quelle(s) machine(s) doivent-ils utiliser ?
Une fois de plus, l'utilisation de la machine spécifique d'un développeur n'est pas une bonne idée, car les développeurs personnalisent leur machine en fonction de leurs préférences personnelles.
Les machines utilisées par les développeurs peuvent ne pas être représentatives des machines sur lesquelles le logiciel fonctionnera réellement lorsqu'il sera utilisé par les clients.

De la même manière que nous avons défini les constructions à l'aide de code via un système de build, nous pouvons définir les environnements à l'aide de code !
Voici un exemple de code de définition de l'environnement pour le système de conteneurs Docker, que vous n'avez pas besoin de comprendre :
```
FROM node:12-alpine
RUN apk add python g++ make
COPY . .
RUN yarn install
CMD ["node", "src/index.js"]
EXPOSE 3000
```
Ce code indique à Docker d'utiliser l'environnement de base `node:12-alpine`, qui a Node.js préinstallé sur un environnement Linux Alpine.
Ensuite, Docker doit exécuter `apk add` pour installer des paquets spécifiques, y compris `make`, un système de build.
Docker doit alors copier le répertoire courant à l'intérieur du conteneur, et lancer `yarn install` pour invoquer le système de build `yarn` de Node.js afin de pré-installer les dépendances.
Le fichier indique également à Docker la commande à exécuter lors du démarrage de cet environnement et le port HTTP à exposer au monde extérieur.

La définition d'un environnement à l'aide de code permet aux développeurs d'exécuter et de tester leur code
dans des environnements spécifiques qui peuvent être personnalisés pour correspondre aux environnements des clients.
Les développeurs peuvent également définir des environnements multiples, par exemple pour s'assurer que leur logiciel
peut fonctionner sur différents systèmes d'exploitation, ou sur des systèmes d'exploitation dans différentes langues.

Nous avons utilisé le terme "machine" pour désigner l'environnement dans lequel le code s'exécute, mais dans la pratique,
il est peu probable qu'il s'agisse d'une machine physique, car cela serait inefficace et coûteux.
Les "pull requests" et les "pushes" sont assez rares étant donné que les ordinateurs modernes
peuvent effectuer des milliards d'opérations par seconde. Approvisionner une machine exclusivement pour un projet serait un gaspillage.

Au lieu de cela, les constructions automatisées utilisent des _machines virtuelles_ ou des _conteneurs_.
Une machine virtuelle est un programme qui émule une machine entière en son sein. Par exemple, il est possible d'exécuter une machine virtuelle Ubuntu sur Windows.
Du point de vue de Windows, la machine virtuelle n'est qu'un programme parmi d'autres.
Mais pour les programmes qui s'exécutent dans la machine virtuelle, c'est comme s'ils s'exécutaient sur du vrai matériel.
Cela permet de partitionner les ressources : une seule machine physique peut faire tourner plusieurs machines virtuelles,
surtout si ces dernières ne sont pas toutes occupées en même temps.
Il isole également les programmes s'exécutant dans la machine virtuelle, ce qui signifie que même s'ils tentent de casser le système d'exploitation,
le monde extérieur à la machine virtuelle n'est pas affecté.
Cependant, les machines virtuelles ont des frais généraux, en particulier lorsqu'elles sont nombreuses.
Même si 100 machines virtuelles exécutent toutes la même version de Windows, par exemple,
elles doivent toutes exécuter une instance distincte de Windows, y compris le noyau Windows.
C'est là qu'interviennent les _conteneurs_. Les conteneurs sont une forme légère de machines virtuelles qui partagent le noyau du système d'exploitation hôte au lieu d'inclure leur propre noyau.
Il y a donc moins de duplication des ressources, au prix d'un moindre isolement.
En règle générale, les services qui permettent à quiconque de télécharger du code utiliseront
des machines virtuelles pour l'isoler autant que possible, tandis que les services privés peuvent utiliser des conteneurs puisqu'ils font confiance au code qu'ils exécutent.

L'utilisation de systèmes de compilation et de machines virtuelles pour compiler,
exécuter et vérifier automatiquement le code chaque fois qu'un développeur apporte des modifications est appelée _intégration continue_,
et il s'agit d'une technique clé dans le développement des logiciels modernes.
Lorsqu'un développeur ouvre une demande d'extraction, l'intégration continue peut effectuer les vérifications configurées, par exemple tester que le code se compile et qu'il passe une analyse statique.
La fusion peut alors être bloquée si l'intégration continue ne réussit pas.
Ainsi, personne ne peut accidentellement fusionner du code cassé dans la branche principale,
et les développeurs qui examinent les demandes d'extraction n'ont pas besoin de vérifier manuellement que le code fonctionne.

Il est important de noter que la réussite ou l'échec d'une opération spécifique d'intégration continue signifie qu'il existe une machine sur laquelle le code réussit ou échoue.
Il est possible qu'un code fonctionne parfaitement sur la machine du développeur qui l'a écrit, mais qu'il échoue lors de l'intégration continue.
Une réponse courante est "mais ça marche sur ma machine !", mais cela n'a rien à voir.
L'objectif d'un logiciel n'est pas de fonctionner sur la machine du développeur, mais de fonctionner pour les utilisateurs.

Les problèmes liés à l'intégration continue proviennent généralement de différences entre les machines des développeurs et les machines virtuelles configurées pour l'intégration continue.
Par exemple, un développeur peut tester une application téléphonique sur son propre téléphone,
avec un scénario de test consistant à "ouvrir la page 'créer un article' et cliquer sur le bouton 'non'", ce qu'il peut faire sans problème.
Mais leur environnement d'intégration continue peut être configuré avec un émulateur de téléphone
doté d'un petit écran avec peu de pixels, et la façon dont l'application est écrite signifie que l'on ne peut pas l'utiliser.
le bouton "non" n'est pas visible :

<p align="center"><img alt="Illustration de l'exemple des téléphones." src="images/phones.svg" width="50%" /></p>.

Le code ne fonctionne donc pas dans l'environnement d'intégration continue, non pas à cause d'un problème d'intégration continue, mais parce que le code ne fonctionne pas sur certains téléphones.
Le développeur devrait corriger le code pour que le bouton "Non" soit toujours visible, éventuellement sous le bouton "Oui" avec une barre de défilement si nécessaire.

---

#### Exercice : Ajouter l'intégration continue
Retournez au dépôt GitHub que vous avez créé, et ajoutez l'intégration continue !
GitHub inclut un service d'intégration continue appelé GitHub Actions, qui est gratuit pour une utilisation de base.
Voici un fichier de base que vous pouvez utiliser, qui doit être nommé `.github/workflows/example.yml` :
```yaml
on: push
jobs:
  example:
    runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - run: echo "Hello!"
```
Après avoir ajouté ce fichier au dépôt GitHub et attendu quelques secondes, vous devriez voir un cercle jaune à côté du commit indiquant que votre action est en cours d'exécution,
que vous pouvez également voir dans l'onglet "Actions" du dépôt.
Il s'agit d'une action très basique qui se contente de cloner le dépôt et d'imprimer du texte. Dans un scénario réel, vous devriez au moins invoquer un système de build.
GitHub Actions est assez puissant, comme vous pouvez le lire sur [la documentation de GitHub Actions](https://docs.github.com/en/actions).

---

Le contrôle des versions, l'intégration continue et d'autres tâches de ce type étaient généralement appelés "opérations" et étaient effectués par une équipe distincte de l'équipe de "développement".
Cependant, de nos jours, ces concepts se sont combinés en "DevOps", dans lequel la même équipe fait les deux,
ce qui permet aux développeurs de configurer plus facilement exactement les opérations qu'ils souhaitent.


## Résumé

Dans ce cours, vous avez appris :
- Les systèmes de gestion de version et les différences entre la première, la deuxième et la troisième génération.
- Git : comment l'utiliser pour des scénarios de base, et comment écrire de bons messages de commit.
- Intégration continue : systèmes de build, machines virtuelles et conteneurs.

Vous pouvez maintenant consulter les [exercices](exercices/) !
