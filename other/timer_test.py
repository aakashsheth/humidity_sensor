import time
from threading import Timer

def do_thing():
    print ("Doing it...")
    Timer(1, do_thing, ()).start()


do_thing()
