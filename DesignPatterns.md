Ce document contient une liste de design patterns courantes, avec leur contexte, et un exemple.

_Les exemples ne sont là que pour illustrer les patterns de manière concise, du vrai code devrait gérer la visibilité (`public`, `private`, etc.),
certains champs devraient probablement être `final`, etc._


# Adapter

Un _adapter_ est utile quand on a un objet de type `X` à disposition mais que l'interface que l'on veut utiliser n'accepte que des objets de type `X'`,
similaire mais pas égal à `X`.
Par exemple, une app utilise deux librairies qui ont les deux une interface pour une couleur à 4 canaux, une B/G/R/A et l'autre A/R/G/B.
Il n'est pas directement possible d'utiliser un objet venant de la première librairie avec la deuxième, et c'est là qu'intervient un _adapter_ :
un objet qui enveloppe un autre objet et fournit l'interface désirée.

Un exemple dans la vraie vie est un adapteur éléctrique, pour utiliser par exemple un appareil suisse sur une prise américaine : les deux sont fondamentalement du même type,
mais il faut un adaptateur passif pour transformer l'interface afin qu'elle fonctionne.

Exemple :

```java
interface BgraColor {
    // 0 = B, 1 = G, 2 = R, 3 = A
    float getChannel(int index);
}

interface ArgbColor {
    float getA();
    float getR();
    float getG();
    float getB();
}

class BgraToArgbAdapter implements ArgbColor {
    BgraColor wrapped;

    BgraToArgbAdapter(BgraColor wrapped) {
        this.wrapped = wrapped;
    }

    @Override public float getA() { return wrapped.getChannel(3); }
    @Override public float getR() { return wrapped.getChannel(2); }
    @Override public float getG() { return wrapped.getChannel(1); }
    @Override public float getB() { return wrapped.getChannel(0); }
}

```


# Builder

Un _builder_ est utile quand construire un objet d'un seul coup n'est pas désirable ou pas possible et que l'objet final doit être immutable.
Par exemple, un `Rectangle` prenant comme arguments `width, height, borderThickness, borderColor, isBorderDotted, backgroundColor` est complexe,
et un constructeur avec tous ces arguments serait difficile à lire quand on crée un `Rectangle`. De plus, certains arguments sont logiquement groupés ;
il n'est pas utile de devoir forcément spécifier `borderColor` et `isBorderDotted` si on ne veut pas de bordure.
À la place, on peut créer un type `RectangleBuilder` qui permet de définir des groupes de propriétés et qui utilisera une valeur par défaut pour les autres,
avec une méthode `build()` pour créer le `Rectangle` final. Chacune des méthodes définissant des propriétés retourne `this` afin de faciliter l'utilisation du builder.
De plus, on peut réutiliser un `RectangleBuilder` pour créer plusieurs rectangles qui ont presque les mêmes propriétés, par exemple avec seulement la taille qui change.

Exemple :

```java
class Rectangle {
    public Rectangle(int width, int height, int borderThickness, Color borderColor, boolean isBorderDotted, Color backgroundColor, ...) {
       ...
    }
}

class RectangleBuilder {
    // width, height sont requis
    RectangleBuilder(int width, int height) { ... }
    // optionnel, pas de bord par défaut
    RectangleBuilder withBorder(int thickness, Color color, boolean isDotted) { ... ; return this; }
    // optionnel, pas de fond par défaut
    RectangleBuilder withBackgroundColor(Color color) { ... ; return this; }
    // pour créer le rectangle
    Rectangle build() { ... }
}

// Utilisation :
new RectangleBuilder(100, 200)
    .withBorder(10, Colors.BLACK, true)
    .build();
```


# Composite

Un _composite_ est utile quand on veut traiter un groupe d'objets du même genre comme un seul objet, à l'aide d'une classe qui expose la même interface que chacun des objets contenus.
Par exemple, un immeuble avec plusieurs appartements peut exposer une abstraction similaire à celle d'une seule habitation, avec des opérations telles que "obtenir la liste des résidents"
ou "calculer le volume utilisable selon la loi".

Exemple :

```java
interface FileSystemItem {
    String getName();
    boolean containsText(String text);
    // etc.
}

class File implements FileSystemItem {
    // implémentation d'un fichier
}

class Folder implements FileSystemItem {
    Folder(String name, List<FileSystemItem> children) { ... }

    // l'implémentation de "containsText" délégue à ses enfants
    // les enfants peuvent eux-mêmes être des dossiers, sans que le Folder ne doive changer son comportement
}
```


# Decorator

Un _decorator_ est utile quand on veut ajouter une opération à une classe qui est indépendante du fonctionnement principal de la classe, comme un cache des résultats ou
une boucle qui réessaie une opération plusieurs fois.
Au lieu d'ajouter dans la classe du code qui est orthogonal à sa fonction actuelle, et qui de plus devrait être copié/collé dans chaque implémentation de son interface,
on peut la "décorer" avec une classe qui expose la même interface et qui délégue l'appel à la classe décorée tout en ajoutant sa propre logique.

Exemple :

```java
interface HttpClient {
    /** Retourne null en cas d'erreur */
    String get(String url);
}

// implémente le protocole HTTP 1
class Http1Client implements HttpClient { ... }
// implémente le protocole HTTP 2
class Http2Client implements HttpClient { ... }

class RetryingHttpClient implements HttpClient {
    HttpClient wrapped;
    int maxRetries;

    HttpClientImpl(HttpClient wrapped, int maxRetries) {
        this.wrapped = wrapped;
        this.maxRetries = maxRetries;
    }

    @Override
    String get(String url) {
        for (int n = 0; n < maxRetries; n++) {
            String result = wrapped.get(url);
            if (result != null) {
                return result;
            }
        }
        return null;
    }
}

class CachingHttpClient implements HttpClient { ... }

// on peut désormais décorer n'importe quel HttpClient avec un RetryingHttpClient ou un CachingHttpClient
// et comme l'interface est la même, on peut décorer un décorateur, par exemple new CachingHttpClient(new RetryingHttpClient(new Http2Client(...), 5))
```


# Facade

Une _facade_ est utile quand on doit gérer du code dont l'interface est difficile à utiliser, par exemple parce que c'est du code ancien qui n'est plus adapté au contexte actuel,
ou parce que c'est une librairie qui fournit plus de détails que ce dont on a besoin..
C'est un adaptateur qui convertit une interface difficile à utiliser en l'interface désirée, ce qui permet au reste du code d'utiliser l'interface désirée.
Cela peut être utilisé pour du vieux code en attente d'une réécriture : si le nouveau code a la même interface que la facade, le reste du programme ne devra pas changer.

Exemple :

```java
// Classes très détaillées, potentiellement utiles mais tout ce qu'on veut faire c'est lire du XML
class BinaryReader {
    BinaryReader(String path) { ... }
}
class StreamReader {
    StreamReader(BinaryReader reader) { ... }
}
class TextReader {
    TextReader(StreamReader reader) { ... }
}
class XMLOptions { ... }
class XMLReader {
    XMLReader(TextReader reader, XMLOptions options) { ... }
}
class XMLDeserializer {
    XMLDeserializer(XMLReader reader, bool ignoreCase, ...) { ... }
}

// Donc on utilise une facade
class XMLParser {
    XMLParser(String path) {
       // ... crée un BinaryReader, puis un StreamReader, etc., et utilise des paramètres spécifiques pour XMLOptions, ignoreCase, etc.
    }
}
```


# Factory

Une _factory_ est utile quand on veut créer un objet dont le type exact dépend des arguments du "constructeur". Cela n'est pas possible dans un langage comme Java ou Python,
donc on crée à la place une "factory method" qui retourne un type abstrait et instancie le type exact en fonction des arguments.

Exemple :

```java
interface Config { ... }

class XMLConfig implements Config { ... }

class JSONConfig implements Config { ... }

class ConfigFactory {
    static Config getConfig(String fileName) {
        // selon le fichier, crée une XMLConfig ou une JSONConfig
    }
}
```


# Null Object

Un _null object_ est utile quand on veut traiter `null` (`None` en Python) comme un "no-op" pour des opérations, au lieu de devoir ajouter une condition vérifiant `null` à chaque usage.
C'est l'équivalent de retourner une liste vide pour indiquer qu'il n'y a pas de résultats : on peut traiter une liste vide comme toute autre liste, mais les opérations dessus ne font rien.

Exemple :

```java
interface File {
    boolean contains(String text);
}

class RealFile implements File { ... }

class NullFile implements File {
    @Override
    boolean contains(String text) {
        return false;
    }
}

class FileSystem {
    static File getFile(String path) {
        // si le path n'existe pas, au lieu de retourner `null`, retourne une `NullFile`,
        // qui peut être traitée comme une `File`
    }
}
```


# Observer

Un _observer_ est utile quand on veut être notifié d'évènements tels que des changements de valeurs ou des interactions utilisateurs, sans avoir à demander en boucle si un changement a eu lieu.
Par exemple, il serait extrêmement inefficace que l'OS demande continuellement au clavier si l'utilisateur a appuyé sur une touche, puisque 99% du temps ce n'est pas le cas.
À la place, le clavier permet à l'OS de "l'observer" en s'inscrivant pour être notifié de tout changement.

Exemple :

```java
interface ButtonObserver {
    // Typiquement l'objet de source est un argument, afin de pouvoir différencier la source
    // si on s'abonne à plusieurs d'entre elles avec le même observer
    void clicked(Button source);
}

class Button {
    void registerForClicks(ButtonObserver button) {
        // gère une liste de tous les observers, peut aussi fournir une méthode pour enlever un observer
    }
}

// On peut maintenant demander à tout Button de nous notifier dès qu'il est cliqué
// En fait, le Button est probablement lui-même un observer, p.ex. de la souris.
```


# Pool

Une _pool_ est utile quand on a besoin très fréquemment de créer des objets dont la création est trop coûteuse d'un point de vue performance.
Par exemple, allouer de la mémoire peut prendre un moment s'il faut exécuter un appel système pour demander plus de mémoire à l'OS ; donc les librairies standard
gèrent une liste de blocs mémoires vides qui peuvent être utilisés dès qu'il y en a besoin, et "libérer" de la mémoire ne fait que la rendre à cette liste.
Il n'y a donc besoin de demander de la mémoire à l'OS que si la pool est vide.

C'est une pattern assez avancée qui n'est normalement nécessaire que pour des optimisations de performance.

Exemple :

```java
class ExpensiveThing { ... }

class ExpensiveThingPool {
    ExpensiveThing get() { ... }
    // Attention, faire un "release" deux fois avec le même objet est dangereux !
    void release(ExpensiveThing thing) { ... }
}

// Au lieu de `new ExpensiveThing()`, on peut maintenant utiliser une pool
```

# Singleton

Un _singleton_ est une idée généralement mauvaise, mentionnée ici uniquement car elle est courante.
Le singleton est une instance unique d'une classe, stockée dans un champ statique accessible à tous.
Cela "évite" de devoir créer une instance de la classe, mais cela veut dire que tous les utilisateurs du singleton y sont liés,
ce qui rend les tests difficiles.

Il existe des cas avancés dans lesquels un singleton est utile, p.ex. en combinaison avec une _pool_, mais en général c'est à éviter, car c'est une variable globale sous un autre nom.


# Strategy

Une _strategy_ est utile quand une opération doit prendre une décision qui peut varier selon le contexte.
Par exemple, une méthode de tri doit savoir ordonner ses arguments, mais dans différents contexte on peut vouloir différent ordres, par exemple ascendant, descendant, un champ avant l'autre...
La méthode prend donc un argument qui représente cette décision à faire, et délégue ainsi ce choix à ceux qui l'appellent.
Cela permet aussi d'éviter de rendre un module bas niveau, comme le tri, dépendant d'un module haut niveau, comme une définition de classe, car sans la strategy le tri devrait avoir connaissance de cette classe
pour savoir comment la trier.

Exemple :

```java
// (Dé)sérialize des objets
interface Serializer { ... }

// Cache pour objets, qui gère p.ex. l'expiration des objets trop vieux
// Utilise une stratégie "serializer" car selon le contexte on veut potentiellement un format différent, de l'encryption, etc.
class Cache {
    Cache(Serializer serializer) { ... }
}
```


# MVC: Model-View-Controller

Un _controller_ est un objet qui gère les requêtes utilisateurs à l'aide d'un _model_ puis retourne une _view_ à l'utilisateur.
MVC est utile quand l'utilisateur interagit à l'aide d'une requête informatique, comme par exemple une requête HTTP.
MVC permet de séparer le code et de le rendre plus maintenable, par exemple le model peut être testé sans devoir tester l'interface utilisateur avec.

Exemple :

```java
// Model
class WeatherForecast {
    WeatherForecast(...) { ... }

    int getTemperature(...) { ... }
}

// View
// Ici en HTML, mais on pourrait avoir une interface `WeatherView` puis plusieurs types de vues,
// par exemple retourner du HTML aux navigateurs Web mais du JSON si le service est appelé depuis un autre service
// (utilisation du header HTTP "Accept")
class HtmlWeatherView {
    HtmlWeatherView(int temperature, ...) { ... }

    String toString() { ... }
}

// Controller
class WeatherController {
    WeatherForecast forecast;

    WeatherController() {
        this.forecast = new WeatherForecast(...);
    }

    HtmlWeatherView get(...) {
        int temperature = forecast.getTemperature(...);
        return new HtmlWeatherView(temperature, ...);
    }
}

// En général on utilise un framework que l'on configure avec quel chemins HTTP doit utiliser quelle méthode sur quel controller,
// puis qui va créer une instance du bon Controller pour gérer une requête, et donner des paramètres à "get" en fonction de la requête
// Mais on peut aussi le faire à la main :
System.out.println(new WeatherController().get(...).toString());
```


# MVP: Model-View-Presenter

Un _presenter_ est un objet qui est utilisé par une _view_ pour implémenter des opérations, et qui utilise en interne un _model_ pour l'implémentation,
mettant ensuite à jour la view en fonction du résultat.
MVP est utile quand l'utilisateur interagit avec la view, comme une application mobile ou desktop, et a le même but que MVP : rendre le code plus maintenable et testable.

Exemple :

```java
// Model
class WeatherForecast {
    WeatherForecast(...) { ... }

    int getTemperature(...) { ... }
}

// View
// Si on veut plusieurs View pour le même presenter, il faut créer une interface pour, afin que le Presenter puisse l'utiliser
class WeatherView {
    WeatherPresenter presenter;

    WeatherView(WeatherPresenter presenter) {
        this.presenter = presenter;
        presenter.setView(this);
    }

    void onClick(...) { presenter.showTemperature(); }

    void showTemperature(int temperature) { ... }
}

// Presenter
class WeatherPresenter {
    WeatherForecast forecast;
    WeatherView view;

    WeatherPresenter(...) { ... }

    void setView(WeatherView view) { this.view = view; }

    void showTemperature() {
        int temperature = forecast.getTemperature(...);
        view.showTemperature(temperature);
    }
}
```


# MVVM: Model-View-ViewModel

Un _viewmodel_ est une interface utilisateur définie en terme de données, de commandes, et d'évènements de changement des données (pattern _observer_),
qui utilise en interne un _model_ pour implémenter les commandes et qui peut être utilisé par une _view_ pour afficher les données.
MVVM est une évolution de MVP, qui évite de coupler un presenter à la view : la view dépend du viewmodel qui dépend du model, mais
le viewmodel ne dépend pas de la view.

Exemple :

```java
// Model
class WeatherForecast {
    WeatherForecast(...) { ... }

    int getTemperature(...) { ... }
}

// View
// On peut créer plusieurs types de View sans interface, car le ViewModel n'interagit pas directement avec
class WeatherView {
    WeatherViewModel viewModel;

    WeatherView(WeatherViewModel viewModel) {
        this.viewModel = viewModel;
        viewModel.registerForTemperatureChanges(showTemperature);
    }

    void showTemperature() {
        // ... affiche this.viewModel.getTemperature() ...
    }
}

// ViewModel
class WeatherViewModel {
    // Pas de référence à une View !
    // Uniquement un pattern Observer permettant à quiconque (View, mais aussi tests unitaires p.ex.) de s'abonner aux changements

    WeatherForecast forecast;
    int temperature;
    Runnable temperatureCallback;

    // Données
    int getTemperature() { return temperature; }

    // Évènements de changements de données
    void registerForTemperatureChanges(Runnable action) { this.temperatureCallback = temperatureCallback; }

    // Commande
    void updateTemperature() {
        // Cette opération serait asynchrone dans une vraie application,
        // on pourrait aussi avoir une propriété `isLoading` permettant à la View d'afficher une barre de progression, par exemple
        int temperature = forecast.getTemperature(...);
        this.temperature = temperature;
        if (temperatureCallback != null) { temperatureCallback.run(); }
    }
}
```
