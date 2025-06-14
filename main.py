# main.py

from flask import Flask
import insert_quote
import fetch_pexels_video

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Luxury IG Bot is live on Cloud Run!"

@app.route('/run', methods=['GET', 'POST'])
def run_bot():
    insert_quote.main()
    fetch_pexels_video.main()
    return "✅ Quote + Video added to Google Sheets!"
