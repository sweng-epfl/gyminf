import java.util.concurrent.*;
import java.util.function.*;

public final class Weather {
    /** Obtient la météo pour aujourd'hui */
    public static CompletableFuture<String> today() {
        return CompletableFuture.supplyAsync(() -> {
            Utils.sleep(2_000); // ça prend du temps !
            return "Sunny";
        });
    }

    /** Obtient la météo pour hier */
    public static CompletableFuture<String> yesterday() {
        // On sait déjà quel temps il faisait hier, donc pas de délai
        return CompletableFuture.completedFuture("Cloudy");
    }

    /** Imprime la météo pour hier et aujourd'hui, dans un ordre non défini. */
    public static void printWeathers() {
        today().thenApply(a -> "Today: " + a)
               .thenAccept(System.out::println);
        yesterday().thenApply(a -> "Yesterday: " + a)
                   .thenAccept(System.out::println);
    }
}
