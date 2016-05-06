Humidity Sensor Controlled Over WiFi Using an Android Device
Written in Python
By:
   Aakash Sheth
   Arlen Burroughs
   Brad Patras


To Start Server, enter this command on the Raspberry Pi: 
sudo python <path to sourcecode>/humidity_sensor/flask_server/index.py
The server is supposed to launch automatically upon booting, but a problem with network connectivity may cause issues.


In a web browser Goto:
   http://arlenburroughs.com/extras/486/get_addr.php?key=jkoplkjasd908f7f7f7fa89sd7jh34j
   to get the Pi's local IP (Note: Must be on same network as PI to view homepage)
   
Homepage:
   <IP from above>:5000/homepage
      You may also open the Pi's webbrowser and go to "localhost:5000/homepage"

The Remote PCB that is connected to the bread board requires an A23 battery in order to switch the state of the wall socket.
* Leaving the battery in will drain it after a few hours


See index.py for API requirements
