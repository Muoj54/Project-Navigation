    # routes/urls.py
from django.contrib import admin
from django.urls import path
from .views import HomeScreenView, EnterDestinationView, TransportationLocationView, RouteView, MapboxGeocodingProxyView, search_destinations
from . import views

urlpatterns = [

        # path('admin/', admin.site.urls),
    path('', HomeScreenView.as_view(), name='home'),
    path('', EnterDestinationView.as_view(), name='home'),
    path('routes/', EnterDestinationView.as_view(), name='enter_destination'),
    path('transportation_location/', TransportationLocationView.as_view(), name='transportation_location'),
    # path('transportation_location/<str:destination_name>/', TransportationLocationView.as_view(), name='transportation_location'),
    path('geocode/', MapboxGeocodingProxyView.as_view(), name='mapbox-geocode'),
    path('routes/', RouteView.as_view(), name='route_view'),
    path('search_destinations/', search_destinations, name='search_destinations'),
    path('get_location_data/', views.get_location_data, name='get_location_data'),
    
        # path('Ma3FinderApp/', route_view, name='route_view'),
        # path('openrouteservice_proxy/', OpenRouteServiceProxyView.as_view(), name='openrouteservice_proxy'),
        
        # path('', EnterDestinationView.as_view(), name='enter_destination'),
        # path('transportation_location/', TransportationLocationView.as_view(), name='transportation_location'),
        # path('routes/', EnterDestinationView.as_view(), name='route_view'),
        # path(',', RouteView.as_view(), name='route_view'),
        # path('routes/', RouteView.as_view(), name='route_view'),
        # path('openrouteservice_proxy/', OpenRouteServiceProxyView.as_view(), name='openrouteservice_proxy'),
        # path('map/', MapView.as_view(), name='map'),
        # path('Ma3FinderApp/', route_view, name='route_view'),

        ]