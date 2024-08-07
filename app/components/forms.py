import streamlit as st
from utils.google_sheets import update_citizen_sheet, get_sereno_dnis, get_incident_numbers

def citizen_form():
    st.header("Reportar emergencia")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nombres = st.text_input("Nombres del denunciante")
        apellidos = st.text_input("Apellidos del denunciante")
        dni = st.text_input("DNI del denunciante", max_chars=8)
        celular = st.text_input("Celular del denunciante", max_chars=9)
    
    with col2:
        tipo = st.selectbox("Tipo de emergencia", get_tipos_emergencia())
        subtipo = st.selectbox("Subtipo de emergencia", get_subtipos_emergencia(tipo))
        modalidad = st.selectbox("Modalidad", get_modalidades(subtipo))
    
    ubicacion = st.radio("Ubicación", ["Para mí", "Para otra persona"])
    
    if ubicacion == "Para mí":
        lat, lon = get_current_location()
    else:
        lat = st.number_input("Latitud")
        lon = st.number_input("Longitud")
        
        st.markdown("Seleccione la ubicación en el mapa:")
        display_location_picker(lat, lon)
    
    if st.button("Enviar alerta", key="panic_button"):
        update_citizen_sheet(nombres, apellidos, dni, celular, tipo, subtipo, modalidad, lat, lon)
        return True
    
    return False

def sereno_form():
    st.header("Gestión de alertas")
    
    dni_sereno = st.selectbox("Seleccione su DNI", get_sereno_dnis())
    
    if dni_sereno:
        estado_sereno = get_sereno_status(dni_sereno)
        st.write(f"Estado actual: {estado_sereno}")
        
        numero_parte = st.selectbox("Número de parte", get_incident_numbers())
        
        if numero_parte:
            incident_data = get_incident_data(numero_parte)
            display_incident_data(incident_data)
            
            new_status = st.radio("Actualizar estado", ["Normal", "Alerta"])
            
            if st.button("Actualizar estado"):
                update_incident_status(numero_parte, new_status)
                update_sereno_status(dni_sereno, new_status)
                return True
    
    return False