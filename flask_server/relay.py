import RPi.GPIO as GPIO
import time

# GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set PIN 17,18 as output 
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def turn_on():
    print ("     Sending signal to 'on' button")
    GPIO.output(17, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(17, GPIO.LOW)

def turn_off():
    print ("     Sending signal to 'off' button")
    GPIO.output(18, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(18, GPIO.LOW)
        
        


