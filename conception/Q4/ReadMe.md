`app.py` contient un squelette d'application météo, avec un `Model` déjà écrit qui répond aux requêtes de manière asynchrone.

Votre tâche est d'écrire une application console utilisant le pattern "Model-View-ViewModel", avec les fonctionnalités suivantes :
- Affichage du jour et de la météo correspondante
- Une commande pour rafraîchir la météo
- Une commande pour passer au jour suivant
- Une commande pour passer au jour précédent

Une fois que c'est fait, ajoutez une fonctionalité de résilience : l'application doit réessayer d'obtenir la météo plusieurs fois en cas d'erreur.

_Tâche optionelle_ : Essayez d'écrire une autre `View` utilisant [tkinter](https://docs.python.org/3/library/tkinter.html), ce qui ne devrait normalement pas nécessiter de changements au `ViewModel`.
