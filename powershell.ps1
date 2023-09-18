$path = "C:\Users\$env:UserName\magic_stand\"

Start-Process python -ArgumentList "flask_server.py" -NoNewWindow
Start-Process $path -ArgumentList "--kiosk" -NoNewWindow
