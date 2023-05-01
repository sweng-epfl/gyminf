# Introduction

Bienvenue dans ce cours de génie logiciel !
Commençons par expliquer pourquoi vous devriez vous intéresser aux logiciels, pourquoi le _génie_ logiciel est important, quel est l'objectif de ce cours, et une introduction rapide aux outils modernes.


## Pourquoi s'intéresser aux logiciels ?

Le but des logiciels est d'aider les humains en automatisant des tâches.
Il s'agit d'une question d'échelle : effectuer des tâches que les humains ne pourraient raisonnablement pas faire eux-mêmes parce que cela prendrait trop de temps ou d'efforts.

Prenons l'exemple du recensement aux États-Unis.
Pour savoir combien de personnes vivent à quel endroit, le gouvernement américain procède à un recensement tous les dix ans.
Le gouvernement engage des personnes qui se rendent dans chaque maison de chaque ville de chaque État et posent des questions sur les habitants et leurs caractéristiques démographiques.

Auparavant, le recensement était effectué manuellement. Cela a bien fonctionné lors de la fondation des États-Unis, mais à la fin du 19e siècle, l'échelle est devenue un problème.
La totalisation des résultats de toutes les maisons pour obtenir les résultats des villes, des États et de l'ensemble du pays prenait beaucoup de temps.
En raison de la croissance démographique, le recensement a commencé à prendre près de dix ans, ce qui signifie qu'au moment où une itération du recensement était effectuée,
ses données étaient déjà considérées comme obsolètes, et il était temps d'en faire un nouveau.
C'est là que l'automatisation est intervenue : une entreprise a mis au point [une machine](https://www.ibm.com/ibm/history/ibm100/us/en/icons/tabulator/)
qui comptait les cartes dans un format spécifique, permettant ainsi au recensement de se dérouler à nouveau dans des délais raisonnables.
Bien entendu, il existe de nombreux autres problèmes qui ne peuvent être résolus manuellement, et la création d'un type de machine spécifique pour chacun d'entre eux n'est pas envisageable.
C'est là que les logiciels entrent en jeu : nous pouvons désormais écrire un _code_ qui effectue ces tâches à l'aide d'un seul type de machine.
Soit dit en passant, la société qui a fabriqué la machine à compter les points survit encore aujourd'hui sous le nom d'IBM !

De nos jours, les logiciels sont omniprésents, et savoir écrire et maintenir des logiciels est donc une compétence très prisée.
Les voitures contiennent des millions de lignes de code, même les "vieilles" qui fonctionnent au gaz plutôt qu'à l'électricité.
Même les appareils électroménagers tels que les machines à laver ou les barbecues utilisent des logiciels suffisamment complexes pour nécessiter des mises à jour régulières afin de corriger les bugs !

Au début des années 2000, les [entreprises ayant le plus de capitalisation de la planète](https://en.wikipedia.org/wiki/List_of_public_corporations_by_market_capitalization)
étaient principalement actives dans les secteurs du gaz, du pétrole, de la santé, de la banque et d'autres services de ce type.
Aujourd'hui, c'est l'inverse : seule une petite fraction des entreprises les plus précieuses s'occupe de services spécifiques tels que la santé,
et la grande majorité d'entre elles s'occupent de logiciels, de matériel ou des deux.

Les logiciels sont également un outil essentiel pour la science.
Les scientifiques ont développé des [modèles de cerveau](https://actu.epfl.ch/news/blue-brain-builds-neurons-with-mathematics/) dans des logiciels, permettant des expériences qui ne seraient pas réalisables sur de vrais cerveaux.
Un autre exemple est la technique de [communication cerveau-texte](https://www.nature.com/articles/s41586-021-03506-2) qui utilise du matériel pour obtenir des signaux directement du cerveau humain et des logiciels pour les traiter,
permettant aux personnes paralysées de communiquer en pensant à écrire avec leur main, qui envoie des signaux du cerveau, même si leur corps ne peut pas bouger !

Il est tentant de penser qu'il existe déjà suffisamment de logiciels, mais c'est loin d'être le cas.
Par exemple, au début de la pandémie de coronavirus, la Suisse n'a pas pu suivre les cas assez rapidement parce que
[les cas devaient être remplis sur des formulaires papier et faxés](https://www.swissinfo.ch/eng/crunching-the-numbers_why-switzerland-struggles-to-keep-track-of-coronavirus-cases/45628604) au gouvernement fédéral.
Ce manque d'automatisation a été un problème majeur pour réagir assez rapidement à une pandémie afin d'aider les citoyens.


## Pourquoi le génie logiciel est-il important ?

Nous venons de voir à quel point les logiciels sont importants, mais pourquoi faut-il suivre un cours sur le _génie_ logiciel ?
Il s'agit avant tout de _confiance_ : permettre aux gens de croire que le logiciel fera ce qu'ils veulent faire de la manière dont ils le veulent.
Les utilisateurs devraient pouvoir compter sur les logiciels pour les tâches quotidiennes, même celles qui pourraient les blesser ou les tuer si elles étaient mal exécutées.

Prenons à nouveau l'exemple des voitures. Les voitures modernes sont dotées de capacités de conduite autonome, qui sont alimentées par un logiciel utilisant des données provenant de capteurs matériels.
Si ce logiciel comporte des bugs qui provoquent des erreurs, [des accidents peuvent se produire](https://www.theguardian.com/technology/2021/aug/16/teslas-autopilot-us-investigation-crashes-emergency-vehicles).
Ces accidents diminuent la confiance des utilisateurs dans le logiciel, ce qui peut rendre l'ensemble du logiciel de conduite autonome inutile en amenant les gens à refuser de l'utiliser.

Les vaisseaux spatiaux sont un autre type de véhicule auquel les utilisateurs doivent faire confiance.
Lorsque la NASA a délégué une partie de la construction du logiciel à Boeing et a vérifié le résultat, [leur enquête](https://www.businessinsider.com/nasa-investigating-potentially-catastrophic-boeing-spaceship-error-2020-2)
a révélé que des "problèmes systémiques" étaient à l'origine d'une erreur logicielle.
En d'autres termes, cette erreur n'était pas le fait d'une seule personne, mais le résultat de mauvaises pratiques dans l'ensemble de l'entreprise.

Avant que la NASA ne dispose de machines, elle employait des ["calculateurs"](https://en.wikipedia.org/wiki/Computer\_\(occupation\)) : des personnes dont le travail consistait à effectuer des calculs.
L'un de ces calculateurs était [Katherine Johnson](https://www.nasa.gov/content/katherine-johnson-biography), qui effectuait des calculs pour l'alunissage, entre autres opérations.
Lorsque l'astronaute John Glenn devait se mettre en orbite autour de la Terre à bord de la capsule Friendship 7,
il a d'abord refusé de voler parce que la NASA avait utilisé des machines pour effectuer les calculs, ce en quoi il n'avait pas confiance.
Il a donc demandé à la NASA que Johnson vérifie les calculs de la machine, en déclarant fameusement :
"Si elle dit qu'ils sont bons, alors je suis prêt à partir". C'est ce qu'elle a fait, et la mission a été un succès.

Pourrions-nous avoir une Katherine Johnson pour vérifier tous les logiciels que nous écrivons ? Malheureusement, la _complexité_ des logiciels modernes rend cette tâche infaisable.
Considérons le morceau de code suivant, qui pourrait se trouver dans la fonction d'accélération d'une voiture auto-conduite :
```python
# Accélérer, sauf si la vitesse est déjà 100
if speed >= 100:
  speed = 100
else:
  speed = speed + 1
```
Ce code divise le programme en deux chemins : l'un dans lequel la vitesse était au moins égale à 100 et a été plafonnée, et l'autre dans lequel la vitesse était inférieure à 100 et a été augmentée.
Une instruction "if" a permis de doubler le nombre de chemins.
S'il y avait une autre déclaration de ce type après celle-ci, il y aurait alors quatre chemins.
Une autre, et il y en aurait huit, et ainsi de suite.
La mission lunaire Apollo 11 contenait [environ 150 000 lignes de code](https://www.synopsys.com/blogs/software-security/apollo-11-software-development/).
Si seulement 1 % de ces lignes sont des instructions "if", cela conduit à 2^1500 chemins.
Et Apollo 11 est minuscule par rapport aux normes modernes ; le système d'exploitation Windows compte des dizaines de millions de lignes de code.
Il n'y a pas assez d'atomes dans l'univers pour répertorier tous les chemins possibles du programme !

L'ingénierie d'un logiciel fiable va toutefois au-delà du problème impossible de la vérification de chaque chemin dans le programme.
Prenons l'exemple d'un programme qui, à partir d'une liste d'étudiants et de leurs notes, envoie à chacun d'entre eux un courrier électronique leur annonçant leur note.
Il s'agit là d'un bon exemple de logiciel automatisant une tâche qui serait longue et sujette à des erreurs si elle était effectuée manuellement.
Le logiciel transforme une ligne de saisie telle que "Alice, 9/10" en un courriel envoyé à Alice pour l'informer de sa note.
Cela fonctionne-t-il toujours si, au lieu d'avoir un nom utilisant des lettres anglaises comme Alice, l'élève s'appelle 狄仁傑 ou محمد بن موسی خوارزمی ?
Que se passe-t-il si l'élève a un nom à l'américaine comme "Bob, Jr", qui comprend une virgule qui est également utilisée par le logiciel pour séparer les noms et les notes dans l'entrée ?
Que se passe-t-il si, après l'envoi des premiers courriels, l'ordinateur sur lequel le logiciel est exécuté perd sa connexion Internet ?
Les courriels sont-ils perdus ? L'exécution répétée du logiciel entraîne-t-elle l'envoi de courriels en double ?
Le logiciel peut-il gérer la notification aux utilisateurs dans une autre langue que l'anglais ?
Par exemple, en français, les salutations sont souvent spécifiques au genre, l'anglais "Dear Alice"/"Dear Bob" devenant le français "_Chère_ Alice"/"_Cher_ Bob". Le logiciel peut-il gérer cela ?
Même s'il gère tous les problèmes susmentionnés, comment une autre personne peut-elle s'en assurer ?
Le responsable du logiciel peut affirmer que cela fonctionne, mais ce n'est pas suffisant pour risquer d'envoyer des notes erronées à vos étudiants.
Et si quelqu'un d'autre lui fait confiance et souhaite ajouter une fonctionnalité, comment cette fonctionnalité peut-elle être réintégrée dans la version "principale" du logiciel ?
L'envoi d'une version par courrier électronique fonctionne si les développeurs sont peu nombreux,
mais cette méthode n'est pas adaptée à des dizaines de personnes apportant des modifications susceptibles d'entrer en conflit.
Rappelons que Windows contient des dizaines de millions de lignes de code ;
une personne seule, ou même une équipe de plusieurs dizaines de personnes, n'est pas suffisante pour développer de grands projets logiciels.


## Le but de ce cours

Ce cours a pour but de transformer les _étudiants_ en _ingénieurs_, en les initiant aux concepts du monde réel et à leurs applications,
afin qu'ils passent de l'_écriture de code_ au _développement de logiciels_.

Un aspect clé de cette démarche est de s'éloigner des exercices théoriques avec des solutions bien définies et de s'orienter vers des exercices du monde réel avec des solutions discutables.
Par exemple, un étudiant peut rendre un travail de codage et recevoir une note reflétant "la qualité" de sa solution.
Mais dans le monde réel, un ingénieur soumet un _projet_ et reçoit des _réactions_ de la part des utilisateurs.
Ce retour d'information peut inclure des désaccords sur le problème même que le logiciel est censé résoudre,
y compris des changements d'opinion de la part du client qui nécessitent des modifications du logiciel même si la solution de l'ingénieur était "bonne" d'un point de vue théorique.

Une analogie utile consiste à imaginer la construction d'un avion.
Si un étudiant rend un avion "complet à 95 %", il peut s'attendre à obtenir une note de 95 %.
Mais si un ingénieur présente un avion "complet à 95 %", le résultat dépend fortement des 5 % manquants.
Si les sièges ne sont pas aussi confortables qu'ils pourraient l'être, ou si la vitesse maximale est un peu inférieure à ce qu'elle devrait être, le client peut toujours être satisfait.
Mais si l'aile n'est qu'à moitié terminée, l'avion ne peut pas voler, même s'il est "complet à 95 %", et le client le rejettera !

Dans les cours précédents, vous avez appris à écrire du code. Dans ce cours, vous apprendrez les autres étapes clés du développement d'un logiciel :
- **Exigences** : comment déterminer les besoins des utilisateurs et comment les traduire en logiciels.
- **Conception** : comment concevoir un logiciel correctement, afin de rendre le logiciel plus facile à écrire et à maintenir.
- **Évolution** : comment prendre un logiciel existant et le faire évoluer pour corriger les bugs et ajouter des fonctionnalités.

Ces étapes ne sont pas entièrement ordonnées non plus, car dans le monde réel des logiciels, il est courant que les exigences changent,
que le plan ait besoin d'être ajusté, ou que le développement commence par l'évolution d'un logiciel existant.

Vous apprendrez également les tâches clés liées à l'écriture d'un code fiable et efficace :
- **Opérations** : comment assurer le suivi du logiciel et de ses modifications, et comment éviter les erreurs humaines telles que l'intégration d'une modification de code qui casse le code existant.
- **Test** : comment tester un logiciel de manière automatisée, pour donner confiance aux autres que le logiciel fait ce qu'il doit faire, et comment utiliser les tests pour aider l'ensemble du processus de développement.
- **Débogage** : comment utiliser les outils et les techniques modernes pour trouver et corriger les bugs d'un logiciel.
- **Performance** : comment concevoir et écrire des logiciels efficaces, et comment trouver et résoudre les problèmes de performance.
- **Sécurité** : comment écrire des logiciels qui résistent aux entrées d'utilisateurs malveillants et comment s'assurer que les utilisateurs ne peuvent pas rompre la confidentialité, l'intégrité et la disponibilité des données.
- **Travail d'équipe** : comment effectuer toutes les tâches susmentionnées au sein d'une équipe, à l'échelle des bases de code des logiciels modernes.


## Outils modernes

Heureusement, il n'est pas nécessaire de repartir de zéro chaque fois que vous ou votre équipe souhaitez concevoir un logiciel.
En fait, si vous deviez écrire des logiciels en partant de rien et sans aide extérieure à chaque fois, vous ne parviendriez jamais à terminer un projet de taille raisonnable.

Les ingénieurs logiciels utilisent des dépôts de paquets tels que [Maven Central](https://mvnrepository.com/repos/central), la [NuGet Gallery](https://www.nuget.org/), 
ou le [NPM Registry](https://www.npmjs.com/) pour réutiliser le code existant.
Si vous souhaitez que votre logiciel réessaie automatiquement des opérations qui ont échoué, [quelqu'un d'autre l'a probablement déjà fait](https://www.nuget.org/packages/Polly) ;
vous n'avez pas besoin de passer des semaines à
écrire une nouvelle bibliothèque, à concevoir des tests, à réfléchir aux cas limites, à la rendre suffisamment générique pour la réutiliser dans plusieurs projets, et ainsi de suite.

Lorsque les ingénieurs logiciels rencontrent des problèmes, ils ne les résolvent pas seuls.
Bien que tout problème puisse être résolu avec suffisamment de temps, l'utilisation efficace de son temps est un objectif clé de l'ingénierie.
Au lieu de cela, les ingénieurs logiciels utilisent des sites web tels que [StackOverflow](https://stackoverflow.com/) pour poser des questions et y répondre.
Répondre à des questions est bénéfique pour celui qui y répond, car l'enseignement est un excellent moyen de revérifier sa compréhension d'un concept.


#### Exercice
Considérez le code PHP suivant, même si vous n'avez jamais utilisé PHP auparavant :
```php
class Context {
    protected $config;
    public function getConfig($key) {
        $cnf = $this->config;
        return $cnf::getConfig($key);
    }
}
```
Si vous essayez d'utiliser ce code, l'interpréteur PHP affichera l'erreur suivante : ``syntax error, unexpected T_PAAMAYIM_NEKUDOTAYIM`` (erreur de syntaxe, T_PAAMAYIM_NEKUDOTAYIM inattendu).
Qu'est-ce qui ne va pas ? (Indice : ce n'est pas un problème que vous pouvez résoudre en regardant le code, utilisez des outils !)
<details>
<summary>Solution (cliquez pour développer)</summary>
<p>

En cherchant ce nom étrange dans votre moteur de recherche préféré, vous trouverez des questions existantes qui vous apprendront
qu'il s'agit en fait de l'hébreu, la langue des auteurs de PHP, pour "double deux-points".
L'erreur vient du fait qu'au lieu d'un double deux-points, le code devrait utiliser une flèche `->`.

</p>
</details>


#### Exercice
Si un collègue vous dit qu'il a reçu un rapport de bug d'un utilisateur de la version "Win32" de votre application,
nommée d'après l'ancienne interface de programmation de Windows, avec le code d'erreur 39, pourriez-vous dire ce qui a causé l'erreur ?
<details>
<summary>Solution (cliquez pour développer)</summary>
<p>

En cherchant "win32 error code 39" ou quelque chose de similaire dans votre moteur de recherche préféré, vous trouverez la documentation de Microsoft pour l'interface de programmation Win32,
Vous y apprendrez que le code d'erreur 0x27, qui correspond au chiffre 39 en hexadécimal, signifie que le disque est plein.
Vous pourrez alors discuter de la meilleure façon de gérer cette erreur, par exemple en affichant un message utile à l'utilisateur,
ou peut-être en supprimant certains des fichiers temporaires de votre application et en réessayant.

</p>
</details>


## Un mot sur la méthode de ce cours

Ce cours n'est pas un cours magistral "traditionnel" dans lequel vous écoutez un cours ou lisez des notes de cours de manière passive.
La recherche sur l'enseignement et l'apprentissage a montré que l'interactivité améliore l'apprentissage, et il y aura donc des exercices fréquents dans les cours, tels que ceux mentionnés ci-dessus.
Il y a également des exercices traditionnels que vous pouvez faire après les cours pour tester votre propre compréhension de la matière.
Les examens ressembleront aux exercices, car leur objectif est également de tester votre compréhension de la matière.
