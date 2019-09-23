import time
import threading
from timeloop import Timeloop
from datetime import timedelta
from modules.AWSServer import MQTTServer
from modules.UARTSerial import Serial

multiplier = 10

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

        current = (30 * int(currentAdc)) / 1023 # A
        electricity += ((127 * current)* 3.6) / 1000 # kW/h

        electricityMoney = electricity * 0.92189069

        if waterPeriod != 0:
            waterFlow = (7.5 / int(waterPeriod)) * 3.6 # m3/s
        else:
            waterFlow = 0
        
        water += waterFlow

        waterMoney = 15.29 + 14.14
        waterTmp = water
        if water <= 5:
            waterMoney += (waterTmp * 0.96) + (waterTmp * 0.89)
        elif water <=10:
            waterMoney += (waterTmp * 0.96) + (waterTmp * 0.89)
            waterTmp -= 5
            waterMoney += (waterTmp * 3.089) + (waterTmp * 2.857)
        elif water <= 15:
            waterMoney += (waterTmp * 0.96) + (waterTmp * 0.89)
            waterTmp -= 5
            waterMoney += (waterTmp * 3.089) + (waterTmp * 2.857)
            waterTmp -= 5
            waterMoney += (waterTmp * 6.407) + (waterTmp * 5.926)
        elif water <=20:
            waterMoney += (waterTmp * 0.96) + (waterTmp * 0.89)
            waterTmp -= 5
            waterMoney += (waterTmp * 3.089) + (waterTmp * 2.857)
            waterTmp -= 5
            waterMoney += (waterTmp * 6.407) + (waterTmp * 5.926)
            waterTmp -= 5
            waterMoney += (waterTmp * 7.637) + (waterTmp * 7.064)
        elif water <=40:
            waterMoney += (waterTmp * 0.96) + (waterTmp * 0.89)
            waterTmp -= 5
            waterMoney += (waterTmp * 3.089) + (waterTmp * 2.857)
            waterTmp -= 5
            waterMoney += (waterTmp * 6.407) + (waterTmp * 5.926)
            waterTmp -= 5
            waterMoney += (waterTmp * 7.637) + (waterTmp * 7.064)
            waterTmp -= 5
            waterMoney += (waterTmp * 8.326) + (waterTmp * 7.702)
        else:
            waterMoney += (waterTmp * 0.96) + (waterTmp * 0.89)
            waterTmp -= 5
            waterMoney += (waterTmp * 3.089) + (waterTmp * 2.857)
            waterTmp -= 5
            waterMoney += (waterTmp * 6.407) + (waterTmp * 5.926)
            waterTmp -= 5
            waterMoney += (waterTmp * 7.637) + (waterTmp * 7.064)
            waterTmp -= 5
            waterMoney += (waterTmp * 8.326) + (waterTmp * 7.702)
            waterTmp -= 20
            waterMoney += (waterTmp * 13.662) + (waterTmp * 12.637)

        data = {
            "electricity" : int(electricity),
            "water" : int(water),
            "money" :{
                "electricity" : electricityMoney,
                "water" : waterMoney
            }
        }
        server.publish(data, "data")
        print('running')

if __name__ == "__main__":
    main()