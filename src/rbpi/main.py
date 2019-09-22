import time
import threading
from timeloop import Timeloop
from datetime import timedelta
from modules.AWSServer import MQTTServer
from modules.UARTSerial import Serial

currentAdc = None
waterPeriod = None
electricity = 0
water = 0

tl = Timeloop()

server = MQTTServer("a2cr09xzlv9lkb-ats.iot.us-west-2.amazonaws.com", "resources/root-CA.crt",
                         "resources/cert.key", "resources/cert.crt", "")
server.connect()

def main():

    global currentAdc
    global waterPeriod

    serial = Serial("/dev/ttyS0", 9600, 5)

    tl.start(block=False)

    while(1):
        serial.write('e'.encode())
        currentAdc = serial.read()
        if (currentAdc == b''):
            currentAdc = b'0'
        print("ELE:", currentAdc)

        serial.write('w'.encode())
        waterPeriod = serial.read()
        if (waterPeriod == b'' or int(waterPeriod) < 0):
            waterPeriod = b'0'
        print("WAT:", waterPeriod)

@tl.job(interval=timedelta(seconds=1))
def sendData(): 

    global currentAdc
    global waterPeriod
    global electricity
    global water
        
    if currentAdc is not None and waterPeriod is not None:
        current = (30*int(currentAdc)) / 1023
        electricity += 127*current
        try:
            water += 7.5 / int(waterPeriod)
        except Exception as e:
            print ("ERROR:",e)
        data = {
            "electricity" : int(electricity),
            "water" : int(water)
        }
        server.publish(data, "data")
        print('running')

if __name__ == "__main__":
    main()