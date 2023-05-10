public final class Utils {
    /** Dort pour le nombre donné de millisecondes */
    public static void sleep(int milliseconds) {
        try {
            Thread.sleep(milliseconds);
        } catch (InterruptedException e) {
            throw new AssertionError("Ne devrait jamais arriver dans ce code d'exemple", e);
        }
    }
}
