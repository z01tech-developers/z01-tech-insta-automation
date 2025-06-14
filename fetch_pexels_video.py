import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# === CONFIG ===
PEXELS_API_KEY = "WBKcaBN3ux5MhMFopyoF2u5ZShe80zEwL2Axamd2OrjhtS2hAXAas6pM"  # 🔁 Replace with your actual key
SHEET_ID = "1PTTeJhjyo2L9MxSMslhror_SNclAgEPVY97Cb1FETrQ"  # Your Google Sheet ID
SHEET_NAME = "Sheet1"

# === GOOGLE SHEETS AUTH ===
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)

# === PEXELS VIDEO FETCH ===
def fetch_luxury_video():
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    params = {
        "query": "luxury lifestyle",
        "per_page": 1
    }
    response = requests.get("https://api.pexels.com/videos/search", headers=headers, params=params)

    if response.status_code == 200:
        videos = response.json().get("videos")
        if videos:
            return videos[0]["video_files"][0]["link"]
    return None

# === SHEET UPDATE ===
def update_video_url(row_index, video_url):
    # Video URL is in column D (index 4)
    sheet.update_cell(row_index, 4, video_url)
    print(f"✅ Updated video URL in row {row_index}")

# === MAIN ===
def main():
    rows = sheet.get_all_records()
    for i, row in enumerate(rows, start=2):  # Skip header row (1), start at 2
        current_url = row.get("Image URL") or ""
        if current_url == "" or "example.com" in current_url:
            video_url = fetch_luxury_video()
            if video_url:
                update_video_url(i, video_url)
            break  # Update only the first incomplete row

if __name__ == "__main__":
    main()
