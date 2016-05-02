path = "/home/pi/486/humidity_sensor/flask_server/"

def readSettings():
    myFile = open(path+'settings', 'r')
    value = myFile.readline()
    myFile.close()
    return value

def writeSettings(value):    
    myFile = open(path+'settings', 'w')
    myFile.truncate()
    myFile.write(value)
    myFile.close()

def readState():
    myFile = open(path+'state', 'r')
    value = myFile.readline()
    myFile.close()
    return value

def writeState(value):    
    myFile = open(path+'state', 'w')
    myFile.truncate()
    myFile.write(value)
    myFile.close()

def readUserState():
    myFile = open(path+'user_state', 'r')
    value = myFile.readline()
    myFile.close()
    return value

def writeUserState(value):    
    myFile = open(path+'user_state', 'w')
    myFile.truncate()
    myFile.write(value)
    myFile.close()

def readHumidity():
    myFile = open(path+'humidity', 'r')
    value = myFile.readline()
    myFile.close()
    return value

def writeHumidity(value):
    myFile = open(path+'humidity', 'w')
    myFile.truncate()
    myFile.write(str(value))
    myFile.close()
