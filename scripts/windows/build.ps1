# pyinstaller main.py --icon=assets\icon.ico --onefile --noconsole

# pyinstaller --add-data "app\assets\images:app\assets\images" main.py --onefile --noconsole

pyinstaller --add-data "app\assets\images:app\assets\images" --add-data "app\assets\data:app\assets\data" main.py --onefile --noconsole