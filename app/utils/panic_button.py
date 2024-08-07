from utils.graph_utils import find_nearest_sereno, calculate_route
from utils.google_sheets import update_sereno_status, update_ciudadano_status

def process_panic_button(alert):
    nearest_sereno = find_nearest_sereno(alert['location'])
    
    if nearest_sereno:
        route = calculate_route(nearest_sereno['location'], alert['location'])
        
        update_sereno_status(nearest_sereno['id'], 'Alerta')
        update_ciudadano_status(alert['id'], 'En atención')
        
        create_route_animation(route)
        
        return True
    else:
        return False

def create_route_animation(route):
    # Implementar la creación de la animación GIF de la ruta
    # Esto podría involucrar el uso de bibliotecas como matplotlib o pillow
    pass

def reassign_sereno(alert):
    current_sereno = get_assigned_sereno(alert['id'])
    update_sereno_status(current_sereno['id'], 'Normal')
    
    new_sereno = find_nearest_sereno(alert['location'], exclude=[current_sereno['id']])
    
    if new_sereno:
        route = calculate_route(new_sereno['location'], alert['location'])
        
        update_sereno_status(new_sereno['id'], 'Alerta')
        update_assigned_sereno(alert['id'], new_sereno['id'])
        
        create_route_animation(route)
        
        return True
    else:
        return False