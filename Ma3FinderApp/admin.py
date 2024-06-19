# transport/admin.py

from django.contrib import admin
from .models import BusStop, Destination, BusStopDestination

class BusStopDestinationInline(admin.TabularInline):
    model = BusStopDestination

@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):
    inlines = [BusStopDestinationInline]
    list_display = ('name', 'latitude', 'longitude')
    search_fields = ('name',)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    inlines = [BusStopDestinationInline]

# Remove the following line if you have registered BusStop elsewhere
# admin.site.register(BusStop)
