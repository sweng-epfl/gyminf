import java.util.concurrent.*;
import java.util.*;

import org.junit.jupiter.api.Test;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

final class WeatherTests {
    // N'utilisez pas de sleep!
    // Cependant, comme JUnit veut des tests synchrones, vous aurez besoin d'attendre que les opérations finissent

    @Test
    void todaysWeatherIsSunny() {
        // TODO: Testez que `Weather.today` retourne `"Sunny"`, sans modifier `Weather.today`
    }

    @Test
    void clickingButtonSetsWeatherToSunny() {
        // TODO: Testez que `WeatherView.clickButton` change `WeatherView.weather` en `"Sunny"`, sans modifier `WeatherView`
    }

    @Test
    void weathersContainsYesterdayAndToday() {
        // TODO: Testez que `Weather.printWeathers` retourne `"Today: Sunny"` et `"Yesterday: Cloudy"` dans n'importe quel ordre,
        //       **en modifiant `Weather.printWeathers` autant que nécessaire**
        //       Mais gardez la logique de préfixes dans `Weather`; faites des changements minimaux
    }
}
