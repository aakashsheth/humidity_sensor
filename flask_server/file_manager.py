
def readSettings():
    myFile = open('settings', 'r')
    value = myFile.readline()
    myFile.close()
    return value

def writeSettings(value):    
    myFile = open('settings', 'w')
    myFile.truncate()
    myFile.write(value)
    myFile.close()

def readState():
    myFile = open('state', 'r')
    value = myFile.readline()
    myFile.close()
    return value

def writeState(value):    
    myFile = open('state', 'w')
    myFile.truncate()
    myFile.write(value)
    myFile.close()

def readUserState():
    myFile = open('user_state', 'r')
    value = myFile.readline()
    myFile.close()
    return value

def writeUserState(value):    
    myFile = open('user_state', 'w')
    myFile.truncate()
    myFile.write(value)
    myFile.close()
