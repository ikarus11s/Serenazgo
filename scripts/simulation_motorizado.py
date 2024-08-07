import time
import random
from data.pueblo_libre_graph import get_graph
from utils.google_sheets import update_sereno_location, get_serenos_motorizado

def simulate_motorizado():
    graph = get_graph()
    serenos = get_serenos_motorizado()
    
    while True:
        for sereno in serenos:
            if sereno['estado'] == 'Normal':
                move_motorizado(graph, sereno)
            elif sereno['estado'] == 'Alerta':
                move_to_alert(graph, sereno)
        
        time.sleep(5)  # Actualizar cada 5 segundos

def move_motorizado(graph, sereno):
    current_node = sereno['current_node']
    neighbors = list(graph.neighbors(current_node))
    valid_neighbors = [n for n in neighbors if graph[current_node][n]['type'] in ['calle', 'avenida']]
    
    if valid_neighbors:
        next_node = random.choice(valid_neighbors)
        new_location = graph.nodes[next_node]['location']
        update_sereno_location(sereno['id'], new_location)
        sereno['current_node'] = next_node

def move_to_alert(graph, sereno):
    # Similar a move_to_alert en simulation_automovil.py
    pass

if __name__ == "__main__":
    simulate_motorizado()