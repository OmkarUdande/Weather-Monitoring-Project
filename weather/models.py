from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=50)
    temperature = models.FloatField()
    feels_like = models.FloatField()
    weather_main = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"
