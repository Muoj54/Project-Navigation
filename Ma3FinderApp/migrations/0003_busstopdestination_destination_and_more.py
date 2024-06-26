# Generated by Django 5.0.6 on 2024-06-15 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ma3FinderApp', '0002_rename_stop_busstop_delete_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusStopDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ma3FinderApp.busstop')),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bus_stops', models.ManyToManyField(through='Ma3FinderApp.BusStopDestination', to='Ma3FinderApp.busstop')),
            ],
        ),
        migrations.AddField(
            model_name='busstopdestination',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ma3FinderApp.destination'),
        ),
        migrations.AlterUniqueTogether(
            name='busstopdestination',
            unique_together={('bus_stop', 'destination')},
        ),
    ]
