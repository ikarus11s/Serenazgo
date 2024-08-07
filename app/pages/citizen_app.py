import streamlit as st
from components.forms import citizen_form
from utils.panic_button import process_panic_button

def show():
    st.title("App del Ciudadano")
    
    if citizen_form():
        process_panic_button()
        st.success("Su alerta ha sido enviada. Un sereno está en camino.")