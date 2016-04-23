from flask import Flask, request
import RPi.GPIO as GPIO
import time
import myDHT22

# GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set PIN 18 as output 
GPIO.setup(18, GPIO.OUT)


app = Flask(__name__)

# Sample test to see if I could the LED to light up
##@app.route("/<action>")
##def on(action):
##        if action == "on":
##                GPIO.output(18, GPIO.HIGH)
##                return "LED IS ON!"
##
##@app.route("/off")
##def off():
##        GPIO.output(18, GPIO.LOW)
##        return "LED is OFF!"

@app.route("/test", methods=['GET'])
def test():
	data = "{'status': 'It works'}"
       	return data

#######################################################

# Get the current humidity
@app.route("/humdity_sensor", methods=['GET'])
def getHumiditySensor():

        # Get the humidity sensor reading
        reading = myDHT22.getHumidity()

        current_humidity = reading['humidity']
        current_temp = reading['temp']

        data = {
                'status' : '',
                'current_humidity' : '',
                'current_temp' : '',
        }

        if(reading):
                data['status'] = 'success'
                data['current_humidity'] = current_humidity
                data['current_temp'] = current_temp
                return flask.jsonify(data)


        data['current_humidity'] = "null"
        data['current_temp'] = "null"
        data['status'] = "fail"
        data['error'] = "Unable to read from sensor"
        
        return flask.jsonify(data)

        

@app.route("/humidity_change_setting", methods=['POST'])
def setCurrentHumidity():
        
        # Set new value
        value = request.form['value']
        current_humidity_setting = ''
        
        try:
                myFile = open('settings', 'w')
                myFile.truncate()

                myFile.write(value)
                myFile.close()

                current_humidity_setting = value

                data = {
                        'status' : 'success',
                        'current_humidity_setting' : current_humidity_setting,
                }
                return flask.jsonify(data)
                
        except Exception:
                return flask.jsonify({
                        'status' : 'failure',
                        'message' : 'Could not write to file'
                })
                


# Get the current humidity setting
@app.route("/humidity_setting", methods=['GET'])
def getCurrentHumiditySetting():

        # Get the current humidity setting
        try:
                myFile = open('settings', 'r')
                value = myFile.readLine()
                myFile.close()

                current_humidity_setting = value

                data = {
                        'status' : 'success',
                        'current_humidity_setting' : current_humidity_setting,
                }
                return flask.jsonify(data)
                
        except Exception:
                return flask.jsonify({
                        'status' : 'failure',
                        'message' : 'Could not read from file'
                })

                
# Get current state of humidifier
@app.route("/state", methods=['GET'])
def getCurrentState():

        # Get the status, on or off
        try:
                myFile = open('state', 'w')
                state = myFile.readLine()
                myFile.close()

                data = {
                        'status' : 'success',
                        'current_humidity_status' : state,
                }
                return flask.jsonify(data)
                
        except Exception:
                return flask.jsonify({
                        'status' : 'failure',
                        'message' : 'Could not read humidifier state from file'
                })
        


if __name__ == "__main__":
        app.run(host='0.0.0.0')
        print("Succesfully launched!")
