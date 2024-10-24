from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler  


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'

    def ready(self):
        from  .views import fetch_weather

        scheduler = BackgroundScheduler()

        # Define the cities
        cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad']

        #  run every 5 minutes for each city
        for city in cities:
            scheduler.add_job(fetch_weather, 'interval', minutes=5, args=[city])

        scheduler.start()
