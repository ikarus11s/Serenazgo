import networkx as nx
from data.pueblo_libre_graph import get_graph

def find_nearest_sereno(location):
    graph = get_graph()
    nearest_node = find_nearest_node(graph, location)
    
    serenos = get_active_serenos()
    distances = {}
    
    for sereno in serenos:
        sereno_node = find_nearest_node(graph, sereno['location'])
        path = nx.dijkstra_path(graph, sereno_node, nearest_node)
        distance = nx.dijkstra_path_length(graph, sereno_node, nearest_node)
        travel_time = calculate_travel_time(distance, sereno['velocidad'])
        distances[sereno['id']] = travel_time
    
    nearest_sereno_id = min(distances, key=distances.get)
    return get_sereno_by_id(nearest_sereno_id)

def find_nearest_node(graph, location):
    min_distance = float('inf')
    nearest_node = None
    
    for node in graph.nodes():
        node_location = graph.nodes[node]['location']
        distance = calculate_distance(location, node_location)
        
        if distance < min_distance:
            min_distance = distance
            nearest_node = node
    
    return nearest_node

def calculate_distance(loc1, loc2):
    # Implementar cálculo de distancia entre dos puntos geográficos
    pass

def calculate_travel_time(distance, speed):
    # Convertir velocidad de km/h a m/s
    speed_ms = speed * 1000 / 3600
    return distance / speed_ms