import os
import json
import gspread
from google.oauth2.service_account import Credentials
from config import SPREADSHEET_ID
import streamlit as st


# Convertir el JSON en un diccionario de Python
creds_dict = st.secrets["gcp_service_account"]

# Configurar credenciales
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

def update_citizen_sheet(nombres, apellidos, dni, celular, tipo, subtipo, modalidad, lat, lon):
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Ciudadanos")
    
    # Generar número de parte
    last_row = len(sheet.get_all_values())
    numero_parte = f"PO-{last_row + 1:07d}"
    
    # Obtener fecha y hora actual
    fecha_hora = get_current_datetime()
    
    # Preparar datos
    row_data = [fecha_hora, numero_parte, nombres, apellidos, dni, celular, tipo, subtipo, modalidad, lat, lon, "Alerta"]
    
    # Agregar nueva fila
    sheet.append_row(row_data)

def get_sereno_dnis():
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Serenos")
    return sheet.col_values(1)[1:]  # Asumiendo que los DNIs están en la primera columna

def get_incident_numbers():
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Ciudadanos")
    return sheet.col_values(2)[1:]  # Asumiendo que los números de parte están en la segunda columna

def get_incident_data(numero_parte):
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Ciudadanos")
    incident = sheet.find(numero_parte)
    return sheet.row_values(incident.row)

def update_incident_status(numero_parte, new_status):
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Ciudadanos")
    incident = sheet.find(numero_parte)
    sheet.update_cell(incident.row, 12, new_status)  # Asumiendo que el estado está en la columna 12

def update_sereno_status(dni, new_status):
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Serenos")
    sereno = sheet.find(dni)
    sheet.update_cell(sereno.row, 13, new_status)  # Asumiendo que el estado está en la columna 13import gspread
from google.oauth2.service_account import Credentials

# Convertir el JSON en un diccionario de Python
creds_dict = st.secrets["gcp_service_account"]
# Configurar credenciales
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

def update_citizen_sheet(nombres, apellidos, dni, celular, tipo, subtipo, modalidad, lat, lon):
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Ciudadanos")
    
    # Generar número de parte
    last_row = len(sheet.get_all_values())
    numero_parte = f"PO-{last_row + 1:07d}"
    
    # Obtener fecha y hora actual
    fecha_hora = get_current_datetime()
    
    # Preparar datos
    row_data = [fecha_hora, numero_parte, nombres, apellidos, dni, celular, tipo, subtipo, modalidad, lat, lon, "Alerta"]
    
    # Agregar nueva fila
    sheet.append_row(row_data)

def get_sereno_dnis():
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Serenos")
    return sheet.col_values(1)[1:]  # Asumiendo que los DNIs están en la primera columna

def get_incident_numbers():
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Ciudadanos")
    return sheet.col_values(2)[1:]  # Asumiendo que los números de parte están en la segunda columna

def get_incident_data(numero_parte):
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Ciudadanos")
    incident = sheet.find(numero_parte)
    return sheet.row_values(incident.row)

def update_incident_status(numero_parte, new_status):
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Ciudadanos")
    incident = sheet.find(numero_parte)
    sheet.update_cell(incident.row, 12, new_status)  # Asumiendo que el estado está en la columna 12

def update_sereno_status(dni, new_status):
    sheet = client.open("Serenazgo Pueblo Libre").worksheet("Serenos")
    sereno = sheet.find(dni)
    sheet.update_cell(sereno.row, 13, new_status)  # Asumiendo que el estado está en la columna 13
