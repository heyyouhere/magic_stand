Start-Process python -ArgumentList "flask_server.py" -NoNewWindow
Start-Process "C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -ArgumentList "--kiosk localhost:1583" -NoNewWindow
