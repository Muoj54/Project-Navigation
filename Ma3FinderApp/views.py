from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from django.urls import reverse
import requests
# import folium
# from geopy.geocoders import Nominatim
# # import geopy.geocoders as geocoders
# from geopy.exc import GeocoderTimedOut
# import openrouteservice as ors
import requests
from Ma3FinderApp.models import BusStop, BusStopDestination, Destination
from math import sqrt
from .utils import find_nearest_bus_stop
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from Ma3FinderApp.models import Destination, BusStop, BusStopDestination
import requests
from django.http import HttpResponseServerError
from django.core.serializers.json import DjangoJSONEncoder


# client = ors.Client(key='5b3ce3597851110001cf6248d155096955ff4efa8969d56e02eae948')


# client = ors.Client(key='5b3ce3597851110001cf6248d155096955ff4efa8969d56e02eae948')

# timeout = 10

# try:
#     location = g.geocode(TransportationLocationView) # type: ignore
#     # Process successful geocoding results (access location.latitude, location.longitude, etc.)
# except geopy.exc.GeocoderUnavailable as e: # type: ignore
#     # Handle geocoding failure gracefully
#     print(f"Geocoding failed: {e}")
#     # Optionally, provide a fallback mechanism or display an error message to the user
# except Exception as e:  # Catch other potential exceptions
#     # Handle unexpected errors
#     print(f"An error occurred: {e}")


class HomeScreenView(TemplateView):
    template_name = 'home.html'

    # def dispatch(self, request, *args, **kwargs):
    #     print(request.headers)
    #     return super().dispatch(request, *args, **kwargs)


# class MapView(TemplateView):
#     def get(self, request):
#             m = folium.Map()
#             m = m._repr_html_()
#             context = {
#                 'map': m,
#             }
#             return render(request, 'base.html', context)
         
             

class EnterDestinationView(TemplateView):
    template_name = 'enter_destination.html'

    def get(self, request):
        destinations = Destination.objects.all()
        return render(request, self.template_name, {'destinations': destinations})

    def post(self, request):
        destination_id = request.POST.get('destination')
        if destination_id:
            return redirect(reverse('transportation_location', kwargs={'destination_id': destination_id}))
        destinations = Destination.objects.all()
        return render(request, self.template_name, {'destinations': destinations, 'error': 'Please select a destination'})

    # def post(self, request, *args, **kwargs):
    #     destination = request.POST.get('destination','')
    #     if destination:
    #         return redirect(reverse('transportation_location', kwargs={'destination': destination}))
    #     # Process the destination (e.g., find transportation location)
    #     # Redirect to transportation location view with destination as parameter
    #     # return redirect('transportation_location', destination=destination)
    #     else:
    #         return HttpResponse('Destination not found!')

# class TransportationLocationView(TemplateView):
#     template_name = 'transportation_location.html'

#     def get(self, request, *args, **kwargs):
#         destination = request.GET.get('destination')
#         user_lat = request.GET.get('lat')
#         user_lng = request.GET.get('lng')

#         if user_lat and user_lng:
#             user_location = [float(user_lat), float(user_lng)]
#             destination_location = self.get_location_from_address(destination)

#             if not destination_location:
#                 return self.render_to_response({'error': 'Could not find the destination location'})

#             folium_map = folium.Map(location=user_location, zoom_start=12)
#             folium.Marker(user_location, popup='Your Location', icon=folium.Icon(color='blue')).add_to(folium_map)
#             folium.Marker(destination_location, popup=destination, icon=folium.Icon(color='red')).add_to(folium_map)
#             folium.PolyLine([user_location, destination_location], color='green', weight=2.5, opacity=1).add_to(folium_map)

#             map_html = folium_map._repr_html_()
#             return self.render_to_response({'map': map_html, 'destination': destination})

#         return self.render_to_response({'error': 'Could not get user location'})

#     def get_location_from_address(self, address):
#         geolocator = Nominatim(user_agent="ma3finder")
#         try:
#             location = geolocator.geocode(address)
#             if location:
#                 return [location.latitude, location.longitude]
#         except GeocoderTimedOut:
#             return None
#         return None

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['lat'] = self.request.GET.get('lat')
#         context['lng'] = self.request.GET.get('lng')
#         context['destination'] = self.request.GET.get('destination')
#         return context



    # def get(self, request, *args, **kwargs):
    #     destination = request.GET.get('destination')
    #     user_lat = request.GET.get('lat')
    #     user_lng = request.GET.get('lng')

    #     if user_lat and user_lng:
    #         user_location = [float(user_lat), float(user_lng)]
    #         destination_location = self.get_location_from_address(destination)

    #         if not destination_location:
    #             return self.render_to_response({'error': 'Could not find the destination location'})

    #         folium_map = folium.Map(location=user_location, zoom_start=12)
    #         folium.Marker(user_location, popup='Your Location', icon=folium.Icon(color='blue')).add_to(folium_map)
    #         folium.Marker(destination_location, popup=destination, icon=folium.Icon(color='red')).add_to(folium_map)
    #         folium.PolyLine([user_location, destination_location], color='green', weight=2.5, opacity=1).add_to(folium_map)

    #         map_html = folium_map._repr_html_()
    #         return self.render_to_response({'map': map_html, 'destination': destination})

    #     return self.render_to_response({'error': 'Could not get user location'})

    # def get_location_from_address(self, address):
    #     geolocator = Nominatim(user_agent="ma3finder")
    #     try:
    #         location = geolocator.geocode(address)
    #         if location:
    #             return [location.latitude, location.longitude]
    #     except GeocoderTimedOut:
    #         return None
    #     return None

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['lat'] = self.request.GET.get('lat')
    #     context['lng'] = self.request.GET.get('lng')
    #     context['destination'] = self.request.GET.get('destination')
    #     return context






    

    # def get(self, request, destination, *args, **kwargs):
    #     user_lat = request.GET.get('lat')
    #     user_lng = request.GET.get('lng')

    #     if user_lat and user_lng:
    #         user_location = [float(user_lat), float(user_lng)]
    #         destination_location = self.get_location_from_address(destination)

    #         if not destination_location:
    #             return self.render_to_response({'error': 'Could not find the destination location'})

    #         folium_map = folium.Map(location=user_location, zoom_start=12)
    #         folium.Marker(user_location, popup='Your Location', icon=folium.Icon(color='blue')).add_to(folium_map)
    #         folium.Marker(destination_location, popup=destination, icon=folium.Icon(color='red')).add_to(folium_map)
    #         folium.PolyLine([user_location, destination_location], color='green', weight=2.5, opacity=1).add_to(folium_map)

    #         map_html = folium_map._repr_html_()
    #         return self.render_to_response({'map': map_html, 'destination': destination})

    #     return self.render_to_response({'error': 'Could not get user location'})

    # def get_location_from_address(self, address):
    #     geolocator = Nominatim(user_agent="ma3finder")
    #     try:
    #         location = geolocator.geocode(address)
    #         if location:
    #             return [location.latitude, location.longitude]
    #     except GeocoderTimedOut:
    #         return None
    #     return None
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['lat'] = self.request.GET.get('lat')
    #     context['lng'] = self.request.GET.get('lng')
    #     context['destination'] = self.request.GET.get('destination')
    #     return context

class MapboxGeocodingProxyView(TemplateView):
    def get(self, request, *args, **kwargs):
        access_token = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA'
        text = request.GET.get('text')
        url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{text}.json?access_token={access_token}'
        response = requests.get(url)
        return JsonResponse(response.json())









    # def get(self, request, destination, *args, **kwargs):
    #     user_lat = request.GET.get('lat', None)
    #     user_lng = request.GET.get('lng', None)
        
    #     if user_lat is not None and user_lng is not None:
    #         user_location = [float(user_lat), float(user_lng)]
    #         destination_location = self.get_location_from_address(destination)
            
    #         if not destination_location:
    #             return self.render_to_response({'error': 'Could not find the destination location'})
            
    #         folium_map = folium.Map(location=user_location, zoom_start=12)
    #         folium.Marker(user_location, popup='Your Location', icon=folium.Icon(color='blue')).add_to(folium_map)
    #         folium.Marker(destination_location, popup=destination, icon=folium.Icon(color='red')).add_to(folium_map)

    #         folium.PolyLine([user_location, destination_location], color='green', weight=2.5, opacity=1).add_to(folium_map)

    #         map_html = folium_map._repr_html_()
    #         return self.render_to_response({'map': map_html, 'destination': destination})

    #     return self.render_to_response({'error': 'Could not get user location'})

    # def get_location_from_address(self, address):
    #     geolocator = Nominatim(user_agent="ma3finder")
    #     try:
    #         location = geolocator.geocode(address)
    #         if location:
    #             return [location.latitude, location.longitude]
    #     except GeocoderTimedOut:
    #         return None
    #     return None











    # def get(self, request, destination, *args, **kwargs):
    #     user_lat = request.GET.get('lat', None)
    #     user_lng = request.GET.get('lng', None)
        
    #     if user_lat is not None and user_lng is not None:
    #         user_location = [float(user_lat), float(user_lng)]
    #         # For example purposes, let's assume the destination coordinates
    #         destination_location = [1.2921, 36.8219]  # Coordinates for Nairobi

    #         folium_map = folium.Map(location=user_location, zoom_start=12)
    #         folium.Marker(user_location, popup='Your Location', icon=folium.Icon(color='blue')).add_to(folium_map)
    #         folium.Marker(destination_location, popup=destination, icon=folium.Icon(color='red')).add_to(folium_map)
            
    #         # Draw a line between user location and destination
    #         folium.PolyLine([user_location, destination_location], color='green', weight=2.5, opacity=1).add_to(folium_map)
            
    #         map_html = folium_map._repr_html_()
    #         return self.render_to_response({'map': map_html, 'destination': destination})

    #     return self.render_to_response({'error': 'Could not get user location'})




    # def get(self, request, destination, *args, **kwargs):
    #     import folium
    #     map_center = [1.2921, 36.8219]  # Coordinates for Nairobi as an example
    #     folium_map = folium.Map(location=map_center, zoom_start=12)
    #     folium.Marker(map_center, popup=destination).add_to(folium_map)
    #     map_html = folium_map._repr_html_()
    #     return self.render_to_response({'map': map_html, 'destination': destination})
    

    # def get(self, request, destination):
    #     # Perform any processing needed for the destination, e.g., geocoding
    #     # Here we assume destination is a string representing the place

    #     # For the sake of this example, we'll use a fixed latitude and longitude
    #     start_lat, start_lng = -1.2921, 36.8219  # Nairobi coordinates

    #     # Create a folium map centered around the destination
    #     folium_map = folium.Map(location=[start_lat, start_lng], zoom_start=13)
    #     folium.Marker([start_lat, start_lng], popup=destination).add_to(folium_map)

    #     # Convert the map to HTML
    #     map_html = folium_map._repr_html_()

    #     return render(request, self.template_name, {'map_html': map_html, 'destination': destination})


    

    # def get_context_data(self, **kwargs):
    #     destination = kwargs['destination']
    #     # Logic to find transportation location based on the destination
    #     # For example, you can fetch the location from a database or API
    #     # Replace 'transportation_location' with the actual location data
    #     transportation_location = 'Transportation location for ' + destination
    #     context = super().get_context_data(**kwargs)
    #     context['destination'] = destination
    #     context['transportation_location'] = transportation_location
    #     return context
    # def index(request):
    #     m = folium.Map()
    #     m = m._repr_html_()
    #     context = {
    #         'map': m,
    #     }
    #     return render(request, 'transportation_location.html')
class RouteView(TemplateView):
    template_name = 'trasnsportation_location.html'

    def get_route(self, start_lng, start_lat, end_lng, end_lat, access_token, profile='mapbox/driving'):
        url = f'https://api.mapbox.com/directions/v5/{profile}/{start_lng},{start_lat};{end_lng},{end_lat}'
        params = {
            'access_token': access_token,
            'geometries': 'geojson',
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        start_lng = kwargs.get('start_lng')
        start_lat = kwargs.get('start_lat')
        end_lng = kwargs.get('end_lng')
        end_lat = kwargs.get('end_lat')

        if start_lng and start_lat and end_lng and end_lat:
            access_token = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA'
            route_data = self.get_route(start_lng, start_lat, end_lng, end_lat, access_token)
            context['route_data'] = route_data
            context['start_lat'] = start_lat
            context['start_lng'] = start_lng
            context['end_lat'] = end_lat
            context['end_lng'] = end_lng

        return context

# timeout = 10

# try:
#     location = g.geocode(TransportationLocationView) # type: ignore
#     # Process successful geocoding results (access location.latitude, location.longitude, etc.)
# except geopy.exc.GeocoderUnavailable as e: # type: ignore
#     # Handle geocoding failure gracefully
#     print(f"Geocoding failed: {e}")
#     # Optionally, provide a fallback mechanism or display an error message to the user
# except Exception as e:  # Catch other potential exceptions
#     # Handle unexpected errors
#     print(f"An error occurred: {e}")
# class TransportationLocationView(TemplateView):
#     template_name = "transportation_location.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_lat = float(self.request.GET.get('lat'))
#         user_lng = float(self.request.GET.get('lng'))
#         destination_name = self.request.GET.get('destination')
#         destination_lat, destination_lon = self.geocode(destination_name)
        
#         nearest_stop = find_nearest_bus_stop(user_lat, user_lng)
#         directions_to_stop = self.get_directions(user_lat, user_lng, nearest_stop.latitude, nearest_stop.longitude)
#         directions_from_stop_to_destination = self.get_directions(nearest_stop.latitude, nearest_stop.longitude, destination_lat, destination_lon)
        
#         context['nearest_stop'] = nearest_stop
#         context['directions_to_stop'] = directions_to_stop
#         context['directions_from_stop_to_destination'] = directions_from_stop_to_destination
#         return context

#     def geocode(self, destination):
#         # Placeholder function, replace with actual geocoding logic
#         if destination.lower() == 'thika':
#             return -1.0332, 37.0693  # Coordinates for Thika, Kenya
#         else:
#             return -1.2571334, 36.8969799  # Fallback coordinates

#     def get_directions(self, start_lat, start_lng, end_lat, end_lng):
#         access_token = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA'
#         url = f'https://api.mapbox.com/directions/v5/mapbox/driving/{start_lng},{start_lat};{end_lng},{end_lat}?geometries=geojson&access_token={access_token}'
#         response = requests.get(url)
#         directions = response.json()
#         return directions
# class TransportationLocationView(TemplateView):
#     template_name = 'transportation_location.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         lat = self.request.GET.get('lat')
#         lng = self.request.GET.get('lng')
#         destination_name = self.request.GET.get('destination')

#         if lat and lng and destination_name:
#             bus_stops = BusStop.objects.all()
#             context['bus_stops'] = bus_stops

#             try:
#                 destination = Destination.objects.get(name=destination_name)
#                 bus_stop_destinations = BusStopDestination.objects.filter(destination=destination)
#                 context['bus_stop_destinations'] = bus_stop_destinations
#             except Destination.DoesNotExist:
#                 context['bus_stop_destinations'] = []

#             context['start_lat'] = lat
#             context['start_lng'] = lng
#             context['destination'] = destination_name
#             context['mapbox_access_token'] = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA'
#         else:
#             context['bus_stops'] = []
#             context['bus_stop_destinations'] = []

#         return context    
#     # This is the view taht works. DO NOT CHANGE IT!


# class TransportationLocationView(TemplateView):
#     template_name = 'transportation_location.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         lat = self.request.GET.get('lat')
#         lng = self.request.GET.get('lng')
#         destination_name = self.request.GET.get('destination')

#         if lat and lng and destination_name:
#             bus_stops = BusStop.objects.all()
#             context['bus_stops'] = list(bus_stops.values('name', 'latitude', 'longitude'))

#             destination = get_object_or_404(Destination, name=destination_name)
#             bus_stop_destinations = BusStopDestination.objects.filter(destination=destination)
#             context['bus_stop_destinations'] = list(bus_stop_destinations.values('bus_stop__name', 'bus_stop__latitude', 'bus_stop__longitude'))
            
#             context['start_lat'] = lat
#             context['start_lng'] = lng
#             context['destination'] = destination_name
#             context['mapbox_access_token'] = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA'
#         else:
#             context['bus_stops'] = []
#             context['bus_stop_destinations'] = []

#         return context
class TransportationLocationView(TemplateView):
    template_name = 'transportation_location.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        lat = self.request.GET.get('lat')
        lng = self.request.GET.get('lng')
        destination_name = self.request.GET.get('destination')

        # Debugging logs
        print(f"Latitude: {lat}")
        print(f"Longitude: {lng}")
        print(f"Destination Name: {destination_name}")

        if lat and lng and destination_name:
            try:
                destination = get_object_or_404(Destination, name=destination_name)
                bus_stops = destination.bus_stops.all()

                # Debugging logs
                print(f"Bus Stops for {destination_name}: {bus_stops}")

                context['bus_stops'] = list(bus_stops.values('name', 'latitude', 'longitude'))
                context['start_lat'] = lat
                context['start_lng'] = lng
                context['destination'] = destination.name
                context['mapbox_access_token'] = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA'
            except Destination.DoesNotExist:
                print(f"Destination {destination_name} does not exist")
                context['bus_stops'] = []
                context['start_lat'] = None
                context['start_lng'] = None
                context['destination'] = None
                context['mapbox_access_token'] = None
        else:
            context['bus_stops'] = []
            context['start_lat'] = None
            context['start_lng'] = None
            context['destination'] = None
            context['mapbox_access_token'] = None

        return context


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     destination_name = kwargs.get('destination_name')

    #     if destination_name:
    #         try:
    #             destination = get_object_or_404(Destination, name=destination_name)
    #             # Simulate lat and lng being fetched from JavaScript
    #             lat = self.request.GET.get('lat')
    #             lng = self.request.GET.get('lng')

    #             if lat and lng:
    #                 # Process using the provided lat and lng
    #                 bus_stops = destination.bus_stops.all()

    #                 context['bus_stops'] = list(bus_stops.values('name', 'latitude', 'longitude'))
    #                 context['start_lat'] = lat
    #                 context['start_lng'] = lng
    #                 context['destination'] = destination.name
    #                 context['mapbox_access_token'] = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA'  # Replace with your Mapbox token
    #             else:
    #                 # No lat and lng provided, handle this case
    #                 context['bus_stops'] = []
    #                 context['start_lat'] = None
    #                 context['start_lng'] = None
    #                 context['destination'] = destination.name
    #                 context['mapbox_access_token'] = None
    #         except Destination.DoesNotExist:
    #             context['bus_stops'] = []
    #             context['start_lat'] = None
    #             context['start_lng'] = None
    #             context['destination'] = None
    #             context['mapbox_access_token'] = None
    #     else:
    #         context['bus_stops'] = []
    #         context['start_lat'] = None
    #         context['start_lng'] = None
    #         context['destination'] = None
    #         context['mapbox_access_token'] = None

    #     return context

        # Determine destination based on provided parameters
        # if destination_name:
        #     destination = get_object_or_404(Destination, name=destination_name)
        # elif destination_id:
        #     destination = get_object_or_404(Destination, id=destination_id)
        # else:
        #     destination = None

        # # Populate context based on availability of destination
        # if destination:
        #     context['destination'] = destination.name

        #     if lat and lng:
        #         bus_stops = destination.bus_stops.all()
        #         context['bus_stops'] = list(bus_stops.values('name', 'latitude', 'longitude'))
        #         context['start_lat'] = lat
        #         context['start_lng'] = lng
        #     else:
        #         context['bus_stops'] = []
        #         context['start_lat'] = None
        #         context['start_lng'] = None

        #     context['mapbox_access_token'] = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA'
        # else:
        #     context['bus_stops'] = []
        #     context['start_lat'] = None
        #     context['start_lng'] = None
        #     context['destination'] = None
        #     context['mapbox_access_token'] = None

        # return context
    
def transportation_location_view(request, destination_name):
    destination = get_object_or_404(Destination, name=destination_name)
    bus_stops = list(destination.bus_stops.values('name', 'latitude', 'longitude'))

    # Debug logs
    print('Destination:', destination.name)
    print('Bus Stops:', bus_stops)

    context = {
        'start_lat': destination.bus_stops.first().latitude if destination.bus_stops.exists() else None,
        'start_lng': destination.bus_stops.first().longitude if destination.bus_stops.exists() else None,
        'destination': destination.name,
        'bus_stops': bus_stops
    }

    return render(request, 'transportation_location.html', context)
    
def search_destinations(request):
    query = request.GET.get('q', '')
    if query:
        destinations = Destination.objects.filter(name__icontains=query).values('name')
        return JsonResponse(list(destinations), safe=False)
    return JsonResponse([], safe=False)
# def transportation_location(request):
#     # Retrieve data from your models
#     destination_name = " "  # Replace with actual destination name
#     destination = Destination.objects.get(name=destination_name)  # Assuming you have a specific destination
#     bus_stops = destination.bus_stops.all()  # Get all bus stops associated with the destination

#     # Prepare data to pass to template
#     context = {
#         'destination': destination_name,
#         'start_lat': 0,  # Replace with actual starting point latitude
#         'start_lng': 0,  # Replace with actual starting point longitude
#         'bus_stops': list(bus_stops.values('name', 'latitude', 'longitude')),  # Convert queryset to list of dicts
#     }

#     return render(request, 'transportation_location.html', context)
def transportation_location(request):
    # Assuming the destination name is passed as a query parameter named "destination"
    # destination_name = request.GET.get("destination", "Karen")  # Default to "Karen" if not provided
    # destination = get_object_or_404(Destination, name=destination_name)
    # bus_stops = destination.bus_stops.all()
    destination_name = " "  # Replace with actual destination name
    destination = Destination.objects.get(name=destination_name)  # Assuming you have a specific destination
    bus_stops = destination.bus_stops.all()  # Get all bus stops associated with the destination
    
    location_data = {
        "destination": destination.name,
        "bus_stops": list(bus_stops.values('name', 'latitude', 'longitude'))
    }
    
    context = {
        "location_data": json.dumps(location_data, cls=DjangoJSONEncoder),
        "destination": destination.name,
        "bus_stops": json.dumps(list(bus_stops.values('name', 'latitude', 'longitude')), cls=DjangoJSONEncoder)
    }
    return render(request, 'transportation_location.html', context)



def destination_list_view(request):
    # Example user location (replace with actual user location logic)
    user_lat = request.GET.get('lat', '0')
    user_lng = request.GET.get('lng', '0')

    destinations = Destination.objects.all()
    context = {
        'destinations': destinations,
        'user_lat': user_lat,
        'user_lng': user_lng,
    }
    return render(request, 'destination_list.html', context)
def get_location_data(request):
    destination_name = request.GET.get('destination')
    destination = get_object_or_404(Destination, name=destination_name)
    
    bus_stops = destination.bus_stops.all()
    bus_stops_data = [{
        'name': stop.name,
        'latitude': stop.latitude,
        'longitude': stop.longitude
    } for stop in bus_stops]
    
    data = {
        'destination': destination.name,
        'bus_stops': bus_stops_data
    }
    
    return JsonResponse(data)