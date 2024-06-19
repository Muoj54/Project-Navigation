# yourapp/management/commands/populate_data.py

from django.core.management.base import BaseCommand
from Ma3FinderApp.models import Stop, Route


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Add stops
        stop_a = Stop.objects.create(name='Stop A', latitude=-1.2848354, longitude=36.8260022)
        stop_b = Stop.objects.create(name='Stop B', latitude=-1.286263,  longitude=36.829590)
        stop_c = Stop.objects.create(name='Stop C', latitude=-1.264857, longitude=36.8998021)
        
        # Add routes
        Route.objects.create(name='Route 1', start_stop=stop_a, end_stop=stop_b)
        Route.objects.create(name='Route 2', start_stop=stop_b, end_stop=stop_c)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
