import time
import random
from data.pueblo_libre_graph import get_graph
from utils.google_sheets import update_sereno_location, get_serenos_automovil

def simulate_automovil():
    graph = get_graph()
    serenos = get_serenos_automovil()
    
    while True:
        for sereno in serenos:
            if sereno['estado'] == 'Normal':
                move_automovil(graph, sereno)
            elif sereno['estado'] == 'Alerta':
                move_to_alert(graph, sereno)
        
        time.sleep(5)  # Actualizar cada 5 segundos

def move_automovil(graph, sereno):
    current_node = sereno['current_node']
    neighbors = list(graph.neighbors(current_node))
    valid_neighbors = [n for n in neighbors if graph[current_node][n]['type'] == 'calle']
    
    if valid_neighbors:
        next_node = random.choice(valid_neighbors)
        new_location = graph.nodes[next_node]['location']
        update_sereno_location(sereno['id'], new_location)
        sereno['current_node'] = next_node

def move_to_alert(graph, sereno):
    if 'target_node' not in sereno:
        return
    
    current_node = sereno['current_node']
    target_node = sereno['target_node']
    
    if current_node == target_node:
        sereno['estado'] = 'Normal'
        del sereno['target_node']
        return
    
    path = nx.shortest_path(graph, current_node, target_node, weight='weight')
    next_node = path[1]
    
    new_location = graph.nodes[next_node]['location']
    update_sereno_location(sereno['id'], new_location)
    sereno['current_node'] = next_node

if __name__ == "__main__":
    simulate_automovil()