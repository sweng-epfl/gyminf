import java.util.Objects;
import java.util.function.Function;
import java.util.function.Predicate;

/**
 * Un `Vector3` est un vecteur à 3 composants qui sont chacun des nombres à virgule flottante à 32 bits.
 *
 * <ul>
 *  <li>Créer un vecteur avec `x`, `y` et `z` les assigne aux composants correspondants dans l'espace.</li>
 *  <li>Le vecteur `zero` est celui dont tous les composants sont zéro.</li>
 *  <li>Copier un vecteur crée un nouvel objet avec les mêmes composants.</li>
 *  <li>Calculer le produit scalaire entre deux vecteurs non-nuls retourne la somme du produit des composants.</li>
 *  <li>La longueur d'un vecteur est la racine carrée du produit scalaire du vecteur avec lui-même.</li>
 *  <li>Le produit vectoriel entre deux vecteurs non-nuls `a` et `b` est le vecteur avec `x = a.y * b.z - a.z * b.y`, `y = a.z * b.x - a.x * b.z` et `z = a.x * b.y - a.y * b.x`.</li>
 *  <li>La valeur normalisée d'un vecteur est telle que chaque composant est divisé par la longueur du vecteur ; elle n'est pas définie si la longueur est trop proche de zéro.</li>
 *  <li>Mettre un vecteur à une échelle est fait individuellement par composant.</li>
 *  <li>Deux vecteurs sont égaux si et seulement si leurs composants sont égaux.</li>
 * </ul>
 */
public final class Vector3 {

    public final float x, y, z;

    public Vector3(float x, float y, float z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public static Vector3 zero() {
        return new Vector3(0.0f, 0.0f, 0.0f);
    }

    public Vector3 copy() {
        return new Vector3(this.x, this.y, this.z);
    }

    public boolean isZero() {
        return isAll(f -> f == 0.0f);
    }

    public float dot(Vector3 other) {
        if (other == null) {
            throw new IllegalArgumentException();
        }
        return this.x * other.x + this.y * other.y + this.z * other.z;
    }

    public float length() {
        return (float) Math.sqrt(dot(this));
    }

    public Vector3 cross(Vector3 other) {
        if (other == null) {
            throw new IllegalArgumentException();
        }
        return new Vector3(
                this.y * other.z - this.z * other.y,
                this.z * other.x - this.x * other.z,
                this.x * other.y - this.y * other.x
        );
    }

    public Vector3 normalized() {
        float length = length();
        if (length <= 1e-5) {
            return copy();
        }
        return scaled(1.0f / length);
    }

    public Vector3 scaled(float scalar) {
        return apply(f -> f * scalar);
    }

    @Override
    public String toString() {
        String format;
        if (isAny(f -> f < 1e-2)) {
            format = "%e"; // scientific notation
        } else {
            format = "%f"; // standard floating point notation
        }
        StringBuilder builder = new StringBuilder();
        builder.append("[ ");
        builder.append(String.format(format, this.x));
        builder.append(" ");
        builder.append(String.format(format, this.y));
        builder.append(" ");
        builder.append(String.format(format, this.z));
        builder.append(" ]");
        return builder.toString();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Vector3 vector3 = (Vector3) o;
        return Float.compare(vector3.x, x) == 0 && Float.compare(vector3.y, y) == 0
                && Float.compare(vector3.z, z) == 0;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y, z);
    }

    private boolean isAny(Predicate<Float> predicate) {
        return predicate.test(this.x) || predicate.test(this.y) || predicate.test(this.z);
    }

    private boolean isAll(Predicate<Float> predicate) {
        return predicate.test(this.x) && predicate.test(this.y) && predicate.test(this.z);
    }

    private Vector3 apply(Function<Float, Float> function) {
        var x = function.apply(this.x);
        var y = function.apply(this.y);
        var z = function.apply(this.z);
        return new Vector3(x, y, z);
    }
}
