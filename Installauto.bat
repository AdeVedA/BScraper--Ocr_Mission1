@echo off

git init
timeout /t 2
git remote add origin https://github.com/AdeVedA/BScraper--Ocr_Mission1.git -t main
timeout /t 2
git pull origin main
timeout /t 10
python -m venv env
timeout /t 2
call .\env\Scripts\activate.bat
timeout /t 2
pip install -r requirements.txt
timeout /t 2