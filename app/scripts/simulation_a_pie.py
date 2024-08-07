import time
import random
from data.pueblo_libre_graph import get_graph
from utils.google_sheets import update_sereno_location, get_serenos_a_pie

def simulate_a_pie():
    graph = get_graph()
    serenos = get_serenos_a_pie()
    
    while True:
        for sereno in serenos:
            if sereno['estado'] == 'Normal':
                move_a_pie(graph, sereno)
            elif sereno['estado'] == 'Alerta':
                move_to_alert(graph, sereno)
        
        time.sleep(30)  # Actualizar cada 30 segundos

def move_a_pie(graph, sereno):
    current_node = sereno['current_node']
    neighbors = list(graph.neighbors(current_node))
    
    next_node = random.choice(neighbors)
    new_location = graph.nodes[next_node]['location']
    update_sereno_location(sereno['id'], new_location)
    sereno['current_node'] = next_node

def move_to_alert(graph, sereno):
    # Similar a move_to_alert en simulation_automovil.py
    pass

if __name__ == "__main__":
    simulate_a_pie()