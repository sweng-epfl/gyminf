# Fournisseurs de documents fiables

Vous venez de rejoindre SwengDocs, une entreprise qui stocke des documents
pour ses clients dans le nuage, et vous avez été affecté à l'équipe
responsable du service de stockage de documents.

L'architecture actuelle de SwengDocs est assez simple : chaque document est stocké
sur un ou plusieurs serveurs, et chaque document est identifié par un identifiant unique.

Le `DocumentService` est responsable de la récupération des documents. Cependant, le service n'est pas très fiable,
si une erreur se produit lors de la récupération d'un document, toute l'opération échoue.
Ce n'est pas acceptable, car le service peut être temporairement indisponible, ou le document peut être disponible sur un autre serveur.

Votre tâche consiste à améliorer la fiabilité du `DocumentService` en implémentant deux fonctionnalités :

1. **Retrying** : si une erreur survient lors de la récupération d'un document, le
   service doit réessayer l'opération. Les tentatives ne doivent s'arrêter que lorsque l'opération
   réussit, ou lorsque le document ne peut pas être trouvé
   (c'est-à-dire qu'une `DocumentNotFoundException` est levée par le `DocumentProvider`).
2. **Fournisseurs multiples** : le service doit être en mesure de récupérer des
   documents auprès de plusieurs fournisseurs, en réussissant si l'un d'entre eux possède le document. Si
   le document n'a pas été trouvé chez tous les fournisseurs, le service doit lancer
   une exception `DocumentNotFoundException`. Sinon, le service doit réessayer l'opération
   sur le fournisseur suivant si l'un d'entre eux échoue avec une autre erreur.

Le `DocumentService` est déjà implémenté, et vous pouvez le trouver dans le fichier
`DocumentService.java`. Vous pouvez également trouver l'interface `DocumentProvider` dans le fichier `DocumentProvider.java`.

Votre tâche consiste à effectuer des changements minimaux dans la classe `DocumentService`, et
d'implémenter les deux fonctionnalités dans la classe `DocumentService`. Vous pouvez ajouter de nouvelles
classes et méthodes, mais vous ne devez pas changer la signature des méthodes existantes.

De plus, une suite de tests est fournie dans le fichier `DocumentServiceTest.java`
pour vous aider à vérifier votre implémentation et vous assurer qu'elle fonctionne comme prévu.
