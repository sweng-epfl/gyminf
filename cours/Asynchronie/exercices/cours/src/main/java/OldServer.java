import java.util.function.*;
import java.util.*;

public final class OldServer {
    private static final Random random = new Random();

    /** Télécharge des données... pas très fiable */
    public static void download(Consumer<String> callback, Consumer<Throwable> errorCallback) {
        new Thread(()-> {
            Utils.sleep(1_000); // faisons semblant de travailler
            if (random.nextInt(5) == 0) { // va probablement échouer !
                callback.accept("Réussite");
            } else {
                errorCallback.accept(new RuntimeException("Échec"));
            }
        }).start();
    }
}
