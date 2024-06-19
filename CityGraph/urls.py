# citygraph/urls.py

from django.urls import path
from .views import CityGraphView, CityGraphResultView

urlpatterns = [
    path('city_graph/', CityGraphView.as_view(), name='city_graph'),
    path('city_graph/result/', CityGraphResultView.as_view(), name='city_graph_result'),
]
