@REM pyinstaller main.py --icon=assets\icon.ico --onefile --noconsole

pyinstaller --add-data "assets\images;assets/images" main.py --onefile --noconsole
