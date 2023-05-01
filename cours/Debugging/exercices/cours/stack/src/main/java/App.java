import java.util.*;

/**
 * Exercice: Ajoutez du code à IntStack pour attrapper les bugs tôt et corrigez les bugs que vous trouvez.
 *           Gardez à l'esprit que les utilisateurs d'IntStack doivent pouvoir tester les préconditions eux-mêmes.
 *           Ajoutez des méthodes publiques ou privées si nécessaire.
 */
public class App {
    /** Une pile d'entiers, avec une taille maximale. */
    static final class IntStack {
        private int top;
        private final int[] values;

        /** Crée une pile vide avec la taille maximale donnée ; il est interdit d'empiler plus d'éléments que cette taille. */
        public IntStack(int maxSize) {
            top = -1;
            values = new int[maxSize];
        }

        /** Retourne et enlève de la pile l'élément sur le dessus de la pile, ou retourne null si la pile est vide. */
        public Integer pop() {
            Integer value = top >= 0 ? values[top] : null;
            top--;
            return value;
        }

        /** Empile la valeur donnée. */
        public void push(int value) {
            values[top] = value;
            top++;
        }
    }

    public static void main(String[] args) {
        useStack(new IntStack(4));
    }

    // exemple d'utilisation d'IntStack
    private static void useStack(IntStack stack) {
        stack.push(1);
        stack.pop();
        stack.pop();
    }
}
