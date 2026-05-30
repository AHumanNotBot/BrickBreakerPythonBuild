@echo off
setlocal

py -m pip install -r requirements.txt
py -m PyInstaller ^
  --noconfirm ^
  --clean ^
  --onedir ^
  --windowed ^
  --name BrickBreakerUSB ^
  --add-data "questions.txt;." ^
  main.py

echo.
echo Build complete. Copy the dist\BrickBreakerUSB folder to your USB drive.
echo Run BrickBreakerUSB.exe from inside that folder.
