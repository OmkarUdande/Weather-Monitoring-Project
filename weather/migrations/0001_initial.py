# Generated by Django 5.1 on 2024-10-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('temperature', models.FloatField()),
                ('feels_like', models.FloatField()),
                ('weather_main', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
