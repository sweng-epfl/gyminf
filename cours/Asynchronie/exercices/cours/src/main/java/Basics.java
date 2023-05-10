import java.util.concurrent.*;

public final class Basics {

    // NOTE: L'API CompletableFuture API est documentée sur
    //       https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html
    //       Vous pouvez ignorer les méthodes avec suffixe "async" pour l'instant.

    /** Écrit dans `System.out` la météo de `Weather.today` */
    public static CompletableFuture<Void> printTodaysWeather() {
        // TODO
        return CompletableFuture.completedFuture(null);
    }

    /** Uploade en utilisant `Server.upload` la météo de `Weather.today` */
    public static CompletableFuture<Void> uploadTodaysWeather() {
        // TODO
        return CompletableFuture.completedFuture(null);
    }

    /** Écrit dans `System.out` la météo de soit `Weather.today` soit `Weather.yesterday`,
        celle qui est disponible le plus tôt, préficé de soit "Today: " soit "Yesterday: " respectivement */
    public static CompletableFuture<Void> printSomeWeather() {
        // TODO
        return CompletableFuture.completedFuture(null);
    }
}
