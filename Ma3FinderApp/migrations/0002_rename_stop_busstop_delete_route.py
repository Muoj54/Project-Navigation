# Generated by Django 5.0.6 on 2024-06-15 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ma3FinderApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stop',
            new_name='BusStop',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]
