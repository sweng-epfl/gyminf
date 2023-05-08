import java.util.*;

public class App {
    // EXERCICE: Ce code n'est pas modulaire et mélange plein de concepts, ce qui le rend difficile à maintenir.
    //           Modularisez-le !
    //           Réfléchissez à quels modules sont nécessaires, ici des fonctions ou des classes, et comment les organiser.
    //           Vous pouvez commencer par écrire votre fonction "main" idéale, puis par implémenter chaque fonction que main utilise.
    //           Vous pouvez exécuter l'app en ligne de commande avec `gradlew.bat run` sur Windows ou `./gradlew run` sur macOS et Linux.

    public static void main(String[] args) {
    outer:
        while (true) {
            var scanner = new Scanner(System.in);
            // La notation polonaise inversée, ou "postfix", signifie l'opérateur en dernier, p.ex. "1 1 + 2 *" pour "(1 + 1) * 2"
            System.out.print("Calcul à faire ? (en notation polonaise inversée; ou 'sortir') ");
            var text = scanner.nextLine().trim();
            if (text.equals("sortir")) {
                break;
            }
            var parts = text.split(" ");
            var stack = new ArrayDeque<Integer>();
            for (String p : parts) {
                if (p.equals("")) {
                    continue;
                }
                if (p.equals("+")) {
                    stack.push(stack.pop() + stack.pop());
                } else if (p.equals("-")) {
                    var a = stack.pop();
                    var b = stack.pop();
                    stack.push(b - a);
                } else if (p.equals("*")) {
                    stack.push(stack.pop() + stack.pop());
                } else if (p.equals("/")) {
                    var a = stack.pop();
                    var b = stack.pop();
                    stack.push(b / a);
                } else {
                    try {
                        stack.push(Integer.parseInt(p));
                    } catch (NumberFormatException e) {
                        System.out.println("Calcul invalide");
                        continue outer;
                    }
                }
            }
            if (stack.size() == 1) {
                System.out.println(stack.pop());
            } else {
                System.out.println("Calcul invalide");
            }
        }
    }
}
