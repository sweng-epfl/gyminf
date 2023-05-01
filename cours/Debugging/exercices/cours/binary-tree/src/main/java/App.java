import java.util.*;

/**
 * Exercise: Ce code a plusieurs bugs, trouvez-le en exécutant le code et corrigez-les à l'aide d'un debugger
 *           Utilisez votre IDE préféré, ou `jdb` en ligne de commande (mais ce dernier est plus difficile à utiliser)
 */
public class App {
    static final class BinaryTree {
        public final String value;
        public final BinaryTree left;
        public final BinaryTree right;

        public BinaryTree(String v, BinaryTree l, BinaryTree r) {
            value = v;
            left = l;
            right = l;
        }

        public static BinaryTree fromList(List<String> list) {
            int mid = list.size() / 2;
            return new BinaryTree(list.get(mid), fromList(list.subList(0, mid-1)), fromList(list.subList(mid, list.size()-1)));
        }

        public List<String> toList() {
            var result = new ArrayList<String>();
            if (left != null) {
                result.addAll(left.toList());
            }
            result.add(value);
            if (right != null) {
                result.addAll(right.toList());
            }
            return result;
        }
    }

    public static void main(String[] args) {
        var list = List.of("ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU");
        var tree = BinaryTree.fromList(list);
        var newList = tree.toList();
        System.out.println("Liste avant : " + String.join(", ", list));
        System.out.println("Liste après : " + String.join(", ", newList));
    }
}
