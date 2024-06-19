# yourapp/utils.py

from math import radians, sin, cos, sqrt, atan2
from .models import BusStop

def calculate_distance(lat1, lon1, lat2, lon2):
    # Haversine formula
    R = 6371.0  # Earth radius in kilometers

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def find_nearest_bus_stop(user_lat, user_lng):
    bus_stops = BusStop.objects.all()
    nearest_stop = None
    min_distance = float('inf')

    for stop in bus_stops:
        distance = calculate_distance(user_lat, user_lng, stop.latitude, stop.longitude)
        if distance < min_distance:
            min_distance = distance
            nearest_stop = stop

    return nearest_stop
