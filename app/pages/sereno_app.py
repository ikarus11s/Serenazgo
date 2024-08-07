import streamlit as st
from components.forms import sereno_form
from utils.panic_button import update_alert_status

def show():
    st.title("App del Sereno")
    
    dni = st.selectbox("Seleccione su DNI", get_sereno_dnis())
    
    if dni:
        status = get_sereno_status(dni)
        st.write(f"Estado: {status}")
        
        if sereno_form():
            update_alert_status()
            st.success("Estado de alerta actualizado.")