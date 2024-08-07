import random
from data.pueblo_libre_graph import get_graph

def update_sereno_positions():
    graph = get_graph()
    
    # Simular movimiento para cada sereno
    for sereno in get_serenos():
        current_node = sereno['current_node']
        neighbors = list(graph.neighbors(current_node))
        next_node = random.choice(neighbors)
        
        update_sereno_position(sereno, next_node)