import time
import datetime
from datetime import date
from datetime import datetime
import thread
from threading import Timer
import myDHT22
import relay
import file_manager as files

# the accuracy of the humidity
# (i.e. '2' will guarantee a humidity between 38 and 40 for a setting of 40%)
humidity_accuracy = 2

def perform_check(interval):

    print ("--- Humidity Automation Checking - "+date.strftime(datetime.now(), '%H:%M:%S'))

    # if user_state is not set to "on", we don't need to do anything
    user_state = files.readUserState()
    if user_state != "on":
        print ("\tUser state: '" + user_state+"'")
        print ("\tNot on, so doing nothing...")
        Timer(interval, perform_check, [interval]).start()
        return

    system = files.readUserState()
    print ("\tUser state : "+system)
    
    state = files.readState()
    print ("\tMach. State: "+state)

    reading = myDHT22.getHumidity()
    humid = reading['humidity']
    print ("\tCurrent Hum: "+str(humid))

    setting = float(files.readSettings())
    print ("\tDesired    : "+str(setting))

    #if it's on and the current humidity is more than the setting, turn off.
    if state == 'on' and humid >= setting:
        print ("   Turning OFF...")
        relay.turn_off()
        files.writeState("off")

    #if it's not on and the humidity is less than the setting (minus accuracy), turn on
    elif state != 'on' and humid < (setting-humidity_accuracy):
        print ("   Turning ON...")
        relay.turn_on()
        files.writeState("on")

    #otherwise, all is well.
    else:
        print ("   All is well, leaving the device "+state)

    if interval <= 0:
        print ("~~~~~ Modification check was just performed ~~~~~")
        return
    
    Timer(interval, perform_check, [interval]).start()

def begin_automation(interval):
    print ("------ Starting automation script with "+str(interval)+" sec. intervals...")
    thread.start_new_thread(perform_check, (interval,))
