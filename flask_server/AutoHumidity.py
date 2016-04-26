import time
import thread
from threading import Timer

def perform_check(interval):
    
    print ("   --- Automation Checking")
    
    myFile = open('user_state', 'r')
    usr_state = myFile.readline()
    myFile.close()

    myFile = open('state', 'r')
    state = myFile.readline()
    myFile.close()

    myFile = open('settings', 'r')
    setting = myFile.readline()
    myFile.close()

    print ("   "+usr_state)
    print ("   "+state)
    print ("   "+setting)
    
    Timer(interval, perform_check, [interval]).start()

def begin_automation(interval):
    print ("------ Starting automation script\n      with "+str(interval)+" sec. intervals...")
    thread.start_new_thread(perform_check, (interval,))
