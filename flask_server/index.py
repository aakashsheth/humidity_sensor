from flask import Flask, request
import RPi.GPIO as GPIO
import time
import myDHT22

import file_manager as files
import publish_ip
import AutoHumidity

# Begin automation logic script
seconds_between_checks = 4
AutoHumidity.begin_automation(seconds_between_checks)

# GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set PIN 18 as output 
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)

@app.route("/test", methods=['GET'])
def test():
	data = "{'status': 'It works'}"
       	return data

#######################################################

# Get the current humidity
@app.route("/humidity_sensor", methods=['GET','POST'])
def getHumiditySensor():
        
	
	# Get the humidity sensor reading
        reading = myDHT22.getHumidity(1)
	print(reading['humidity'])
	time = reading['datetime']
        current_humidity = reading['humidity']
        current_temp = reading['temp']
	print(reading)

        data = {
                'status' : '',
                'time' : '',
                'current_humidity' : '',
                'current_temp' : '',
        }

        if(reading):
                data['status'] = 'success'
                data['time'] = time
                data['current_humidity'] = current_humidity
                data['current_temp'] = current_temp
		print("Data:", str(data)) 
                return str(data)


        data['current_humidity'] = "null"
        data['current_temp'] = "null"
        data['status'] = "fail"
        data['time'] = time
        data['error'] = "Unable to read from sensor"
        
        return str(data)

        

@app.route("/change_humidity_setting/<setting>", methods=['GET', 'POST'])
def setCurrentHumidity(setting):

        print ("Change humidity settings....")
        # Set new value
	value = setting
	print("value", value)

        current_humidity_setting = ''
        
        try:
                files.writeSettings(value)
                AutoHumidity.perform_check(-1)
                current_humidity_setting = value

                data = { 
			'status' : 'success',
			'current_humidity_setting' : str(current_humidity_setting)
		}
                return str(data)
                
        except Exception:
                data = {
                        'status' : 'failure',
                        'message' : 'Could not write to file'
                }
        return str(data)
                

# Get the current humidity setting
@app.route("/humidity_setting", methods=['GET','POST'])
def getCurrentHumiditySetting():

        print ("Get Humidity Setting....")
        # Get the current humidity setting
        try:
                value = files.readSettings()

                current_humidity_setting = value

                data = {
                        'status' : 'success',
                        'current_humidity_setting' : current_humidity_setting,
                }
                return str(data)
                
        except Exception:
                return "{'status' : 'failure','message' : 'Could not read from file'})"

# User updated on/off
@app.route("/user_state/<state>", methods=['GET','POST'])
def setUserState(state):

        # Set new value
	value = state

        try:
                files.writeUserState(value)
		AutoHumidity.perform_check(-2)
                current_user_state = value

                data = { 
			'status' : 'success',
			'current_user_state' : str(current_user_state)
		}
                return str(data)
                
        except Exception:
                return "{'status' : 'failure','message' : 'Could not write user_state from file'})"


 
# Get current state of humidifier
@app.route("/user_state", methods=['GET','POST'])
def getCurrentState():


        data = {
                'status' : '',
                'current_user_state' : '',
        }
        
        # Get the status, on or off
        try:
                state = files.readUserState()

                data['status'] = 'success'
                data['current_user_state'] = state
                return str(data)
                
        except Exception:
                return "{'status' : 'failure','message' : 'Could not read humidifier state from file'})"

# Display all current settings
@app.route("/all_settings", methods=['GET','POST'])
def getAllSettings():

        user_state = files.readUserState()
        to_show =       "User State:\t"+user_state

        state = files.readState()
        to_show +=      "<br>Humidifier State:\t"+state

        value = files.readSettings()
        to_show +=      "<br>Humidity Setting:\t"+value

        reading = myDHT22.getHumidity(1)
	hum = reading['humidity']
	to_show +=	"<br>Current Humidity:\t"+str(hum)

	data = {
                'status' : 'success',
                'current_state' : state,
                'current_user_state' : user_state,
                'current_humidity_setting' : value,
                'current_humidity' : hum,
        }

	return str(data)


if __name__ == "__main__":
	#app.run(processes=3)
        app.run(host='0.0.0.0', processes=3)
        print("Succesfully launched!")
