# Debugging

> **Prérequis** : Vous êtes _fortement_ encouragé, mais pas strictement obligé, d'utiliser un IDE pour les exercices sur le debugging dans cette conférence.
> Vous pouvez également utiliser le debugger en ligne de commande intégré à Java, `jdb`, mais il est beaucoup moins pratique qu'une interface utilisateur graphique.

L'écriture du code n'est qu'une partie du génie logiciel ; vous passerez souvent plus de temps à _lire_ du code qu'à en écrire.
Il peut s'agir de comprendre un morceau de code afin de pouvoir l'étendre, ou de "debugger" un code existant en trouvant et en corrigeant les bugs.
Ces tâches sont beaucoup plus faciles si vous écrivez votre code en tenant compte de la lisibilité et de la debuggabilité, et si vous savez comment utiliser les outils de debugging.


## Objectifs

Après ce cours, vous devriez être en mesure de :

- Développer un code _lisible
- Utiliser un _debugger_ pour comprendre et debugger le code
- Isoler la _cause première_ d'un bug
- Développer du code _débuggable_


## Qu'est-ce qui rend le code lisible ?

Jetez un coup d'œil à [planets.py](exercices/cours/planets.py) dans le dossier d'exercices de la leçon.
Le trouvez-vous facile à lire et à comprendre ? Probablement pas.
Avez-vous remarqué que le tri ne fonctionne pas parce que le code utilise une fonction qui renvoie la liste triée, mais n'utilise pas sa valeur de retour, plutôt qu'un tri sur place ?
Il est beaucoup plus difficile de repérer ce bug lorsqu'il faut faire appel à toute sa puissance cérébrale pour lire le code.
(Vous pouvez consulter plus de problèmes concrets [dans la solution](exercices/solutions/cours/planets.md))

Malheureusement, le code difficile à lire ne se trouve pas uniquement dans les exercices des notes de cours.
Prenons l'exemple suivant, extrait du cadre ScalaTest :

```scala
package org.scalatest.tools;

objet Runner {
  def doRunRunDaDoRunRun(...) : Unit
}
```

Que fait cette méthode ? Le nom de la méthode ne vous aidera pas. Il s'agit d'une référence à [une chanson de 1963](https://en.wikipedia.org/wiki/Da_Doo_Ron_Ron).
Bien sûr, c'est une référence amusante, mais ne préféreriez-vous pas lire un nom qui vous explique ce que fait la méthode ?
Pire, [la méthode comporte 21 paramètres](https://github.com/scalatest/scalatest/blob/282da2aff8f439906fe5e7d9c3112c84019545e7/jvm/core/src/main/scala/org/scalatest/tools/Runner.scala#L1044-L1066).
Vous pouvez bien sûr comprendre ce que fait la méthode si vous y consacrez suffisamment de temps, mais est-ce nécessaire ?

Parlons de cinq composantes de la lisibilité du code : le nom, la documentation, les commentaires, la mise en forme et la cohérence.

### Noms

Tout d'abord, un exemple de _nommage_ sans même utiliser de code : les erreurs de mesure.
Si vous mesurez la présence de quelque chose qui est absent, il s'agit d'une erreur de type I.
Si vous mesurez l'absence de quelque chose qui est présent, il s'agit d'une erreur de type II.
Ce type d'erreurs se produit constamment, par exemple dans les tests de détection de virus.
Cependant, il est facile d'oublier quel est le type `I` et quel est le type `II`.
Et même si vous vous en souvenez, une faute de frappe dupliquant un caractère peut complètement changer le sens d'une phrase.
A la place, vous pouvez utiliser `faux positif` et `faux négatif`.
Ces noms sont plus faciles à comprendre, plus faciles à retenir et plus résistants aux fautes d'orthographe.

Les noms dans le code peuvent également faire la différence entre un code facile à comprendre et un code difficile à analyser mentalement.
Une variable nommée `isUserOnline` en Java est très bien... tant qu'il s'agit d'une variable booléenne "l'utilisateur est-il en ligne". S'il s'agit d'un nombre entier, c'est beaucoup plus confus.
Et si vous écrivez Python à la place, c'est aussi un problème puisque Python utilise des soulignés pour séparer les mots, alias "snake case", donc cela devrait être `is_user_online`.
Une variable nommée `can_overwrite_the_data` est un nom assez long, ce qui n'est pas un problème en soi, mais est redondant : bien sûr que nous écrasons des "données", le nom est trop vague.

Les noms ne concernent pas uniquement les noms de variables, de méthodes ou de classes. Considérons l'appel de méthode suivant :

```java
split("abc", "a", true, true)
```

Que fait cette méthode ? Bonne question. Que se passerait-il si l'appel ressemblait plutôt à ceci, avec des constantes ou des enums ?

```java
split("abc", "a",
      SplitOptions.REMOVE_EMPTY_ENTRIES,
      CaseOptions.IGNORE_CASE)            
```

Il s'agit du même appel de méthode, mais nous avons donné des noms au lieu de valeurs, et la signification est maintenant plus claire.
Ces constantes ne sont cependant qu'une solution de contournement à l'absence de paramètres nommés en Java. En Scala, et dans d'autres langages comme le C#, vous pourriez appeler la méthode comme suit :

```scala
split("abc",
      separator = "a",
      removeEmptyEntries = true,
      ignoreCase = true)     
```

Le code est maintenant beaucoup plus lisible grâce aux noms explicites, sans avoir à écrire du code supplémentaire.

La _notation hongroise_ est un exemple de bonne volonté en matière de nommage.
Charles Simonyi, un ingénieur hongrois de Microsoft, a eu la bonne idée de commencer les noms de ses variables par le type de données précis qu'elles contenaient,
par exemple `xPosition` pour une position sur l'axe des X,
ou `cmDistance` pour une distance en centimètres.
Cela signifie que n'importe qui pouvait facilement repérer l'erreur dans une formule telle que `distanceTotal += speedLeft / timeLeft`, puisque diviser la vitesse par le temps ne donne pas une distance.
C'est ce qu'on a appelé la "notation hongroise", car dans la Hongrie natale de Simonyi, les noms s'écrivent avec le nom de famille en premier, par exemple "Simonyi Károly".
Malheureusement, un autre groupe au sein de Microsoft n'a pas bien compris l'objectif de Simonyi et a plutôt pensé qu'il s'agissait du type de variable.
Ils ont donc écrit des noms de variables tels que `cValue` pour une variable `char`, `lIndex` pour un index `long`, et ainsi de suite,
ce qui rend les noms plus difficiles à lire sans ajouter plus d'informations que celles déjà présentes dans le type.
On l'a appelé "Systems Hungarian", parce que le groupe faisait partie de la division des systèmes d'exploitation, et malheureusement,
cette notation a fait son chemin dans les API Windows "Win32",
qui étaient les principales API de Windows jusqu'à récemment. De nombreuses API Windows ont reçu des noms difficiles à lire à cause d'un malentendu !
Une fois de plus, le nommage n'est pas le seul moyen de résoudre ce problème, mais seulement l'un d'entre eux. Dans le langage de programmation F#,
vous pouvez déclarer des variables avec des unités, comme `let distance = 30<cm>`,
et le compilateur vérifiera que les comparaisons et les calculs ont un sens compte tenu des unités.

---
#### Exercice
Les noms suivants semblent tous assez raisonnables, pourquoi sont-ils médiocres ?
- `pickle` (en Python)
- `binhex` (en Python)
- `LinkedList<E>` (dans `java.util` de Java)
- `vector<T>` (dans `std` de C++)
- `SortedList` (dans `System.Collections` en C#)
<details>
<summary>Réponses (cliquez pour développer)</summary>
<p>

`pickling` est une façon plutôt étrange de se référer à la sérialisation et à la désérialisation des données pour les "préserver".

`binhex` semble être le nom de quelques utilitaires binaires et hexadécimaux, mais il s'agit en fait d'un module qui gère un ancien format Mac.

Une liste chaînée et une liste doublement chaînée ne sont pas la même chose, mais Java nomme la seconde comme s'il s'agissait de la première.

Un vecteur a une signification spécifique en mathématiques ; le vecteur de C++ est en fait un tableau redimensionnable.

`SortedList` est un nom acceptable pour une classe de liste triée. Mais la classe portant ce nom est un tableau associatif ("map") !

</p>
</details>

---


Dans l'ensemble, les noms sont un outil permettant de rendre le code clair et succinct, ainsi que cohérent avec d'autres bouts de code, de sorte que les lecteurs n'aient pas à penser explicitement aux noms.

### Documentation

La _documentation_ est un outil permettant d'expliquer _ce que fait_ un morceau de code.

La documentation est le principal moyen pour les développeurs d'en savoir plus sur le code qu'ils utilisent.
Lorsqu'ils écrivent du code, les développeurs consultent les commentaires de la documentation, généralement dans un IDE sous forme d'infobulles.
Les commentaires de la documentation doivent donc décrire succinctement ce que fait une classe ou une méthode,
y compris les informations dont les développeurs sont susceptibles d'avoir besoin, comme le fait de savoir si elle lève des exceptions,
ou s'il exige que ses entrées soient dans un format spécifique.

### Commentaires

Les commentaires sont un outil qui permet de savoir pourquoi un morceau de code fait ce qu'il fait.
Il est important de noter que les commentaires ne doivent pas indiquer _comment_ un morceau de code fait ce qu'il fait, car cette information existe déjà dans le code lui-même.

Malheureusement, tous le code ne se documente pas lui-même.
Les commentaires sont un moyen d'expliquer un code délicat.
Parfois, le code doit être écrit d'une manière qui semble excessivement compliquée ou erronée parce que le code contourne un problème dans son environnement, tel qu'un bug dans une bibliothèque,
ou un compilateur qui ne produit un code assembleur rapide que dans des conditions spécifiques.

Voici un bon exemple de commentaire, tiré d'une ancienne version de la bibliothèque `libjsound` du kit de développement Java :

```c
/* Solution de contournement : L'application 32bit sur linux 64bit obtient un échec d'assertion en essayant d'ouvrir des ports.
   Jusqu'à ce que le problème soit corrigé dans ALSA (bug 4807), signalons l'absence de périphériques midi dans la configuration. */
if (jre32onlinux64) { return 0 ; }
```

Il s'agit d'un excellent exemple de commentaire : il explique quel est le problème externe, quelle est la solution choisie et renvoie à un identifiant pour le problème externe.
De cette manière, un futur développeur peut rechercher ce bug dans ALSA, un système audio Linux,
et vérifier s'il a été corrigé entre-temps, de sorte que le code qui contourne le bug puisse être supprimé.

Les commentaires sont un moyen d'expliquer le code au-delà de ce que le code lui-même peut faire, ce qui est souvent nécessaire même si, dans l'idéal, cela ne devrait pas l'être.
Cette explication peut être destinée aux personnes qui examineront votre code avant d'accepter les modifications que vous proposez,
ou aux collègues qui liront votre code lorsqu'ils travailleront sur la base de code des mois plus tard.
N'oubliez pas que l'un de ces "collègues" est probablement "vous-même dans le futur".
Même si vous pensez qu'un morceau de code est clair à l'heure actuelle, vous serez reconnaissant à l'avenir des commentaires qui expliquent les parties non évidentes.

### Formatage

Le formatage du code a pour but de faciliter la lecture du code. On ne remarque pas un bon formatage, mais on remarque un mauvais formatage, et il est plus difficile de se concentrer.

Voici un exemple concret de mauvais formatage :

```c
if (!update(&context, &params))
  goto fail;
  goto fail; 
```

Avez-vous repéré le problème ? Le code donne l'impression que le deuxième `goto` est redondant, parce qu'il est formaté de cette façon.
Mais c'est du C. Le second `goto` est en fait en dehors de la portée du `if`, et est donc toujours exécuté.
Il s'agit d'un véritable bug qui a déclenché [une vulnérabilité](https://nakedsecurity.sophos.com/2014/02/24/anatomy-of-a-goto-fail-apples-ssl-bug-explained-plus-an-unofficial-patch/) dans les produits Apple.

Certains langages imposent au moins une certaine cohérence de formatage, comme Python et F#.
Mais comme vous l'avez vu avec l'exercice `planets.py` plus tôt, cela ne signifie pas qu'il est impossible de mal formater son code.

### Cohérence

Devriez-vous utiliser `camelCase` ou `snake_case` pour vos noms ? 4 ou 8 espaces pour l'indentation ? Ou peut-être des tabulations ? Autant de questions.

C'est à cela que servent les _conventions_. Toute l'équipe décide, une fois pour toutes, de ce qu'il faut faire.
Chaque membre de l'équipe accepte alors les décisions et bénéficie d'un style de code cohérent sans avoir à y penser explicitement.

Lors du choix d'une convention, il faut se méfier d'un problème courant appelé "bikeshedding" en anglais, venant du mot pour un abri à vélos.
Le nom vient de l'histoire qui l'illustre : une réunion du conseil municipal a deux points à l'ordre du jour, l'entretien d'une centrale nucléaire et la construction d'un abri à vélos.
Le conseil approuve rapidement la maintenance nucléaire, qui est très coûteuse, car tous conviennent que cette maintenance est nécessaire pour continuer à fournir de l'électricité à la ville.
Ensuite, le conseil passe une heure à discuter des plans de l'abri à vélos, qui est très bon marché.
N'est-il pas encore trop cher ? Il est certainement possible de réduire un peu le coût, un abri à vélos devrait être encore moins cher.
Doit-il être bleu ou rouge ? Ou peut-être gris ? Combien de vélos doit-il contenir ?
Il est facile de passer beaucoup de temps sur de petites décisions qui, en fin de compte, n'ont pas beaucoup d'importance, parce qu'il est facile de se concentrer sur elles.
Mais ce temps devrait être consacré à des décisions plus importantes qui ont plus d'impact, même si elles sont plus difficiles à discuter.

Une fois que vous vous êtes mis d'accord sur une convention, vous devez utiliser des outils pour la faire respecter, et non des efforts manuels.
Il existe des outils en ligne de commande, tels que `clang-format` pour le code C, ainsi que des outils intégrés aux IDE,
qui peuvent être configurés pour s'exécuter à chaque fois que vous enregistrez un fichier.
Ainsi, vous n'avez plus à réfléchir aux préférences de l'équipe, les outils le font pour vous.


## Comment peut-on debugger efficacement un programme ?

Votre programme vient de recevoir un rapport de bug de la part d'un utilisateur : quelque chose ne fonctionne pas comme prévu. Que se passe-t-il alors ?
La présence d'un bug implique que le comportement du code ne correspond pas à l'intention de la personne qui l'a écrit.

Le but du _debugging_ est de trouver et de corriger la _cause première_ du bug, c'est-à-dire le problème dans le code qui est à l'origine du bug.
Il s'agit d'une différence par rapport aux _symptômes_ de l'insecte, de la même manière que les symptômes d'une maladie telle que la perte d'odorat sont différents d'une cause profonde telle qu'un virus.

Vous trouverez la cause première en posant à plusieurs reprises la question "pourquoi ?" lorsque vous observez des symptômes, jusqu'à ce que vous atteigniez la cause première.
Par exemple, disons que vous avez un problème : vous êtes arrivé en retard en classe.
Pourquoi ? Parce que vous vous êtes réveillé tard.
Pourquoi ? Parce que votre alarme n'a pas sonné.
Pourquoi ? Parce que votre téléphone n'avait plus de batterie.
Pourquoi ? Parce que vous avez oublié de brancher votre téléphone avant de vous coucher.
Voilà la cause du problème. Si vous vous étiez arrêté à, disons, "votre alarme n'a pas sonné",
et que vous aviez essayé de résoudre le problème en ajoutant un deuxième téléphone avec une alarme, vous auriez simplement eu deux alarmes qui n'auraient pas sonné,
car vous oublieriez de brancher également le deuxième téléphone.
Mais maintenant que vous savez que vous avez oublié de brancher votre téléphone, vous pouvez vous attaquer à la cause première,
par exemple en plaçant un post-it au-dessus de votre lit pour vous rappeler de charger votre téléphone.
En théorie, on peut continuer à demander "pourquoi ?", mais cela ne sert plus à rien au bout de quelques fois.
Dans cet exemple, la "vraie" cause profonde est peut-être que vous oubliez souvent des choses, mais vous ne pouvez pas y remédier facilement.

À un niveau élevé, le debugging comporte trois étapes : reproduire le bug, l'isoler, et le debugger.

Reproduire le bug signifie trouver les conditions dans lesquelles il apparaît :
- Quel environnement ?
  Est-ce sur des systèmes d'exploitation spécifiques ? À des heures précises de la journée ? Dans des langues spécifiques ?
- Quelles sont les mesures à prendre pour découvrir le bug ?
  Il peut s'agir d'une situation aussi simple que "ouvrir le programme, cliquer sur le bouton 'login', le programme se bloque", ou d'une situation plus complexe, telle que la création de
  plusieurs utilisateurs ayant des propriétés spécifiques et effectuant ensuite une séquence de tâches qui déclenchent un bug.
- Quel est le résultat attendu ? En d'autres termes, que devrait-il se passer s'il n'y avait pas de bug ?
- Quel est le résultat réel ? Il peut s'agir simplement d'un "plantage", ou de quelque chose de plus complexe,
  comme "les résultats de la recherche sont vides alors que la base de données contient un élément correspondant à la recherche"
- Pouvez-vous reproduire le bug à l'aide d'un test automatisé ? Cela permet de vérifier plus facilement et avec moins d'erreurs si vous avez corrigé le bug ou non.

Isoler le bug signifie trouver approximativement l'origine du bug.
Par exemple, si vous désactivez certains modules de votre programme en commentant le code qui les utilise, le bug apparaît-il toujours ?
Pouvez-vous déterminer quels modules sont nécessaires pour déclencher le bug ?
Vous pouvez également isoler en utilisant le contrôle de version : le bug existe-t-il dans un commit précédent ?
Si c'est le cas, qu'en est-il d'un commit encore plus ancien ? Pouvez-vous trouver le commit qui a introduit le bug ?
Si vous pouvez trouver le commit qui a introduit le bug, et que ce commit est suffisamment petit, vous avez considérablement réduit la quantité de code que vous devez examiner.

Enfin, une fois que vous avez reproduit et isolé le bug, il est temps de le debugger : voir ce qui se passe et comprendre pourquoi.
Vous pouvez le faire à l'aide d'instructions d'impression :
```c
printf("size : %u, capacity : %u\n", size, capacity);
```
Cependant, les instructions d'impression ne sont pas pratiques.
Vous devez écrire potentiellement beaucoup d'instructions, surtout si vous voulez voir les valeurs d'une structure de données ou d'un objet.
Il se peut même que vous ne puissiez pas voir les valeurs d'un objet s'il s'agit de membres privés,
auquel cas vous devez ajouter une méthode à l'objet uniquement pour imprimer certains de ses membres privés.
Vous devez également supprimer manuellement ces instructions après avoir corrigé le bug.
En outre, si vous vous rendez compte pendant l'exécution du programme que vous avez oublié d'imprimer une valeur spécifique,
l'utilisation d'impressions vous oblige à arrêter le programme, à ajouter une impression et à l'exécuter à nouveau, ce qui est lent.

Au lieu d'utiliser des instructions d'impression, utilisez un outil conçu pour le debugging : un debugger !

### Debugger

Un debugger est un outil, généralement intégré à un IDE, qui vous permet d'interrompre l'exécution d'un programme où vous le souhaitez, d'inspecter l'état du programme et même de le modifier,
et, d'une manière générale, de voir ce que fait réellement un morceau de code sans avoir à le modifier.

Une remarque sur les debuggers et les outils en général : certaines personnes pensent que le fait de ne pas utiliser un outil et de faire les choses "à la dure" les rendent meilleurs ingénieurs.
C'est complètement faux, c'est l'inverse : connaître les outils disponibles et les utiliser correctement est essentiel pour être un bon ingénieur.
Tout comme vous ignorez les personnes qui vous disent de ne pas prendre une lampe de poche et une bouteille d'eau lorsque vous partez en randonnée dans une grotte, ignorez les personnes qui vous disent de ne pas utiliser un debugger ou tout autre outil que vous jugez utile.

Les debuggers fonctionnent également pour les logiciels qui s'exécutent sur d'autres machines, comme un serveur, à condition que vous puissiez y lancer un outil de debugging, vous pouvez exécuter le debugger graphique sur votre machine pour debugger un programme sur une machine distante.
Il existe également des debuggers en ligne de commande, tels que `jdb` pour Java ou `pdb` pour Python, bien qu'ils ne soient pas aussi pratiques car vous devez entrer manuellement des commandes pour, par exemple, voir quelles sont les valeurs des variables.

Le seul prérequis des debuggers est un fichier contenant des _symboles de debugging_ : le lien entre le code source et le code compilé.
En d'autres termes, lorsque le programme exécute une ligne spécifique de code assembleur, de quelle ligne s'agit-il dans le code source ?
Quelles variables existent à ce moment-là et dans quels registres du CPU se trouvent-elles ?
Cela n'est bien sûr pas nécessaire pour les langages interprétés tels que Python, pour lesquels vous disposez de toute façon du code source.
Il est techniquement possible d'utiliser un debugger sans symboles de debugging, mais il faut alors comprendre soi-même comment les détails de bas niveau correspondent aux concepts de haut niveau, ce qui est fastidieux.

Examinons cinq questions clés que vous pouvez vous poser pendant le debugging et comment vous pouvez y répondre à l'aide d'un debugger.

_Le programme atteint-il cette ligne ?_
Vous vous demandez peut-être si le bug se déclenche lors de l'exécution d'une ligne de code particulière.
Pour répondre à cette question, utilisez un _point d'arrêt_ ("breakpoint"),
ce que vous pouvez généralement faire en cliquant avec le bouton droit de la souris sur une ligne et en sélectionnant "ajouter un point d'arrêt" dans le menu contextuel.
Une fois que vous avez ajouté un point d'arrêt, exécutez le programme en mode debugging et l'exécution s'interrompra lorsque cette ligne sera atteinte.
Les debuggers permettent généralement de définir des points d'arrêt plus avancés, tels que "ne s'arrêter que si une certaine condition est remplie"
ou "s'arrêter une fois toutes les N fois que cette ligne est exécutée".

Vous pouvez même utiliser des points d'arrêt pour imprimer des choses au lieu de mettre l'exécution en pause.
Attendez, ne venons-nous pas de dire que les impressions n'étaient pas une bonne idée ?
La raison pour laquelle l'impression des points d'arrêt est préférable est que vous n'avez pas besoin de modifier le code, et donc pas besoin de revenir sur ces modifications plus tard,
et vous pouvez changer ce qui est imprimé et où pendant que le programme est en cours d'exécution.

_Quelle est la valeur de cette variable ?_
Vous avez ajouté un point d'arrêt, le programme s'y est rendu et a interrompu l'exécution.
Dans un IDE, vous pouvez généralement passer votre souris sur une variable du code source pour voir sa valeur lorsque le programme est en pause,
ainsi que pour afficher une liste de toutes les variables locales.
Il s'agit notamment des valeurs contenues dans les structures de données telles que les tableaux et les membres privés des classes.
Vous pouvez également exécuter du code pour poser des questions, comme `n % 12 == 0` pour voir si `n` est actuellement un multiple de 12,
ou `IsPrime(n)` si vous avez une méthode `IsPrime` et que vous voulez voir ce qu'elle retourne pour `n`.

_Et si ... ?_
Vous constatez qu'une variable a une valeur à laquelle vous ne vous attendiez pas et vous vous demandez si le bug disparaîtrait si elle avait une valeur différente.
Bonne nouvelle : vous pouvez essayer exactement cela. Les debuggers ont généralement une sorte de fenêtre de "commande"
où vous pouvez écrire des lignes telles que `n = 0` pour changer la valeur de `n`, ou `lst.add("x")` pour ajouter `"x"` à la liste `lst`.

_Qu'est-ce qui va se passer ensuite ?_
L'état du programme semble correct, mais c'est peut-être la ligne suivante qui pose problème.
Les commandes d'exécution pas à pas ("step") vous permettent d'exécuter le programme étape par étape, de sorte que vous pouvez examiner
l'état du programme après l'exécution de chaque étape pour voir si quelque chose ne va pas.
Les debuggers fournissent typiquement une option pour entrer dans n'importe quelle méthode appelée, une pour passer à la ligne suivante au lieu d'entrer dans une méthode,
et une pour finir l'exécution de la méthode en cours.
Certains debuggers disposent d'outils supplémentaires, tels qu'une exécution pas à pas "intelligente" qui ne rentre que dans les méthodes de plus de quelques lignes.
En fonction du langage de programmation et du debugger, vous pouvez même changer le pointeur d'instruction pour la ligne de code de votre choix et modifier du code à la volée sans avoir à interrompre l'exécution du programme.

Notez que vous n'êtes pas obligé d'utiliser la souris pour lancer le programme et l'exécuter pas à pas : les debuggers disposent généralement de raccourcis clavier, tels que F5 pour lancer, F9 pour exécuter pas à pas, etc. et vous pouvez généralement les personnaliser.
Ainsi, votre flux de travail consistera à appuyer sur une touche pour exécuter, à regarder l'état du programme après l'atteinte du point d'arrêt, puis à appuyer sur une touche pour avancer, à regarder l'état du programme, à avancer à nouveau, et ainsi de suite.

_Comment sommes-nous arrivés ici ?_
Vous avez placé un point d'arrêt dans une méthode, le programme l'a atteint et a interrompu l'exécution, mais comment le programme a-t-il atteint cette ligne ?
La _pile d'appel_ est là pour répondre à cette question : vous pouvez voir quelle méthode vous a appelé, quelle méthode a appelé celle-ci, et ainsi de suite.
De plus, vous pouvez voir l'état du programme au moment de cet appel. Par exemple, vous pouvez voir quelles valeurs ont été données comme arguments à la méthode qui a appelé la méthode qui a appelé la méthode dans laquelle vous vous trouvez actuellement.

_Qu'est-ce qui s'est passé pour provoquer un crash ?_
Ne serait-il pas agréable de pouvoir voir l'état du programme au moment où un crash s'est produit sur la machine d'un utilisateur ?
Eh bien, c'est possible ! Le système d'exploitation peut générer un _crash dump_ qui contient l'état du programme lorsqu'il se plante, et vous pouvez charger ce crash dump dans un debugger,
ainsi que le code source du programme et les symboles de debugging, pour voir quel était l'état du programme. C'est ce qui se passe lorsque vous cliquez sur "Signaler le problème à Microsoft" après le plantage de votre document Word.
Notez que cela ne fonctionne que pour les plantages, et non pour les bugs du type "le comportement n'est pas celui auquel je m'attendais", car il n'existe aucun moyen automatisé de détecter ce type de comportement inattendu.


### Le debugging en pratique

Lorsque vous utilisez un debugger pour trouver la cause première d'un bug, vous ajoutez un point d'arrêt,
exécutez le programme jusqu'à ce que l'exécution s'interrompe pour inspecter l'état, et apportez éventuellement des modifications au programme en fonction de vos observations,
puis répétez le cycle jusqu'à ce que vous ayez trouvé la cause première.

Cependant, il arrive que vous ne puissiez pas résoudre le problème tout seul et que vous ayez besoin d'aide.
C'est tout à fait normal, surtout si vous débugz un code écrit par quelqu'un d'autre.
Dans ce cas, vous pouvez demander de l'aide à un collègue, voire poster sur un forum tel que [StackOverflow](https://stackoverflow.com).
Venez préparés, afin de pouvoir aider les autres à vous aider. Quels sont les symptômes ? Avez-vous un moyen facile de reproduire le bug ? Qu'avez-vous essayé ?

Parfois, vous commencez à expliquer votre problème à un collègue et, au cours de votre explication, une ampoule s'allume dans votre tête : voilà le problème !
Votre collègue vous regarde alors, heureux que vous ayez trouvé la solution, mais un peu agacé d'être interrompu.
Pour éviter cette situation, commencez par la technique du "_rubber ducking_" (de l'anglais "rubber duck", canard en caoutchouc) :
expliquez votre problème à un canard en caoutchouc, ou à tout autre objet inanimé.
Parlez à l'objet comme s'il s'agissait d'une personne, en expliquant votre problème.
La raison pour laquelle cela fonctionne est que lorsque nous expliquons un problème à quelqu'un d'autre,
nous expliquons généralement ce qui se passe réellement, plutôt que ce que nous souhaiterions qu'il se passe.
Si vous ne comprenez pas le problème en l'expliquant à un canard, vous aurez au moins répété comment vous expliquerez le bug, et vous serez en mesure de mieux l'expliquer à un humain.

Il n'y a qu'une seule façon de s'améliorer en matière de debugging : s'entraîner. La prochaine fois que vous rencontrerez un bug, utilisez un debugger.
Les premières fois, vous serez peut-être plus lent que si vous n'en aviez pas, mais ensuite votre productivité montera en flèche.

---
#### Exercice
Exécutez le code dans le dossier [binary-tree](exercices/cours/binary-tree).
Tout d'abord, lancez-le. Il se plante ! Utilisez un debugger pour ajouter des points d'arrêt et examiner ce qui se passe jusqu'à ce que vous en trouviez la cause et que vous corrigiez les bugs.
Notez que le plantage n'est pas le seul bug.

<details>
<summary>Solution (cliquer pour développer)</summary>
<p>

Tout d'abord, il n'y a pas de cas de base pour la méthode récursive qui construit un arbre, vous devez donc en ajouter un pour gérer le cas `list.size() == 0`.

Deuxièmement, les limites des sous-listes ne sont pas correctes : elles devraient être `0..mid` et `mid+1..list.size()`.

Il y a un bug de correction : le constructeur utilise `l` deux fois, alors qu'il devrait mettre `right` à `r`. Cela ne se serait pas produit si le code avait utilisé de meilleurs noms !

Nous fournissons une [version corrigée](exercices/solutions/cours/BinaryTree.java).

</p>
</details>


## Qu'est-ce qui rend un code débogable ?

L'inventeur [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) a dit un jour à propos d'une de ses machines
"_A deux reprises, on m'a demandé : Monsieur Babbage, si vous introduisez de mauvais chiffres dans la machine, les bonnes réponses en sortiront-elles ?_
_Je ne suis pas en mesure d'appréhender correctement le genre de confusion d'idées qui pourrait provoquer une telle question._"

Il devrait être clair qu'une entrée erronée ne peut pas conduire à une sortie correcte.
Malheureusement, il arrive souvent qu'une entrée erronée conduise à une sortie erronée _silencieusement_ : il n'y a aucune indication que quelque chose d'erroné s'est produit.
Il est donc difficile de trouver la cause première d'un bug.
Si vous remarquez que quelque chose ne va pas, est-ce que c'est parce que l'opération précédente a mal fonctionné ?
Ou parce que l'opération effectuée 200 lignes de code plus tôt a produit un résultat erroné qui est passé inaperçu jusqu'à ce qu'il cause finalement un problème ?

[Margaret Hamilton](https://en.wikipedia.org/wiki/Margaret_Hamilton_\(software_engineer\)),
qui a inventé le terme "génie logiciel" pour donner une légitimité aux logiciels sur la base de son expérience du développement de logiciels pour les premières missions de la NASA,
[disait](https://www.youtube.com/watch?v=ZbVOF0Uk5lU) à propos de ses premiers travaux : "nous avons appris à passer plus de temps en amont [...] afin de ne pas perdre tout ce temps à debugger".

Nous verrons trois méthodes pour rendre le code débogable : la programmation défensive, le logging et le code seulement pour debugging.

### Programmation défensive

Les bugs vous attaquent et vous devez défendre votre code et vos données !
C'est l'idée derrière la _programmation défensive_ : s'assurer que les problèmes qui surviennent en dehors de votre code ne peuvent pas corrompre votre état ou vous faire renvoyer des déchets.
Ces problèmes peuvent être, par exemple, des bugs de logiciels, des entrées non valables saisies par des humains, des tentatives délibérées d'attaque du logiciel par des humains, ou même une corruption du matériel.

Il peut sembler étrange de s'inquiéter de la corruption du matériel, mais cela arrive plus souvent qu'on ne le pense ;
Par exemple, une simple inversion de bit peut transformer `microsoft.com` en `microsfmt.com`, puisque `o` est généralement encodé comme `01101101`
en binaire, qui peut se transformer en `01101111`, l'encodage pour `m`.
Un logiciel qui a l'intention de communiquer avec `microsoft.com`
pourrait donc finir par recevoir des données de `microsfmt.com`, qui peuvent être sans rapport, spécifiquement préparées pour des attaques, ou
[une expérience pour voir dans quelle mesure cela se produit](http://dinaburg.org/bitsquatting.html).

Au lieu de produire silencieusement des déchets, le code doit échouer le plus tôt possible.
Plus une défaillance est proche de sa cause première, plus il est facile de la debugger.

Les _assertions_ sont l'outil clé pour éviter les échecs précoces.
Une assertion est un moyen de vérifier si le code se comporte réellement de la manière dont l'ingénieur qui l'a écrit pense qu'il devrait le faire.

Par exemple, si un morceau de code trouve l'index d'une valeur dans un tableau, un ingénieur pourrait écrire ce qui suit immédiatement après avoir trouvé l'index :
```java
if (array[index] != val) {
  throw new AssertionError(...);
}
```
Si cette vérification échoue, il doit y avoir un bug dans le code qui trouve `index`. L'étape "isoler le bug" du debugging est déjà réalisée par l'assertion.

Mais que faire en cas d'échec de la vérification ? Abandonner le programme ?
Cela dépend du programme. En général, s'il existe un moyen de couper ce qui a causé le problème du reste du programme, c'est une meilleure idée.
Par exemple, la _requête_ actuelle pourrait échouer.
Il peut s'agir d'une requête adressée à un serveur, par exemple, ou d'une opération déclenchée par un utilisateur qui appuie sur un bouton.
Le logiciel peut alors afficher un message indiquant qu'une erreur s'est produite, ce qui permet à l'utilisateur de réessayer ou de faire autre chose.
Cependant, certains échecs sont si graves qu'il n'est pas raisonnable de continuer.
Par exemple, si le code qui charge la configuration du logiciel échoue à une assertion, il est inutile de continuer sans la configuration.

Une assertion qui doit être maintenue lors de l'appel d'une méthode est une _précondition_ de cette méthode.
Par exemple, une méthode `int pickOne(int[] array)` qui renvoie un des éléments du tableau a probablement comme précondition "le tableau n'est pas `null` et a au moins `1` élément".
Le début de la méthode pourrait ressembler à ceci :
```java
int pickOne(int[] array) {
  if (array == null || array.length == 0) {
    throw new IllegalArgumentException(...);
  }
  // ...
}
```
Si un morceau de code appelle `pickOne` avec un tableau nul ou vide, la méthode lèvera une `IllegalArgumentException`.

Pourquoi prendre la peine de vérifier cela explicitement alors que la méthode échouerait de toute façon si le tableau était nul ou vide,
puisque la méthode déréférencera le tableau et indexera son contenu ?
Le type d'exception levée indique _qui est responsable_.
Si vous appelez `pickOne` et obtenez une `NullPointerException`, il est raisonnable de supposer que `pickOne` a un bug, car cette exception indique que
le code de `pickOne` croit qu'une référence donnée est non nulle, puisqu'il la déréférence, alors qu'en pratique la référence est nulle.
Cependant, si vous appelez `pickOne` et que vous obtenez une `IllegalArgumentException`, il est raisonnable de supposer que votre code a un bug,
car cette exception indique que vous avez transmis un argument dont la valeur est illégale.
Ainsi, le type d'exception vous aide à trouver l'endroit où se trouve le bug.

Une assertion qui doit être maintenue lors du retour d'une méthode est une _postcondition_ de cette méthode.
Dans notre exemple, la postcondition est "la valeur retournée est une valeur du tableau", ce qui est exactement ce que vous appelez `pickOne` pour obtenir.
Si `pickOne` renvoie une valeur qui n'est pas dans le tableau, le code qui l'appelle produira n'importe quoi,
parce que le code s'attendait à ce que `pickOne` satisfasse son contrat, ce qui n'a pas été le cas.
Il n'est pas raisonnable d'insérer des assertions à chaque fois que l'on appelle une méthode pour vérifier que la valeur retournée est acceptable ;
c'est plutôt à la méthode de vérifier qu'elle honore sa postcondition.
Par exemple, la fin de `pickOne` peut ressembler à ceci :
```java
int result = ...
if (!contains(array, result)) {
  throw new AssertionError(...);
}
return result;
```
De cette façon, si `result` a été calculé de façon incorrecte, le code échouera avant de corrompre le reste du programme avec une valeur invalide.

Certaines assertions sont à la fois des pré-conditions et des post-conditions pour les méthodes d'un objet : les _invariants d'objet_.
Un invariant est une condition qui reste toujours valable de l'extérieur.
Il peut être cassé au cours d'une opération, à condition que cela ne soit pas visible pour le monde extérieur car il est rétabli avant la fin de l'opération.
Par exemple, considérons les champs suivants pour une pile :
```java
classe Stack {
  private int[] values;
  private int top; // sommet de la pile dans `values`
}
```
Un invariant de cette classe est `-1 <= top < values.length`, c'est-à-dire que soit `top == -1`,
ce qui signifie que la pile est vide, soit `top` pointe vers la valeur supérieure de la pile à l'intérieur du tableau.
Une façon de vérifier les invariants est d'écrire une méthode `assertInvariants` qui les affirme et de l'appeler à la fin du constructeur et au début et à la fin de chaque méthode.
Toutes les méthodes de la classe doivent préserver l'invariant afin qu'elles puissent également compter sur son maintien lorsqu'elles sont appelées.
C'est une des raisons pour lesquelles l'encapsulation est si utile : si n'importe qui pouvait modifier `values` ou `top` sans passer par les méthodes de `Stack`,
il n'y aurait aucun moyen de faire respecter cet invariant.

Considérons la méthode Java suivante :
```java
void setWords(List<String> words) {
  this.words = words;
}
```
Cela semble trivialement correct, et pourtant, on peut l'utiliser de la manière suivante :
```
setWords(badWords);
badWords.add("Pas bien !");
```
Oups ! Maintenant l'état de l'objet qui contient `mots` a été modifié de l'extérieur de l'objet, ce qui pourrait briser les invariants que l'objet est supposé avoir.

Pour éviter cela et protéger l'état d'une personne, des _copies de données_ sont nécessaires lorsqu'il s'agit de valeurs mutables :
```java
void setWords(List<String> words) {
  this.words = new ArrayList<>(words);
}
```
De cette manière, aucun changement ne peut intervenir dans l'état de l'objet à son insu.
Il en va de même pour les lectures, `return this.words` étant problématique et `return new ArrayList<>(this.words)` évitant le problème.

Encore mieux, si possible, l'objet pourrait utiliser une liste _immuable_ pour les `mots`, comme la `List[A]` par défaut de Scala.
Cela résout le problème sans nécessiter de copies de données, qui ralentissent le code.

---
#### Exercice
Consultez le code dans le dossier [stack](exercices/cours/stack), qui contient une classe `IntStack` et un exemple d'utilisation.
Ajoutez du code à `IntStack` pour détecter les problèmes à temps, et corrigez les bugs que vous trouvez dans le processus.
Tout d'abord, regardez ce que le constructeur doit faire. Une fois cela fait, ajoutez un invariant et utilisez-le, ainsi qu'une condition préalable pour `push`.
Ensuite, corrigez les bugs que vous trouvez.

<details>
<summary>Solution (cliquer pour développer)</summary>
<p>

Tout d'abord, le constructeur doit rejeter si `maxSize < 0`, puisque c'est invalide.

Deuxièmement, la pile doit avoir l'invariant `-1 <= top < values.length`, comme nous l'avons vu plus haut.

Après avoir ajouté cet invariant, notez que `top--` dans `pop` peut briser l'invariant puisqu'il est utilisé inconditionnellement. Il en va de même pour `top++` dans `push`.
Elles doivent être modifiées pour ne modifier que `top` si nécessaire.

Pour permettre aux utilisateurs de `IntStack` d'appeler `push` en toute sécurité, on peut exposer une méthode `isFull()`, et l'utiliser comme précondition de `push`.

Nous fournissons une [version corrigée](exercices/solutions/cours/Stack.java).

</p>
</details>


### Logging

Qu'est-ce qui s'est passé en production ?
S'il y a eu un crash, vous pouvez obtenir un crash dump et l'ouvrir dans un debugger.
Mais s'il s'agit d'un bug plus subtil où le résultat "semble erroné" pour un humain, comment pouvez-vous savoir ce qui s'est passé pour produire ce résultat ?

C'est là qu'intervient le _logging_ : l'enregistrement de ce qui se passe pendant l'exécution afin que le log puisse être lu au cas où quelque chose se serait mal passé.
Une façon simple d'enregistrer les données est d'imprimer des instructions :
```python
print("Demande : " + demande)
print("État : " + état)
```
Cette méthode fonctionne, mais n'est pas idéale pour de multiples raisons.
Tout d'abord, le développeur doit choisir ce qu'il veut enregistrer au moment de l'écriture du programme.
Par exemple, si l'enregistrement de chaque appel de fonction est considéré comme trop lourd pour un fonctionnement normal,
le log des appels de fonction ne sera jamais enregistré, même si, dans certains cas, il pourrait être utile.
Deuxièmement, le développeur doit choisir le mode d'enregistrement au moment de l'écriture du programme.
Le log doit-il être imprimé sur la console ? Enregistré dans un fichier ? Les deux ? Certains événements devraient-ils envoyer un courriel aux développeurs ?
Troisièmement, l'utilisation de la même fonction d'impression pour chaque log ne permet pas de distinguer ce qui est important de ce qui ne l'est pas.

Au lieu d'utiliser une fonction d'impression spécifique, les frameworks de logging fournissent l'abstraction d'un log avec plusieurs niveaux d'importance, comme le module de logging de Python :
```python
logging.debug("Détail")
logging.info("Information")
logging.warning("Avertissement")
logging.error("Erreur")
logging.critical("Rien ne va plus")
```
Le nombre de niveaux de logging et leur nom changent dans chaque cadre de logging, mais le fait est qu'il y en a plusieurs et qu'ils n'impliquent rien quant à la destination du log.

Les ingénieurs peuvent écrire des appels de logging pour tout ce qu'ils pensent être utile, en utilisant le niveau de logging approprié, et décider _plus tard_ ce qu'il faut logger et où le faire.
Par exemple, par défaut, les logs "debug" et "info" peuvent ne même pas être stockés, car ils sont trop détaillés et pas assez importants.
Mais s'il y a actuellement un bug subtil dans la production, on peut leur permettre de voir exactement ce qui se passe, sans avoir à redémarrer le programme.
Il peut être judicieux d'enregistrer les erreurs en envoyant un courriel aux développeurs, mais s'il y a beaucoup d'erreurs, les développeurs en sont déjà conscients,
ils peuvent décider d'enregistrer temporairement les erreurs dans un fichier, sans avoir à redémarrer le programme.

Il est important de penser à la protection de la vie privée lors de l'écriture du code de logging.
L'enregistrement du contenu intégral de chaque requête, par exemple, peut conduire à l'enregistrement de mots de passe en texte clair pour une fonction de "création d'utilisateur".
Si ce log est conservé dans un fichier et que le serveur est piraté, les attaquants disposeront d'un log détaillé de tous les mots de passe jamais définis.

### Code seulement pour debugging

Qu'en est-il des contrôles de programmation défensifs et des logs qui sont trop lents pour être raisonnablement activés en production ?
Par exemple, si un graphe a pour invariant "aucun nœud n'a plus de 2 arêtes", mais que le graphe a typiquement des millions de nœuds, que faire ?

C'est là qu'intervient le code _seulement pour debugging_.
Les langages de programmation, leurs moteurs d'exécution et les frameworks offrent généralement des moyens d'exécuter le code uniquement en mode debug,
par exemple lors de l'exécution de tests automatisés.

Par exemple, en Python, on peut écrire un bloc `if __debug__:`, qui ne s'exécutera que lorsque le code n'est pas optimisé.

Il est important de vérifier ce que signifient les termes "debugging" et "optimisé" dans un contexte donné.
Par exemple, en Python, `__debug__` est `True` par défaut, à moins que l'interpréteur ne soit lancé avec le commutateur `-O`, pour "optimize".
En Java, les assertions sont du code de debugging uniquement, mais elles sont désactivées par défaut, et peuvent être activées avec le commutateur `-ea`.
Scala a plusieurs niveaux de code de debugging seulement qui sont tous activés par défaut mais qui peuvent être désactivés sélectivement avec le commutateur `-Xelide-below`.

Plus important encore, avant d'écrire du code de debugging uniquement, réfléchissez bien à ce qu'il est "raisonnable" d'activer en production compte tenu de la charge de travail que vous avez.
Passer une demi-seconde à vérifier un invariant est acceptable dans un morceau de code qui prendra des secondes à s'exécuter parce qu'il effectue de nombreuses requêtes web, par exemple,
même si une demi-seconde représente beaucoup de temps de manière absolue.

Gardez à l'esprit ce que [Tony Hoare](https://en.wikipedia.org/wiki/Tony_Hoare), l'un des pionniers de l'informatique et en particulier des langages de programmation et de la vérification,
a dit un jour dans son ["Hints on Programming Language Design"](https://dl.acm.org/doi/abs/10.5555/63445.C1104368) :
"_Il est absurde de procéder à des contrôles de sécurité élaborés sur des cycles de debugging, alors qu'aucune confiance n'est accordée aux résultats,_
_puis de les supprimer lors de la production, lorsqu'un résultat erroné peut s'avérer coûteux ou désastreux._
_Que penserait-on d'un passionné de voile qui porte son gilet de sauvetage lorsqu'il s'entraîne sur la terre ferme,_
_mais l'enlève dès qu'il prend la mer ?_".


## Résumé

Dans ce cours, vous avez appris :
- Comment écrire un code lisible : noms, formatage, commentaires, conventions
- Comment debugger un code : reproduire des bugs, utiliser un debugger
- Comment écrire du code débogable : programmation défensive, logging, code uniquement pour debugging

Vous pouvez maintenant consulter les [exercices](exercices/) !
