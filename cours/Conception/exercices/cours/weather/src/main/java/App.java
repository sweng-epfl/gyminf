import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class App {
    // EXERCICE: Transformez cette app basique pour utiliser MVP au lieu de mélanger la logique et l'UI
    //           Rappelez-vous que MVP est "Model-View-Presenter", la View et le Model doivent être entièrement découplés (ils ne savent pas que l'autre existe)
    //           et le Presenter ne doit connaître que l'interface de la View et du Model.
    //           La View gère les entrées utlisateur et les transfère au Presenter, qui en interne utilise le Model pour exécuter des opérations et met à jour la View.
    //           Votre méthode "main" sera quelque chose comme "new Presenter(new RandomModel(), new ConsoleView()).run();"
    //           Vous pouvez exécuter cette app en ligne de commande avec `gradlew.bat run` sur Windows ou `./gradlew run` sur macOS et Linux.

    public static void main(String[] args) {
        System.out.print("Bonjour ! Appuyez sur Entrée pour consulter la météo");
        var scanner = new Scanner(System.in);
        while (true) {
            scanner.nextLine();
            // Dans une vraie app on utiliserait une API, mais utilisons une simulation à la place
            int weather = ThreadLocalRandom.current().nextInt(0, 4);
            if (weather == 0) {
                System.out.println("Météo : Soleil");
            } else if (weather == 1) {
                System.out.println("Météo : Pluie");
            } else {
                System.out.println("Météo : ???");
            }
        }
    }
}
