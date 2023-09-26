import os

import serial
import serial.tools.list_ports
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')



@app.route('/signal')
def got_signal():
    print("______________Writing to comport________________")

    # Устанавливаем соединение с портом
    ser = serial.Serial("COM2", 9600, timeout=1)

    # Адрес устройства (Address High Byte, Address Low Byte)
    device_address = 0x0F
    address_high_byte = device_address // 256
    address_low_byte = device_address % 256

    # Команда "Dispensing card (Card out address)" (Command High Byte, Command Low Byte)
    command = 0x44
    command_high_byte = command // 256
    command_low_byte = command % 256

    # Расчет BCC
    bcc = (
        0x02  # STX
        ^ address_high_byte
        ^ address_low_byte
        ^ command_high_byte
        ^ command_low_byte
        ^ 0x03  # ETX
    )

# Подготовка команды с BCC для отправки
    command_bytes = bytes([0x02, address_high_byte, address_low_byte, command_high_byte, command_low_byte, 0x03, bcc])

    # Отправка команды
    ser.write(command_bytes)

    # Ожидание ответа
    response = ser.read(64)

    if response:
        print("Response received:", response)
    else:   
        print("No response received.")
        return jsonify('success', 200)
        # serialPort.write(1)

#os.system("C:/Progra~1/Mozill~1/firefox.exe --kiosk localhost:1583")
os.system("C:/Progra~1/Mozill~1/firefox.exe localhost:1583")
app.run(host='0.0.0.0', port=1583)
