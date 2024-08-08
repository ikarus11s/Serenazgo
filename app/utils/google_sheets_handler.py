import gspread
import os
import json
from google.oauth2.service_account import Credentials
from config import SPREADSHEET_ID
import streamlit as st

# Intenta obtener las credenciales de la variable de entorno
creds_json = os.getenv('GOOGLE_CREDENTIALS_SERENAZGO_JSON')

# Si no está en la variable de entorno, intenta obtenerlo de los secretos de Streamlit
if not creds_json:
    try:
        creds_json = st.secrets["GOOGLE_CREDENTIALS_SERENAZGO_JSON"]
    except KeyError:
        st.error("No se encontraron las credenciales de Google. Por favor, configura GOOGLE_CREDENTIALS_SERENAZGO_JSON en los secretos de Streamlit.")
        st.stop()

# Convierte el contenido JSON en un diccionario de Python
try:
    creds_dict = json.loads(creds_json)
except json.JSONDecodeError:
    st.error("El formato de las credenciales de Google no es válido. Asegúrate de que sea un JSON válido.")
    st.stop()
except TypeError:
    st.error("Las credenciales de Google no están definidas o son nulas.")
    st.stop()

def get_google_sheet():
    creds = Credentials.from_service_account_info(creds_dict, scopes=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])
    client = gspread.authorize(creds)
    return client.open_by_key(SPREADSHEET_ID)

def get_serenos_data():
    sheet = get_google_sheet().worksheet('Serenos')
    return sheet.get_all_records()

def get_ciudadanos_data():
    sheet = get_google_sheet().worksheet('Ciudadanos')
    return sheet.get_all_records()

def update_sereno_location(sereno_id, lat, lon):
    sheet = get_google_sheet().worksheet('Serenos')
    cell = sheet.find(sereno_id)
    sheet.update_cell(cell.row, 11, lat)  # Asumiendo que la latitud está en la columna 11
    sheet.update_cell(cell.row, 12, lon)  # Asumiendo que la longitud está en la columna 12

def add_new_alert(data):
    sheet = get_google_sheet().worksheet('Ciudadanos')
    sheet.append_row(data)
