import folium
from streamlit_folium import folium_static
from utils.google_sheets import get_serenos, get_ciudadanos_alerta

def display_map():
    m = folium.Map(location=[-12.0789, -77.0842], zoom_start=14)
    
    add_sereno_markers(m)
    add_ciudadano_markers(m)
    add_ruta_markers(m)
    
    folium_static(m)

def add_sereno_markers(m):
    serenos = get_serenos()
    for sereno in serenos:
        color = 'blue' if sereno['estado'] == 'Normal' else 'red'
        icon = create_sereno_icon(sereno['forma_patrullaje'], color)
        
        popup = folium.Popup(f"DNI: {sereno['dni']}", max_width=300)
        folium.Marker(
            [sereno['latitud'], sereno['longitud']],
            popup=popup,
            icon=icon
        ).add_to(m)

def add_ciudadano_markers(m):
    ciudadanos = get_ciudadanos_alerta()
    for ciudadano in ciudadanos:
        icon = folium.Icon(color='yellow', icon='info-sign')
        popup = folium.Popup(f"DNI: {ciudadano['dni']}", max_width=300)
        folium.Marker(
            [ciudadano['latitud'], ciudadano['longitud']],
            popup=popup,
            icon=icon
        ).add_to(m)

def add_ruta_markers(m):
    rutas = get_rutas_activas()
    for ruta in rutas:
        folium.PolyLine(
            ruta['coordenadas'],
            color="red",
            weight=2,
            opacity=0.8
        ).add_to(m)

def create_sereno_icon(forma_patrullaje, color):
    if forma_patrullaje == 'PATRULLAJE A PIE':
        return folium.Icon(color=color, icon='male', prefix='fa')
    elif forma_patrullaje == 'PATRULLAJE EN MOTO':
        return folium.Icon(color=color, icon='motorcycle', prefix='fa')
    elif forma_patrullaje == 'PATRULLAJE EN AUTO':
        return folium.Icon(color=color, icon='car', prefix='fa')
    else:
        return folium.Icon(color=color, icon='question', prefix='fa')