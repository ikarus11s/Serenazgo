import time
import random
from data.pueblo_libre_graph import get_graph
from utils.google_sheets import update_sereno_location

def simulate_routes():
    graph = get_graph()
    serenos = get_active_serenos()
    
    while True:
        for sereno in serenos:
            if sereno['estado'] == 'Normal':
                simulate_normal_movement(graph, sereno)
            elif sereno['estado'] == 'Alerta':
                simulate_alert_movement(graph, sereno)
        
        time.sleep(5)  # Esperar 5 segundos antes de la próxima actualización

def simulate_normal_movement(graph, sereno):
    current_node = sereno['current_node']
    neighbors = list(graph.neighbors(current_node))
    next_node = random.choice(neighbors)
    
    new_location = graph.nodes[next_node]['location']
    update_sereno_location(sereno['id'], new_location)
    sereno['current_node'] = next_node

def simulate_alert_movement(graph, sereno):
    if 'target_node' not in sereno:
        return
    
    current_node = sereno['current_node']
    target_node = sereno['target_node']
    
    if current_node == target_node:
        sereno['estado'] = 'Normal'
        del sereno['target_node']
        return
    
    path = nx.shortest_path(graph, current_node, target_node)
    next_node = path[1]
    
    new_location = graph.nodes[next_node]['location']
    update_sereno_location(sereno['id'], new_location)
    sereno['current_node'] = next_node

if __name__ == "__main__":
    simulate_routes()