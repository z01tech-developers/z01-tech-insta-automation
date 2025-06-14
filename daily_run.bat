@echo off
cd /d "D:\work\Z01.tech\Luxury IG bot\Insta Automation"
call .venv\Scripts\activate.bat
python insert_quote.py
python fetch_pexels_video.py
