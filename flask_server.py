from flask import Flask, render_template
import serial

app = Flask(__name__)

#____________COM PORT SETTINGS_________________________#
#serialPort = None
#print('Search...')
#ports = serial.tools.list_ports.comports(include_links=False)
#for port in ports :
#    print('Find port '+ port.device)    
#    serialPort = port.device


@app.route('/')
def hello():
    return render_template('index.html')



@app.route('/signal')
def got_signal():
    print("______________Writing to comport________________")
    serialPort.write(1)


app.run(host='0.0.0.0', port=1583)
