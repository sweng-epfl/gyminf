import java.util.concurrent.atomic.*;
import java.util.concurrent.*;

public final class Server {
    /** Uploade du texte vers un serveur (enfin, fait semblant) */
    public static CompletableFuture<Void> upload(String text) {
        return CompletableFuture.supplyAsync(() -> {
            Utils.sleep(2_000); // faisons semblant de travailler
            System.out.println("Uploadé: " + text);
            return null; // "Void" != "void", il faut quand même retourner quelque chose
        });
    }

    /** Uploade un tableau de texte vers un serveur (enfin, fait semblant) */
    public static CompletableFuture<Void> uploadBatch(String[] texts) {
        // TODO annulation si nécessaire avant chaque étape
        return CompletableFuture.supplyAsync(() -> {
            for (String text : texts) {
                Utils.sleep(500); // faisons semblant de prendre du temps
                System.out.println("Uploadé: " + text);
            }
            return null;
        });
    }
}
