import Adafruit_DHT as dht
import datetime
from datetime import datetime

#reading interval in seconds.
reading_interval = 3
num_readings = 1

i=0
prev_time = "00000099"

def getHumidity():
    h,t = dht.read_retry(dht.DHT22, 4)
    ret = {
        'humidity' : h,
        'temp' : t
    }

    return ret


##while (i<num_readings):
##    
##    now = str(datetime.time(datetime.now()))
##    time = now[0:8]
##    
##    time_diff = int(time[6:9])-int(prev_time[6:9])
##
##    if time_diff < reading_interval and time_diff >= 0:
##        continue
##
##    i=i+1
##    
##    print(str(i)+" - "+time )
##
##    now = str(datetime.time(datetime.now()))
##    prev_time = now[0:8]
##
##    h,t = dht.read_retry(dht.DHT22, 4)
##
##    print("Temp (C): "+str(t)[0:4])
##
##    temp_f = 9.0/5.0*t+32
##    print("Temp (F): "+str(temp_f)[0:4])
##    print("Humidity: "+str(h)[0:4]+"\n")

# reading = getHumidity()

    

