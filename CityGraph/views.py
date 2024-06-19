from django.shortcuts import render
# citygraph/views.py

import matplotlib.pyplot as plt
import networkx as nx
import heapq
from geopy.geocoders import Nominatim
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from io import BytesIO
import base64
import urllib.parse
from .forms import CityGraphForm

def fetch_city_coordinates(cities: list):
    geolocator = Nominatim(user_agent="city_graph")
    city_coordinates = {}

    for city in cities:
        location = geolocator.geocode(city)
        if location:
            city_coordinates[city] = (location.latitude, location.longitude)
        else:
            print(f"Unable to find coordinates for {city}")
            city_coordinates[city] = (0, 0)  # or some other default coordinates

    return city_coordinates

def read_file(file) -> dict:
    adjacency_list = {}
    lines = file.read().decode().splitlines()
    for line in lines:
        if line.strip() != 'END OF INPUT':
            line = line.strip().split()
            if len(line) == 0: continue
            pointA, pointB, weight = line
            if pointA not in adjacency_list:
                adjacency_list[pointA] = [(pointB, int(weight))]
            else:
                adjacency_list[pointA].append((pointB, int(weight)))
            if pointB not in adjacency_list:
                adjacency_list[pointB] = [(pointA, int(weight))]
            else:
                adjacency_list[pointB].append((pointA, int(weight)))
    return adjacency_list

def uniform_cost_search(adjacency_list: dict, origin: str, destination: str) -> list:
    pq = [(0, origin, [origin])]
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == destination:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, weight in adjacency_list[node]:
                if neighbor not in visited:
                    neighbor_cost = cost + weight
                    heapq.heappush(pq, (neighbor_cost, neighbor, path + [neighbor]))
    return []

def plot_graph(adjacency_list: dict, city_coordinates: dict, path: list = []):
    G = nx.Graph()
    nodes = list(adjacency_list.keys())
    G.add_nodes_from(nodes)
    for node, connections in adjacency_list.items():
        for connection in connections:
            G.add_edge(node, connection[0], weight=connection[1])
    pos = {city: (coords[1], coords[0]) for city, coords in city_coordinates.items()}
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=50)
    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges]
    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    path_edges = [(u, v) for (u, v) in path_edges if G.has_edge(u, v)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')
    nx.draw_networkx_edges(G, pos, edgelist=set(edges) - set(path_edges), width=1, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=5, font_family='sans-serif')
    plt.title("Coordinate-based Uniform-Cost Search")
    plt.axis('off')
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri

def output_path(adjacency_list: dict, path: list):
    distance = 0
    for i, node in enumerate(path):
        if i == len(path) - 1:
            break
        connections = adjacency_list[node]
        for connection in connections:
            name = connection[0]
            if name == path[i+1]:
                distance += connection[1]
                break
    if len(path) == 0:
        return {"distance": "infinity", "route": "none"}
    route = []
    if len(path) == 1:
        route.append(f"{path[0]} to {path[0]}, 0 km")
        return {"distance": distance, "route": route}
    for i, node in enumerate(path):
        if i == len(path) - 1:
            break
        connections = adjacency_list[node]
        dist = 0
        for connection in connections:
            name = connection[0]
            if name == path[i+1]:
                dist = connection[1]
                break
        route.append(f"{node} to {path[i+1]}, {dist} km")
    return {"distance": distance, "route": route}

class CityGraphView(FormView):
    template_name = 'city_graph_form.html'
    form_class = CityGraphForm
    success_url = '/city_graph/'

    def form_valid(self, form):
        file = form.cleaned_data['file']
        origin = form.cleaned_data['origin']
        destination = form.cleaned_data['destination']
        adjacency_list = read_file(file)
        city_coordinates = fetch_city_coordinates(list(adjacency_list.keys()))
        solution_path = uniform_cost_search(adjacency_list, origin, destination)
        path_info = output_path(adjacency_list, solution_path)
        graph_image = plot_graph(adjacency_list, city_coordinates, solution_path)
        return render(self.request, 'city_graph.html', {'path_info': path_info, 'graph_image': graph_image})

class CityGraphResultView(TemplateView):
    template_name = 'city_graph.html'

# Create your views here.
