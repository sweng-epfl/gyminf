import java.util.concurrent.atomic.*;
import java.util.concurrent.*;

public final class Advanced {
    /** Utilise `Server.uploadBatch` pour uploader les textes donnés, ou annule après 2 secondes */
    public static CompletableFuture<Void> upload(String[] texts) {
        // TODO: ajoutez l'annulation à `Server.upload` et utilisez-la ici
        var cancelFlag = new AtomicBoolean(false);
        return CompletableFuture.completedFuture(null);
    }

    /** Adapte `OldServer.download` au modèle `CompletableFuture`,
        et écrit le résultat dans la console en cas de réussite du téléchargement. */
    public static CompletableFuture<Void> download() {
        // TODO (sans modifier OldServer!)
        return CompletableFuture.completedFuture(null);
    }

    /** Réessaye `download` jusqu'à ce qu'il réussisse */
    public static CompletableFuture<Void> reliableDownload() {
        // TODO
        return download();
    }
}
