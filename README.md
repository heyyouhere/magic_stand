# Setting up on Ubuntu
```console 
$ git clone https://github.com/heyyouhere/magic_stand
```
Make ./start_kiosk.sh executable
```console
$ chmod /magic_stand/start_kiosk.sh
```

Copy videos to new folder /magic_stand/
```console
$ cd idle_short.mp4 magic_short.mp4 /magic_stand/
```
Then setup startup:
- Activities -> \[type\] Startup -> start_kiosk.sh
Then setup autologin:
- Activities -> \[type\] User -> Allow autologin
Disable screen lock: 
- Activities -> \[]