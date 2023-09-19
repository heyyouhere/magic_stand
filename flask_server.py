import serial.tools.list_ports
from flask import Flask, jsonify, render_template

app = Flask(__name__)

#____________COM PORT SETTINGS_________________________#
serialPort = None
print('Search...')
available_ports = serial.tools.list_ports.comports(include_links=False)
for port in available_ports:
    print('Find port '+ port.device)    
    serialPort = port.device



@app.route('/')
def hello():
    return render_template('index.html')



@app.route('/signal')
def got_signal():
    print("______________Writing to comport________________")
    return jsonify('success', 200)
    # serialPort.write(1)


app.run(host='0.0.0.0', port=1583)
