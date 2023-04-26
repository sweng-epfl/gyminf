import java.io.IOException;

public class RealHttpClient implements HttpClient {
    @Override
    public String get(String url) throws IOException {
        // Oups ! Il semble que vous ne pourriez pas utiliser cette classe dans les tests même si vous le vouliez...
        throw new IOException("No internet connection.");
    }
}
