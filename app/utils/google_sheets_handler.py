import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_SHEETS_CREDENTIALS, SPREADSHEET_ID

def get_google_sheet():
    creds = Credentials.from_service_account_info(GOOGLE_SHEETS_CREDENTIALS, scopes=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])
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