import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Emergencia - Pueblo Libre",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Credenciales para Google Sheets (deberías usar variables de entorno en producción)
GOOGLE_SHEETS_CREDENTIALS = {
    "type": "service_account",
    "project_id": "tu-proyecto-id",
    "private_key_id": "tu-private-key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\ntu-private-key\n-----END PRIVATE KEY-----\n",
    "client_email": "tu-client-email@tu-proyecto.iam.gserviceaccount.com",
    "client_id": "tu-client-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tu-client-email%40tu-proyecto.iam.gserviceaccount.com"
}

# ID de la hoja de cálculo de Google
SPREADSHEET_ID = 'tu-spreadsheet-id'

# Configuración del mapa
PUEBLO_LIBRE_CENTER = [-12.0789, -77.0842]
DEFAULT_ZOOM = 14