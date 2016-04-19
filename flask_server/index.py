from flask import Flask, request
import RPi.GPIO as GPIO
import time

# GPIO Settings
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

# Set PIN 18 as output 
GPIO.setup(18, GPIO.OUT)


app = Flask(__name__)

# Sample test to see if I could the LED to light up
@app.route("/<action>")
def on(action):
	if action == "on":
		GPIO.output(18, GPIO.HIGH)
		return "LED IS ON!"

@app.route("/off")
def off():
	GPIO.output(18, GPIO.LOW)
	return "LED is OFF!"

#######################################################

# Get the current humidity
@app.route("/humdity_sensor", methods=['GET'])
def getHumiditySensor():

	


	# Get the humidity sensor reading
	if request.method == 'GET' :
		
		# TODO: Get the current humidity

		current_humidity = "Replace sensor value here"

		data = {
			'status' : ''
			'current_humidity' : '',
		}

		if(sensor):
			data['status'] = 'success'
			data['current_humidity'] = current_humidity
			return flask.jsonify(data)


		data['current_humidity'] = "null"
		data['status'] = "fail"
		data['error'] = "Unable to read from sensor"
		
		return flask.jsonify(data)

	# Set new value
	if request.method == 'POST' :

		value = request.form['value']

		# TODO: Set the new value
		# TODO: Read the value after it was set


		current_humidity_setting = "Value of current setting"

		# If successfull
		data = {
			'status' : ''
			'current_humidity_setting' : current_humidity_setting,
		}
		return flask.jsonify(data)
		


# Get the current humidity setting
@app.route("/humidity_setting", methods=['GET', 'POST'])
def getCurrentHumiditySetting():

	# TODO: get the current humidity setting
	
	current_humidity_setting = "Replace sensor setting here"

	data = {
		'status' : ''
		'current_humidity_setting' : '',
	}

	if(sensor):
		data['status'] = 'success'
		data['current_humidity_setting'] = current_humidity_setting
		return flask.jsonify(data)


	data['current_humidity_setting'] = "null"
	data['status'] = "fail"
	data['error'] = "Unable to read from sensor"
	
	return flask.jsonify(data)

# Get on/off status of humidifier
@app.route("/humidity_status", methods=['GET'])
def getCurrentHumidityStatus():

	# TODO: Get the status, on or off
	current_humidity_status = "Replace sensor status here"

	data = {
		'status' : ''
		'current_humidity_status' : '',
	}

	if(sensor):
		data['status'] = 'success'
		data['current_humidity_status'] = current_humidity_status
		return flask.jsonify(data)


	data['current_humidity_status'] = "null"
	data['status'] = "fail"
	data['error'] = "Unable to read from sensor"
	
	return flask.jsonify(data)

# Get current state of humidifier
@app.route("/state", methods=['GET'])
def getCurrentState():

	# TODO: get the current state

	# Get the humidity state
	current_humidity_state = "Replace sensor state here"

	data = {
		'status' : ''
		'current_humidity_state' : '',
	}

	if(sensor):
		data['status'] = 'success'
		data['current_humidity_state'] = current_humidity_state
		return flask.jsonify(data)


	data['current_humidity_state'] = "null"
	data['status'] = "fail"
	data['error'] = "Unable to read from sensor"
	
	return flask.jsonify(data)

# Get current state of humidifier
@app.route("/humidity_setting", methods=['GET'])
def getCurrentState():

	# TODO: get the the current humidity state

	# Get the humidity state
	current_humidity_state = "Replace sensor state here"

	data = {
		'status' : ''
		'current_humidity_state' : '',
	}

	if(sensor):
		data['status'] = 'success'
		data['current_humidity_state'] = current_humidity_state
		return flask.jsonify(data)


	data['current_humidity_state'] = "null"
	data['status'] = "fail"
	data['error'] = "Unable to read from sensor"
	
	return flask.jsonify(data)

# Toggle the status of the sensor
@app.route("/toggle", methods=['POST'])
def toggleState():

	# TODO: Toggle the sensor status

	# Get the humidity state after toggling
	current_humidity_state = "Replace sensor state here"

	data = {
		'status' : ''
		'current_humidity_state' : '',
	}

	if(current_humidity_state):
		data['status'] = 'success'
		data['current_humidity_state'] = current_humidity_state
		return flask.jsonify(data)


	data['current_humidity_state'] = "null"
	data['status'] = "fail"
	data['error'] = "Unable to read from sensor"
	
	return flask.jsonify(data)

	


if __name__ == "__main__":
	app.run(host='0.0.0.0')
