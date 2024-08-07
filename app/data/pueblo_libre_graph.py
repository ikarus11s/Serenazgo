import networkx as nx

def get_graph():
    G = nx.DiGraph()
    
    # Añadir nodos y aristas que representan las calles de Pueblo Libre
    G.add_edge("A", "B", weight=1)
    G.add_edge("B", "C", weight=2)
    # ... más calles
    
    return G