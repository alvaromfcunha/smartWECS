import time
from modules.AWSServer import MQTTServer
from modules.UARTSerial import Serial
   
def main():

    serial = Serial("/dev/ttyS0", 9600)
    server = MQTTServer("a2cr09xzlv9lkb-ats.iot.us-west-2.amazonaws.com", "resources/root-CA.crt",
                         "resources/cert.key", "resources/cert.crt", "")
    server.connect() 

    while(1):
        serial.write('e')
        time.sleep(.1)
        eletricity = serial.read()

        serial.write('w')
        time.sleep(.1)
        water = serial.read()

        data = {
            "eletricity" : eletricity,
            "water" : water
        }

        server.publish(data, "data")

    
if __name__ == "__main__":
    main()
