import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)  # replace with your file
client = gspread.authorize(creds)

# Open your sheet
sheet = client.open_by_key("1PTTeJhjyo2L9MxSMslhror_SNclAgEPVY97Cb1FETrQ").sheet1  # or .worksheet("Sheet1") if named

# Prepare data
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
row = [now, "Success is silent.", "Let the lifestyle flex 💼", "https://cdn.pexels.com/video123.mp4", "Test", "Initial test"]

# Append row
sheet.append_row(row)

print("✅ Row added to Google Sheet.")
