import RPi.GPIO as GPIO
import time

# GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set PIN 17,18 as output 
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)



while True:
    number = input("Please enter 1(on) or 2(off): ")

    if number == 1:
        GPIO.output(17, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(17, GPIO.LOW)
        print("Send signal to 'on' button")

    elif number == 2:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(18, GPIO.LOW)
        print("Send signal to 'off' button")
        
        


