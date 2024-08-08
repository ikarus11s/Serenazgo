import streamlit as st
import os
import json

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Emergencia - Pueblo Libre",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Obtén las credenciales de Google Sheets desde la variable de entorno
creds_json = os.getenv('GOOGLE_CREDENTIALS_SERENAZGO_JSON')

# Verifica si se recuperaron las credenciales correctamente
if creds_json is None:
    raise ValueError("No se pudo encontrar la clave de credenciales de Google. Asegúrate de haber configurado el secreto en GitHub.")

# Convierte el contenido JSON en un diccionario de Python
GOOGLE_SHEETS_CREDENTIALS = json.loads(creds_json)

# Configura las credenciales
def get_credentials():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    return Credentials.from_service_account_info(GOOGLE_SHEETS_CREDENTIALS, scopes=scope)

# ID de la hoja de cálculo de Google
SPREADSHEET_ID = '1xJO4wKH5evRY86wlLx8pj8ibXDtN91NFEetPCQQeU1c'

# Configuración del mapa
PUEBLO_LIBRE_CENTER = [-12.0789, -77.0842]
DEFAULT_ZOOM = 14

