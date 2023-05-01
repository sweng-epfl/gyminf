# Exigences

Nous n'écrivons pas du code pour le plaisir d'écrire du code : nous développons des logiciels pour _aider les gens à accomplir des tâches_.
Il peut s'agir de "n'importe qui sur Terre" pour les logiciels largement utilisés tels que GitHub, ou de "personnes qui font un travail spécifique" pour les applications internes,
ou même une seule personne dont la vie peut être aidée par un logiciel.
Pour savoir _quel_ logiciel développer, nous devons connaître les besoins des utilisateurs : leurs _exigences_.


## Objectifs

Après cette conférence, vous devriez être en mesure de :
- Définir les besoins des utilisateurs
- Formaliser les exigences en _personas_ et en _récits utilisateurs_
- Développer des logiciels sur la base d'exigences formalisées
- Comprendre les exigences _implicites_ et _explicites


## Quels sont les besoins ?

Une exigence est quelque chose dont les utilisateurs ont besoin.
Par exemple, un utilisateur peut vouloir se déplacer d'un endroit à un autre. Il peut alors utiliser une voiture.
Mais peut-être l'utilisateur a-t-il d'autres exigences, comme le fait de ne pas vouloir ou de ne pas pouvoir conduire, auquel cas un train pourrait répondre à ses besoins.
Les utilisateurs peuvent également avoir des exigences plus spécifiques, comme le fait de vouloir un moyen de transport à faible émission de carbone,
et doivent se déplacer entre des endroits éloignés des transports publics, auquel cas une voiture électrique alimentée par une électricité bas-carbone pourrait être une solution.

Les exigences ne concernent pas les détails de la mise en œuvre.
Un type spécifique de moteur électrique ou un type spécifique d'acier pour les portières de la voiture ne sont pas des exigences de l'utilisateur.
Toutefois, les utilisateurs peuvent avoir des besoins qui amènent les concepteurs du système à faire de tels choix.

Il arrive que l'on distingue les exigences "fonctionnelles" des exigences "non fonctionnelles", ces dernières étant également connues sous le nom d'"attributs de qualité".
Les exigences "fonctionnelles" sont celles qui sont directement liées aux caractéristiques, tandis que les exigences "non fonctionnelles" comprennent l'accessibilité, la sécurité, les performances, etc.
La distinction n'est pas toujours claire, mais elle est parfois faite.

La définition des besoins commence généralement par une discussion avec les utilisateurs.
C'est plus facile si le logiciel a un petit nombre d'utilisateurs bien définis, comme un logiciel spécialement conçu pour qu'une personne puisse faire son travail au sein d'une entreprise.
C'est plus difficile si le logiciel a un grand nombre d'utilisateurs mal définis, comme un moteur de recherche ou une application pour écouter de la musique.

Il est important, lorsque l'on écoute ce que disent les utilisateurs, de garder à l'esprit ce dont ils ont _besoin_ plutôt que ce qu'ils _veulent_.
Ce que les utilisateurs déclarent vouloir est fortement influencé par ce qu'ils connaissent et utilisent déjà.
Par exemple, une personne habituée à voyager à cheval et qui doit traverser une montagne peut demander un "cheval volant", alors qu'il s'agit en fait de traverser la montagne,
et donc un train avec tunnel ou un avion répondrait à leurs besoins.
De même, avant l'avènement du téléphone intelligent moderne, les utilisateurs auraient demandé des vieux téléphones pour la simple raison qu'ils ne savaient même pas qu'un téléphone intelligent était possible,
même si aujourd'hui ils préfèrent leur téléphone intelligent à leur ancien téléphone.

Les souhaits des utilisateurs peuvent être ambigus, surtout lorsqu'ils sont nombreux.
Si vous sélectionnez les cellules contenant "100" et "200" dans un tableur tel que Microsoft Excel et que vous élargissez la sélection, que se passe-t-il ?
Excel doit-il remplir les nouvelles cellules avec "300", "400", etc. ? Doit-il répéter "100" et "200" ?
Que se passe-t-il si vous développez une sélection contenant la cellule unique "Salle 120" ? Doit-elle être répétée, ou doit-elle devenir "Salle 121", "Salle 122", etc. ?
Il n'y a pas de réponse parfaite à ces questions, car toute réponse laissera certains utilisateurs insatisfaits, mais un développeur doit faire un choix.

Ne pas écouter les besoins des utilisateurs peut coûter cher, comme Microsoft l'a constaté avec Windows 8.
L'interface utilisateur de Windows 8 était une réinvention majeure de l'interface Windows, utilisant un "écran de démarrage" plutôt qu'un menu,
avec des applications en plein écran qui pouvaient être empilées plutôt que déplacées.
Il s'agissait d'un changement radical par rapport au Windows que les utilisateurs connaissaient, et ce fut un échec commercial.
Microsoft a dû rétablir le menu Démarrer et abandonner le concept d'applications plein écran en mosaïque.
Cependant, Apple a ensuite fait quelque chose de similaire pour une nouvelle version de son système d'exploitation pour iPad,
et cela a plutôt bien fonctionné, peut-être parce que les utilisateurs ont des attentes différentes sur les ordinateurs de bureau et les tablettes.


## Comment formaliser les exigences ?

Une fois que vous avez discuté avec un grand nombre d'utilisateurs et obtenu de nombreuses idées sur les besoins des utilisateurs, comment consolider ce retour d'information en éléments exploitables ?
C'est la raison d'être de la formalisation des exigences, et nous discuterons de la formalisation du _qui_ avec les "personas" et du _quoi_ avec les "user stories".

À qui s'adresse le logiciel ? La réponse à cette question est parfois évidente, car le logiciel est destiné à un petit groupe d'utilisateurs spécifiques, mais la plupart des grands logiciels sont destinés à de nombreuses personnes.
En fait, les grands logiciels comptent généralement beaucoup trop d'utilisateurs pour qu'un processus personnalisé puisse être mis en place.
Au lieu de cela, vous pouvez utiliser des _personas_ pour représenter des groupes d'utilisateurs.

Un persona est une personne _abstraite_ qui représente un groupe d'utilisateurs similaires.
Par exemple, dans une application musicale, une persona pourrait être Alice, une étudiante, qui utilise l'application pendant son trajet dans les transports publics.
Alice n'est pas une personne réelle, et elle n'a pas besoin de caractéristiques spécifiques telles qu'une couleur de cheveux ou une nationalité.
Au lieu de cela, Alice est une représentation abstraite des nombreuses personnes qui pourraient utiliser l'application et qui ont toutes des caractéristiques similaires du point de vue de l'application,
à savoir qu'elles utilisent l'application dans les transports publics pour se rendre à l'école, à l'université ou dans un autre lieu similaire.
Les exigences d'Alice pourraient conduire à des fonctionnalités telles que le téléchargement de podcasts à l'avance à la maison et l'écoute avec l'écran éteint.
Une autre persona pour la même application pourrait être Bob, un retraité, qui utilise l'application pour cuisiner et faire le ménage.
Bob n'est pas non plus une personne réelle, mais il représente un groupe d'utilisateurs potentiels qui ne sont pas très au fait des dernières technologies
et qui souhaitent utiliser l'application pendant qu'ils effectuent des tâches à la maison.

Bien qu'il soit possible de créer des personas pour de nombreux groupes d'utilisateurs potentiels, elles ne seront pas toutes retenues.
Toujours pour l'exemple de l'application musicale, un autre personnage pourrait être Carol, une "hacker" qui veut écouter de la musique piratée.
Carol aurait besoin de fonctionnalités telles que le chargement de morceaux de musique existants dans l'application et le contournement de la protection des droits d'auteur.
L'application est-elle destinée à des personnes comme Carol ? C'est aux développeurs d'en décider.

Un dernier mot sur les personas : évitez de trop les abstraire. Les personas sont utiles parce qu'elles représentent des personnes réelles d'une manière utile au développement.
Si vos personas finissent par ressembler à "Jean, un utilisateur qui utilise l'application" ou "Jeanne, une personne qui a un téléphone", elles ne seront pas utiles.
De même, si vous savez déjà qui est exactement dans un groupe d'utilisateurs, il n'est pas nécessaire de l'abstraire.
"Sam, un administrateur système" n'est pas une persona utile si votre application n'a qu'un seul administrateur système : utilisez plutôt la personne réelle.

---

#### Exercice
Quels pourraient être des personas pour une application de chat vidéo ?
<details>
<summary>Exemple de solutions (cliquer pour développer)</summary>
<p>

Anne, une responsable qui s'adresse fréquemment à son équipe tout en travaillant à distance.

Basil, un retraité qui souhaite dialoguer par vidéo avec ses petits-enfants pour rester en contact.

Carlos, un médecin qui doit parler à des patients dans le cadre d'une installation de télémédecine.

</p>
</details>

---

Que peuvent faire les utilisateurs ? Après avoir défini à qui s'adresse le logiciel, il faut décider des fonctionnalités à mettre en place.
Les récits utilisateurs sont un outil utile pour formaliser les caractéristiques basées sur les exigences,
y compris qui veut la caractéristique, quelle est la caractéristique, et quel est le contexte.
Le contexte est essentiel, car la même fonctionnalité peut être mise en oeuvre de manière extrêmement différente en fonction du contexte.
Par exemple, "envoyer des courriers électroniques contenant des informations" est une fonction qu'un système logiciel peut avoir.
Si les utilisateurs souhaitent archiver des informations, les courriers électroniques doivent contenir des informations très détaillées, mais leur heure d'arrivée n'a que peu d'importance.
Si le contexte est que les utilisateurs souhaitent recevoir une notification dès qu'un événement se produit,
les courriels doivent être envoyés immédiatement, et il convient de faire très attention à ce qu'ils ne se retrouvent pas dans un filtre anti-spam.
Si le contexte est que les utilisateurs souhaitent partager des données avec leurs amis qui n'utilisent pas le logiciel,
les courriels doivent avoir une conception claire qui ne contient que les informations pertinentes afin qu'ils puissent être facilement transférés.

Il existe de nombreux formats pour les récits utilisateurs ; dans ce cours, nous utiliserons le format en trois parties "_en tant que... je veux... pour..._".
Ce format inclut l'utilisateur qui souhaite la fonctionnalité, qui peut être un persona ou un rôle spécifique, la fonctionnalité elle-même et
un contexte expliquant pourquoi l'utilisateur souhaite cette fonctionnalité.
Par exemple, "En tant qu'étudiant, je veux regarder des enregistrements de cours, afin de pouvoir rattraper mon retard après une maladie".
Ce récit utilisateur permet aux développeurs de créer une fonctionnalité qui est réellement utile à la personne : il ne serait pas utile à cet étudiant, par exemple,
de créer une fonction d'enregistrement des cours qui soit une archive accessible une fois le cours terminé, car on peut supposer que l'étudiant ne sera pas malade pendant toute la durée du cours.

Revenons à notre exemple d'application musicale et considérons le récit utilisateur "En tant qu'Alice, je souhaite télécharger des podcasts à l'avance, afin d'économiser des données mobiles".
Cela signifie que l'application doit télécharger l'intégralité du podcast à l'avance, mais Alice dispose toujours de données mobiles, elle ne veut simplement pas en utiliser trop.
Un récit similaire dans un contexte différent pourrait être "En tant que navetteur en voiture, je souhaite télécharger des podcasts à l'avance,
afin de pouvoir utiliser l'application sans données mobiles".
Ce récit conduit à une autre fonctionnalité : maintenant, l'application ne peut pas du tout utiliser les données mobiles,
parce que le navetteur n'a tout simplement pas de données à certains moments de son trajet.

Pour évaluer les récits utilisateurs, rappelez-vous l'acronyme "INVEST" :
- **I**ndépendant : le récit doit être autonome.
- **N**égociable : le récit n'est pas un contrat strict mais peut évoluer.
- **V**aluable (ayant une valeur) : le récit doit apporter une valeur évidente à quelqu'un.
- **E**stimable : les développeurs doivent être en mesure d'estimer le temps nécessaire à la mise en oeuvre du récit.
- _**S**mall_ (petit) : le récit doit être d'une taille raisonnable et ne pas être un énorme récit "fourre-tout".
- **T**estable : les développeurs doivent être en mesure de savoir quels sont les critères d'acceptation du récit sur la base de son texte, afin de pouvoir tester leur mise en oeuvre.

Les récits trop difficiles à comprendre et surtout trop vagues échoueront au test "INVEST".

#### Exercice
Quels récits utilisateurs pourriez-vous utiliser pour une application de chat vidéo ?
<details>
<summary>Exemple de solutions (cliquer pour développer)</summary>
<p>

En tant qu'Anne, je veux voir mon calendrier dans l'application, afin de pouvoir planifier des réunions sans entrer en conflit avec mes autres engagements.

Comme Basil, je veux lancer une réunion à partir d'un message que mes petits-enfants m'envoient, afin de ne pas avoir à passer du temps à configurer l'application.

En tant qu'adepte de la protection de la vie privée, je veux que mes chats vidéo soient chiffrés de bout en bout, afin que mes données ne soient pas divulguées en cas de piratage des serveurs de l'application.

</p>
</details>

#### Exercice
Lesquels des éléments suivants constituent des bons récits utilisateur et pourquoi ?
1. En tant qu'utilisateur, je veux me connecter rapidement pour ne pas perdre de temps.
2. En tant que titulaire d'un compte Google, je souhaite me connecter avec mon adresse Gmail.
3. En tant que cinéphile, je souhaite afficher les films recommandés en haut sur un fond gris foncé avec un défilement horizontal.
4. En tant que lecteur occasionnel, je veux savoir où je me suis arrêté la dernière fois, afin de poursuivre ma lecture.
5. En tant que développeur, je souhaite améliorer l'écran de connexion, afin que les utilisateurs puissent se connecter avec des comptes Google.
<details>
<summary>Solutions (cliquez pour développer)</summary>
<p>

1 est trop vague, 2 est acceptable car la raison est implicite et évidente, 3 est beaucoup trop spécifique, 4 est excellent, et 5 est terrible car il concerne les développeurs et non les utilisateurs.

</p>
</details>


## Comment pouvons-nous développer à partir des exigences ?

Vous avez écouté les utilisateurs, vous les avez abstraits dans des personas et leurs exigences dans des récits utilisateurs, et vous avez développé une application sur cette base.
Vous êtes convaincu que vos personas aimeraient votre application et que votre mise en œuvre répond aux besoins définis par les récits des utilisateurs.
Après avoir dépensé beaucoup de temps et d'argent, vous disposez maintenant d'une application que vous pouvez présenter à de vrais utilisateurs... et ils ne l'aiment pas.
Ce n'est pas du tout ce qu'ils avaient imaginé. Qu'est-ce qui n'a pas fonctionné ?
Ce que vous venez de faire, en demandant aux utilisateurs leur avis sur l'application, est une _validation_ : vous vérifiez si ce que vous avez spécifié correspond à ce que veulent les utilisateurs.
Ceci est différent de la _vérification_, qui vérifie que votre application fait correctement ce que vous avez spécifié.

L'une des clés de la réussite d'un logiciel est de procéder à une validation précoce et fréquente, plutôt que de l'attendre jusqu'à la fin.
Si ce que vous construisez ne correspond pas aux attentes des utilisateurs, vous devez le savoir le plus tôt possible,
au lieu de gaspiller des ressources à construire quelque chose que personne n'utilisera.
Pour effectuer cette validation, vous devrez construire le logiciel d'une manière qui puisse être décrite par les utilisateurs,
en utilisant un _vocabulaire commun_ avec eux et en les _intégrant_ dans le processus afin qu'ils puissent donner leur avis.
Voyon donc ces deux façons de procéder.

Tout d'abord, vous avez besoin d'un vocabulaire commun avec vos utilisateurs, comme le résume Eric Evans dans son livre de 2003 "Domain-Driven Design".
Envisagez la fabrication de bonbons : vous pourriez demander à l'avance aux gens s'ils veulent des bonbons contenant
du NaCl, $C_{24}$ $H_{36}$ $O_{18}$, $C_{36}$ $H_{50}$ $O_{25}$, $C_{125}$ $H_{188}$ $O_{80}$, et ainsi de suite.
Il s'agit d'une définition précise que vous pourriez donner à des chimistes, qui créeraient ensuite le produit en question.
Toutefois, il est peu probable qu'une personne ordinaire comprenne ce que c'est avant que vos chimistes ne le créent réellement.
Au lieu de cela, vous pourriez demander aux gens s'ils veulent des bonbons au "caramel salé".
C'est moins précis, car on peut imaginer différentes sortes de caramel salé, mais beaucoup plus compréhensible pour les utilisateurs finaux.
Vous n'avez pas besoin de créer des biscuits au caramel salé pour que les gens vous disent s'ils aiment l'idée ou non,
et une discussion sur le bonbon que vous proposez sera beaucoup plus fructueuse si l'on utilise le terme "caramel salé"
plutôt qu'une formule chimique.

Dans son livre, Evans propose quelques termes spécifiques qui peuvent être enseignés aux utilisateurs, tels que "entité" pour les objets dont l'identité est liée à une propriété spécifique,
"objet valeur" pour les objets qui sont des agrégats de données sans identité distincte, etc.
L'important n'est pas de savoir quels termes exacts vous utilisez, mais l'idée qu'il faut concevoir un logiciel d'une manière qui puisse être facilement décrite aux utilisateurs.

Prenons l'exemple de ce qu'un utilisateur pourrait appeler un "service de connexion", qui identifie les utilisateurs par ce qu'ils appellent des "adresses électroniques".
Un programmeur habitué à l'aspect technique des choses pourrait appeler cela une `PrincipalFactory`,
puisque "principals" est une façon d'appeler une identité d'utilisateur, et qu'une "factory" est un objet qui crée des objets.
Les identifiants pourraient être techniquement appelés "ID".
Cependant, si l'on demande à un utilisateur "Que doit-il se passer lorsque l'ID n'est pas trouvé ? Le principal renvoyé par la fabrique doit-il être `null` ?", l'utilisateur sera perplexe.
La plupart des utilisateurs ne connaissent aucun de ces termes.
Au lieu de cela, si l'objet dans le code est nommé `LoginService`, et prend en compte des objets de type `Email` pour identifier les utilisateurs, le programmeur peut maintenant demander à l'utilisateur
"Que se passe-t-il lorsque l'e-mail n'est pas trouvé ? Le processus de connexion doit-il échouer ?" et obtenir une réponse utile.

L'utilisation d'un vocabulaire _correct_ pour discuter avec les gens passe aussi par l'utilisation d'un vocabulaire _spécifique_. Prenons le terme "personne".
Si vous demandez à des employés d'une université ce qu'est une "personne", ils marmonneront une vague réponse sur le fait que les gens ont un nom et un visage,
parce qu'ils n'ont pas affaire à des "personnes" en général dans leur travail.
Ils s'occupent plutôt de types de personnes spécifiques.
Par exemple, les gens du service financiers ont affaire à des "employés" et à des "contractants", et pourraient volontiers vous enseigner exactement ce que sont ces concepts,
en quoi ils diffèrent, quels types d'attributs ils possèdent, quelles opérations sont effectuées sur leurs données, etc.
Evans parle de "contexte délimité" : dans un domaine d'activité spécifique, certains mots ont une signification particulière, qui doit se refléter dans la conception.
Imaginez que vous essayiez de faire en sorte qu'un auditeur financier,
un employé de cafétéria et un professeur se mettent d'accord sur ce qu'est une "personne" et discutent de l'ensemble
de l'application en utilisant une définition de la "personne" qui inclut tous les attributs possibles.
Cela prendrait une éternité et tout le monde s'ennuierait.
Au lieu de cela, vous pouvez parler à chaque personne séparément, représenter ces concepts séparément dans le code et effectuer des opérations pour les relier entre eux par le biais d'une identité commune,
comme une fonction `get_employee(email)`, une fonction `get_student(email)`, et ainsi de suite.

Une fois que vous disposez d'un langage commun, vous pouvez également rédiger des scénarios de test d'une manière compréhensible pour les utilisateurs.
Il s'agit du _développement guidé par le comportement_ (Behavior-Driven Development),
qui peut être réalisé à la main ou à l'aide d'outils tels que [Cucumber](https://cucumber.io/) ou [Behave](https://behave.readthedocs.io/).
L'idée est d'écrire des scénarios de test en trois étapes : "_étant donné que... quand... alors..._", qui contiennent un état initial, une action et un résultat.

Voici par exemple un exemple de Behave tiré de leur documentation :
```
Schéma du scénario : Mélangeurs
   Étant donné que j'ai mis <chose> dans un mixeur,
   Quand j'allume le mixeur
   Alors il doit se transformer en <autre chose>

Exemples : Amphibiens
  | chose                       | autre chose |
  | Grenouille arboricole rouge | bouillie    |

Exemples : Électronique grand public
  | chose        | autre chose      |
  | iPhone       | déchets toxiques |
  | Galaxy Nexus | déchets toxiques |
```
En utilisant ce texte, on peut écrire des fonctions pour "mettre un objet dans un mixeur", "mettre en marche le mixeur" et "vérifier ce qu'il y a dans le mixeur",
et Behave exécutera les fonctions pour les arguments fournis.
Les utilisateurs ne doivent pas regarder les fonctions elles-mêmes, mais seulement le texte, et ils peuvent alors dire si cela correspond à ce qu'ils attendaient.
Peut-être que seules les grenouilles bleues, et non les grenouilles rouges, doivent se transformer en bouillie.
Ou peut-être que le scénario de test est précisément ce dont ils ont besoin, et que les développeurs doivent donc implémenter la fonctionnalité réelle.

Le processus global est le suivant :
1. Discuter avec les utilisateurs pour connaître leurs besoins
2. Traduire ces exigences en histoires d'utilisateurs
3. Définir des scénarios de test basés sur ces histoires d'utilisateurs
4. Obtenir un retour d'information de la part des utilisateurs sur ces scénarios
5. Répéter l'opération autant de fois que nécessaire jusqu'à ce que les utilisateurs soient satisfaits ; la mise en œuvre peut alors commencer.

#### Exercice
Quel vocabulaire utiliseriez-vous pour discuter d'un système d'inscription aux cours dans une université (ou de tout autre système que vous utilisez fréquemment),
et quels scénarios de test pourriez-vous définir ?
<details>
<summary>Exemple de solutions (cliquer pour développer)</summary>
<p>

Un système d'inscription aux cours pourrait avoir des étudiants, qui sont des entités identifiées par une adresse électronique de l'université,
qui disposent d'une liste de cours et de notes associées à ces cours, et
les professeurs, qui sont associés aux cours qu'ils enseignent et peuvent les modifier. Les cours eux-mêmes peuvent avoir un nom, un code, une description et un nombre de crédits.

Certains scénarios de test pourraient être les suivants :
"Étant donné qu'un utilisateur est déjà inscrit à un cours, quand l'utilisateur essaie de s'inscrire à nouveau, alors cela n'a aucun effet", ou "Étant donné qu'un professeur
est responsable d'un cours, quand le professeur fixe la note d'un étudiant dans le cours, alors la note de cet étudiant est mise à jour".

</p>
</details>


## Quels sont les besoins implicites ?

Les ingénieurs en logiciel conçoivent des systèmes pour toutes sortes de personnes, de toutes les régions du monde, avec toutes sortes de besoins.
Souvent, certaines personnes ont des exigences qui sont _implicites_, mais qui sont tout aussi nécessaires que les exigences dont elles vous parleront explicitement.
Concrètement, nous verrons la _traduction_ ("localization" en anglais), l'_internationalisation_ et l'_accessibilité_.
Ils sont parfois abrégés en "l10n", "i18n" et "a11y", chacun ayant conservé sa lettre de début et de fin, les lettres restantes étant réduites à leur nombre.
Par exemple, il y a 10 lettres entre "l" et "n" dans "localization", d'où "l10n".

La _traduction_ est importante. Les utilisateurs s'attendent à ce que tous les textes des programmes soient rédigés dans leur langue, même s'ils n'y pensent pas explicitement.
Au lieu de `print("Hello " + user)`, par exemple, votre code devrait utiliser une constante qui peut être modifiée en fonction de la langue.
Il est tentant d'avoir une constante `HELLO_TEXT` avec la valeur `"Hello"` pour l'anglais,
mais cela ne fonctionne pas pour toutes les langues car le texte peut aussi venir après le nom d'utilisateur, et pas seulement avant.
Le code pourrait donc utiliser une fonction qui se charge d'envelopper le nom de l'utilisateur avec le bon texte : `print(hello_text(user))`.

La traduction peut sembler simple, mais elle implique également une vérification des hypothèses de votre interface utilisateur et de votre logique.
Par exemple, un bouton qui peut contenir le texte "Log in" en anglais peut ne pas être assez large lorsque le texte est le français "Connexion".
Un champ de texte suffisamment large pour contenir chacun des mots de "capitaine de la navigation à vapeur du Danube" pourrait déborder sur l'allemand "Donaudampfschifffahrtsgesellschaftkapitän".
Vos fonctions qui fournissent du texte traduit peuvent avoir besoin de plus d'informations que vous ne le pensez.
Les noms anglais n'ont pas de genre grammatical, donc tous les noms peuvent utiliser le même texte, mais le français en a deux, l'allemand en a trois,
et le swahili en a [dix-huit](https://en.wikipedia.org/wiki/Swahili_grammar#Noun_classes) !
Les noms anglais ont une forme "singulière" et une forme "plurielle", tout comme de nombreuses langues telles que le français, mais ce n'est pas universel ;
le slovène, par exemple, a une terminaison pour 1, une pour 2, une pour 3 et 4, et une pour 5 et plus.

Les traductions peuvent comporter des bugs, tout comme les logiciels.
Par exemple, la traduction allemande du jeu Champions World Class Soccer comporte un bug dans lequel "shootout" n'est pas traduit par "schiessen", comme il se doit,
mais plutôt à "scheissen", qui a une signification totalement différente bien qu'il n'y ait qu'une lettre d'écart.
Un autre cas de problèmes allemands se présente [dans le jeu Grandia HD](https://www.nintendolife.com/news/2019/08/random_amazingly_grandia_hds_translation_gaffe_is_only_the_second_funniest_german_localisation_mistake) :
manquer une attaque affiche le texte "Fräulein", qui est bien la traduction du mot anglais "Miss" mais dans un contexte totalement différent.

La traduction n'est pas quelque chose que vous pouvez faire seul, à moins que vous ne traduisiez vers votre langue maternelle, car personne ne connaît toutes les caractéristiques de toutes les langues.
Tout comme les autres parties d'un logiciel, la traduction doit être testée, en l'occurrence par des locuteurs natifs.

L'_internationalisation_ est une question d'éléments culturels autres que la langue.
Prenons l'exemple suivant :

<p align="center"><img alt="Illustration de (de gauche à droite) un t-shirt sale, une machine à laver, un t-shirt propre" src="images/washing.svg" width="50%" /></p>

Que voyez-vous ? Comme vous lisez un texte en français, vous pensez peut-être qu'il s'agit d'une illustration d'un t-shirt qui passe de sale à propre dans une machine à laver.
Mais quelqu'un dont la langue maternelle se lit de droite à gauche, comme l'arabe, pourrait voir le contraire : un t-shirt qui passe de propre à sale dans la machine.
C'est un peu dommage, mais c'est ainsi que fonctionne la communication humaine : les gens ont des attentes implicites qui sont parfois contradictoires. Les logiciels doivent donc s'adapter.
Un autre exemple est de mettre "Vincent van Gogh" dans une liste de personnes classées par nom de famille. Vincent est-il sous "G" pour "Gogh" ou sous "V" pour "van Gogh" ?
Cela dépend de la personne à qui l'on s'adresse : les néerlandais attendent le premier, les belges le second. Les logiciels doivent s'adapter, sinon au moins l'un de ces deux groupes sera confus.
L'utilisation d'un format de date spécifique à une culture est un autre exemple : "10/01" signifie des dates très différentes pour un habitant des États-Unis et pour un habitant du reste du monde.

Les noms des personnes constituent un élément important lié à l'internationalisation.
De nombreux systèmes logiciels sont construits sur la base d'hypothèses étranges concernant les noms des personnes,
telles que "ils sont entièrement composés de lettres", ou "les noms de famille ont au moins 3 lettres", ou simplement "les noms de famille sont quelque chose que tout le monde a".
En général, [les programmeurs croient beaucoup de choses fausses sur les noms](https://shinesolutions.com/2018/01/08/falsehoods-programmers-believe-about-names-with-examples/),
ce qui entraîne de nombreuses difficultés pour les personnes dont le nom n'est pas conforme à ces hypothèses,
comme les personnes dont le nom comporte des traits d'union ou des apostrophes, ou encore les personnes dont le nom ne comporte qu'une ou deux lettres,
les personnes issues de cultures qui n'ont pas de notion de nom de famille, etc.
Rappelez-vous que _le nom d'une personne n'est jamais invalide_.

Tout comme la traduction, l'internationalisation n'est pas quelque chose que vous pouvez faire seul.
Même si vous êtes originaire de la région que vous visez, cette région est susceptible de contenir de nombreuses personnes issues de cultures différentes.
L'internationalisation doit être testée.

L'_accessibilité_ est une propriété que possède un logiciel lorsqu'il peut être utilisé par tout le monde, même par les personnes qui n'entendent pas, ne voient pas, n'ont pas de mains, etc.
Les fonctions d'accessibilité comprennent les sous-titres, la synthèse vocale, la dictée, les claviers à une main, etc.
Les frameworks d'interface utilisateur ont généralement des fonctions d'accessibilité documentées en même temps que leurs autres fonctions.
Ils sont utiles non seulement aux personnes souffrant d'un handicap permanent, mais aussi à celles qui sont temporairement incapables d'utiliser une partie de leur corps.
Par exemple, les sous-titres sont pratiques pour les personnes qui se trouvent dans des trains bondés et qui ont oublié leurs écouteurs.
La synthèse vocale est pratique pour les personnes qui font autre chose pendant qu'elles utilisent une application sur leur téléphone.
Les fonctions conçues pour les personnes sans mains sont pratiques pour les parents qui tiennent leur bébé.

L'accessibilité n'est pas seulement une bonne chose d'un point de vue moral : elle est souvent exigée par la loi, en particulier pour les logiciels destinés aux agences gouvernementales.
C'est également une bonne chose d'un point de vue égoïste : une application plus accessible a plus de clients potentiels.


## Toutes les exigences sont-elles éthiques ?

Nous avons parlé des exigences des utilisateurs en partant du principe que vous devez faire tout ce dont les utilisateurs ont besoin. Mais est-ce toujours le cas ?

Parfois, les exigences sont en conflit avec votre éthique d'ingénieur, et ces conflits ne doivent pas être ignorés.
Ce n'est pas parce qu'"un ordinateur le fait" que la tâche est acceptable ou qu'elle sera exécutée sans aucun biais.
L'ordinateur peut être impartial, mais il exécute un code écrit par un être humain,
qui reproduit les hypothèses et les préjugés de cet être humain, ainsi que toutes sortes de problèmes dans les données sous-jacentes.

Par exemple, il y a eu de nombreuses variantes d'"algorithmes pour prédire si quelqu'un sera un criminel", utilisant des caractéristiques telles que les visages des personnes.
Si quelqu'un passait dans une classe et disait à chaque élève "tu es un criminel" ou "tu n'es pas un criminel",
on pourrait raisonnablement être contrarié et soupçonner toutes sortes de mauvaises raisons pour ces décisions.
Il en va de même pour un ordinateur : il n'existe pas d'algorithme magique "impartial" ou "objectif" et, en tant qu'ingénieur logiciel, vous devez toujours être conscient de l'éthique.


## Résumé

Dans cette conférence, vous avez appris à :
- Définir et formaliser les besoins des utilisateurs à l'aide d'exigences, de personas et de récits d'utilisateurs.
- Développement basé sur les besoins par le biais d'une conception axée sur le domaine et d'un développement axé sur le comportement
- Comprendre les exigences implicites telles que la traduction, l'internationalisation, l'accessibilité et l'éthique

Vous pouvez maintenant consulter les [exercices](exercices/) !

