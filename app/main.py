import streamlit as st
from config import *
from utils.google_sheets_handler import get_serenos_data, get_ciudadanos_data
from utils.map_utils import create_map, add_sereno_markers, add_ciudadano_markers, display_map
from utils.simulation_controller import simulation_controller

def main():
    st.title("Sistema de Emergencia - Pueblo Libre")

    menu = st.sidebar.selectbox(
        "Menú",
        ["Mapa de Serenazgo", "Gestión de Alertas", "Simulación"]
    )

    if menu == "Mapa de Serenazgo":
        show_serenazgo_map()
    elif menu == "Gestión de Alertas":
        show_alert_management()
    elif menu == "Simulación":
        show_simulation_control()

def show_serenazgo_map():
    st.header("Mapa de Serenazgo")
    m = create_map()
    serenos = get_serenos_data()
    ciudadanos = get_ciudadanos_data()
    add_sereno_markers(m, serenos)
    add_ciudadano_markers(m, ciudadanos)
    display_map(m)

def show_alert_management():
    st.header("Gestión de Alertas")
    alertas = get_ciudadanos_data()
    for alerta in alertas:
        if alerta['Estado'] == 'Alerta':
            st.write(f"Alerta: {alerta['Número de parte']}")
            st.write(f"Ubicación: {alerta['Latitud']}, {alerta['Longitud']}")
            if st.button(f"Atender alerta {alerta['Número de parte']}"):
                # Aquí iría la lógica para atender la alerta
                st.success(f"Alerta {alerta['Número de parte']} atendida")

def show_simulation_control():
    st.header("Control de Simulación")
    if st.button("Iniciar Simulación"):
        simulation_controller.start_simulations()
        st.success("Simulación iniciada")
    if st.button("Detener Simulación"):
        simulation_controller.stop_simulations()
        st.success("Simulación detenida")

if __name__ == "__main__":
    main()
