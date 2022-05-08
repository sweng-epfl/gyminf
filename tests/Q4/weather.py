from enum import Enum

class Weather(Enum):
    UNKNOWN = 1
    SUN = 2
    RAIN = 3
    SNOW = 4
    ITS_RAINING_MEN = 5

class WeatherService:
    # Crée un WeatherService qui utilisera l'URL de serveur donnée.
    def __init__(self, url):
        self.url = url

    def get_weather(self):
        try:
            text = self.fetch()
        except:
            return Weather.UNKNOWN
        if text == "Sunny":
            return Weather.SUN
        if text == "Rainy":
            return Weather.RAIN
        if text == "Snowy":
            return Weather.SNOW
        if text == "???":
            return Weather.ITS_RAINING_MEN
        return Weather.UNKNOWN

    def fetch(self):
        raise "Pas encore implémenté, oups !"
