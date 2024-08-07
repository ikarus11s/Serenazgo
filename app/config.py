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
    st.error("No se pudo encontrar la clave de credenciales de Google. Asegúrate de haber configurado el secreto en GitHub.")
else:
    # Convierte el contenido JSON en un diccionario de Python
    creds_dict = json.loads(creds_json)
    
    # Configura las credenciales
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
    client = gspread.authorize(creds)

    # Ahora puedes usar el cliente para interactuar con Google Sheets
    try:
        sheet = client.open("Serenazgo").sheet1
        st.write("Conexión exitosa con Google Sheets.")
    except Exception as e:
        st.error(f"No se pudo conectar a Google Sheets: {e}")

        
# ID de la hoja de cálculo de Google
SPREADSHEET_ID = '1xJO4wKH5evRY86wlLx8pj8ibXDtN91NFEetPCQQeU1c'

# Configuración del mapa
PUEBLO_LIBRE_CENTER = [-12.0789, -77.0842]
DEFAULT_ZOOM = 14

