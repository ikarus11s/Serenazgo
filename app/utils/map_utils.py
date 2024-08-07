import folium
from streamlit_folium import folium_static
from config import PUEBLO_LIBRE_CENTER, DEFAULT_ZOOM

def create_map():
    m = folium.Map(location=PUEBLO_LIBRE_CENTER, zoom_start=DEFAULT_ZOOM)
    return m

def add_sereno_markers(m, serenos):
    for sereno in serenos:
        color = 'blue' if sereno['Estado'] == 'Normal' else 'red'
        icon = get_sereno_icon(sereno['Forma de patrullaje'], color)
        folium.Marker(
            [sereno['Latitud'], sereno['Longitud']],
            popup=f"DNI: {sereno['DNI']}",
            icon=icon
        ).add_to(m)

def add_ciudadano_markers(m, ciudadanos):
    for ciudadano in ciudadanos:
        if ciudadano['Estado'] == 'Alerta':
            folium.Marker(
                [ciudadano['Latitud'], ciudadano['Longitud']],
                popup=f"DNI: {ciudadano['DNI']}",
                icon=folium.Icon(color='yellow', icon='info-sign')
            ).add_to(m)

def get_sereno_icon(forma_patrullaje, color):
    if forma_patrullaje == 'PATRULLAJE A PIE':
        return folium.Icon(color=color, icon='male', prefix='fa')
    elif forma_patrullaje == 'PATRULLAJE EN MOTO':
        return folium.Icon(color=color, icon='motorcycle', prefix='fa')
    elif forma_patrullaje == 'PATRULLAJE EN AUTO':
        return folium.Icon(color=color, icon='car', prefix='fa')
    else:
        return folium.Icon(color=color, icon='question', prefix='fa')

def display_map(m):
    folium_static(m)