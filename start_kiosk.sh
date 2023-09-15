#!/bin/bash


python3 -m http.server 6969 --directory /home/$USER/magic_stand/ &
firefox --kiosk localhost:6969