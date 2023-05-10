# Tests

Votre tâche est de tester deux bases de données d'utilisateurs :
`CBDistantCredentialDatabase` qui utilise des callbacks,
et `CFDistantCredentialDatabase` qui utilises des futures.

Voici les scénarios de tests :

1. Essayer d'authentifier un utilisateur inexistant cause une `UnknownUserException`
2. Ajouter un utilisateur à une base de données vide l'ajoute bien
3. Ajouter le même utilisateur deux fois cause une `AlreadyExistsUserException`
4. Ajouter un utilisateur puis essayer de l'authentifier retourne le bon utilisateur
5. Ajouter un utilisateur puis essayer de l'authentifier mais avec un mauvais mot de passe cause une `InvalidCredentialException`
