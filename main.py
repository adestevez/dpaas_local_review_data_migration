import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# 1️⃣ Definir los alcances (Scopes)
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# 2️⃣ Autenticarse con el archivo JSON de credenciales
creds = Credentials.from_service_account_file("credentials/dev-dpaas.json", scopes=SCOPES)
client = gspread.authorize(creds)

# 3️⃣ Abrir la hoja de cálculo por su ID
SHEET_ID = "1AuFOMhsAnUgX-vAtEGnDUnlRgrNHHkzv1zjirkiBdws"
workbook = client.open_by_key(SHEET_ID)

# 4️⃣ Seleccionar la hoja específica (puedes cambiar "Sheet1" por el nombre de la hoja)
sheet = workbook.worksheet("Test1")

# 5️⃣ Leer los datos de la hoja (todas las filas)
data = sheet.get_all_values()

# 6️⃣ Convertir los datos a un DataFrame de Pandas para mejor visualización
df = pd.DataFrame(data[1:], columns=data[0])  # Usa la primera fila como nombres de columnas
