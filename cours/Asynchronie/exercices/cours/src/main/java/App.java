public class App {
    public static void main(String[] args) {
        // Pour cette app d'exemple, nous voulons attendre que tout finisse,
        // donc nous utilisns `join()`, mais dans une vraie app ce serait géré par un framework
        // (ou par le langage lui-même, p.ex. en C# la méthode main peut retourner une future)
        // N'UTILISEZ PAS .join() DANS VOTRE CODE SAUF SI VOUS AVEZ UNE TRÈS BONNE RAISON !

        System.out.println("--- Basics ---");

        System.out.println("- Météo aujourd'hui");
        Basics.printTodaysWeather().join();

        System.out.println("- Upload de la météo");
        Basics.uploadTodaysWeather().join();

        System.out.println("- Météo");
        Basics.printSomeWeather().join();

        System.out.println();
        System.out.println("--- Advanced ---");

        System.out.println("- Upload d'un batch de 2");
        Advanced.upload(new String[] { "one", "two" }).join();

        System.out.println("- Upload d'un batch de 20");
        Advanced.upload(new String[] { "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                                       "11", "12", "13", "14", "15", "16", "17", "18", "19", "20" }).join();

        System.out.println("- Download");
        try {
            Advanced.download().join();
        } catch (RuntimeException e) {
            // Évidemment, du vrai code aurait de la gestion d'erreur plus sérieuse
            System.out.println("Erreur de download");
        }

        System.out.println("- Download, de manière fiable");
        try {
            Advanced.reliableDownload().join();
        } catch (RuntimeException e) {
            System.out.println("Erreur de download");
        }
    }
}
