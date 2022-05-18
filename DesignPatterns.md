# Design patterns courantes

Ce document contient une liste de design patterns courantes, avec leur contexte, et un exemple.


# Adapter

Un _adapter_ est nécessaire quand on a un objet de type `X` à disposition mais que l'interface que l'on veut utiliser n'accepte que des objets de type `X'`,
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
    private final BgraColor wrapped;

    public BgraToArgbAdapter(BgraColor wrapped) {
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
    public RectangleBuilder(int width, int height) { ... }
    // optionnel, pas de bord par défaut
    public RectangleBuilder withBorder(int thickness, Color color, boolean isDotted) { ... ; return this; }
    // optionnel, pas de fond par défaut
    public RectangleBuilder withBackgroundColor(Color color) { ... ; return this; }
    // pour créer le rectangle
    public Rectangle build() { ... }
}

// Utilisation :
new RectangleBuilder(100, 200)
    .withBorder(10, Colors.BLACK, true)
    .build();
```

# Composite

TODO

# Decorator

# Facade

# Factory

# Null Object

# Observer

# Pool

# Singleton

# Strategy
