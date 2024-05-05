@echo off

python -m venv env
timeout /t 2
call .\env\Scripts\activate.bat
timeout /t 2
pip install -r requirements.txt
timeout /t 2
deactivate
pause