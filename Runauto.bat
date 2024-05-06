@echo off

call .\env\Scripts\activate.bat
timeout /t 2
python BScraper.py
pause
call .\env\scripts\deactivate.bat
pause
