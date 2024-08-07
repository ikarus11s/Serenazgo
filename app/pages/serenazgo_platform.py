import streamlit as st
from components.map import display_map
from utils.fake_gps import update_sereno_positions

def show():
    st.title("Plataforma de Serenazgo")
    
    # Actualizar posiciones de serenos
    update_sereno_positions()
    
    # Mostrar mapa
    display_map()