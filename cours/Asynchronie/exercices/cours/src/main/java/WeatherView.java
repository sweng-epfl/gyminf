public final class WeatherView {
    private static Runnable callback;
    private static String weather;

    /** Obtient la météo à afficher. */
    public static String weather() {
        return weather;
    }

    /** Définit un callback pour tester le clic */
    public static void setCallback(Runnable callback) {
        WeatherView.callback = callback;
    }

    // Prétendons qu'il y a un framework comme Android qui utilise cette méthode et a besoin d'un type de retour `void` et de zéro paramètres
    public static void clickButton() {
        Weather.today()
               .thenAccept(w -> {
                   weather = w;
                   if (callback != null) {
                       callback.run();
                   }
               });
    }
}
