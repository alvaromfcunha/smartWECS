import time
from modules.AWSServer import MQTTServer
from modules.UARTSerial import Serial
   
def main():

    serial = Serial("/dev/ttyS0", 9600)
    server = MQTTServer("a2cr09xzlv9lkb-ats.iot.us-west-2.amazonaws.com", "resources/root-CA.crt",
                         "resources/cert.key", "resources/cert.crt", "")
    server.connect() 

    while(1):
        serial.rese
        serial.write('e'.encode())
        time.sleep(.1)
        eletricity = serial.read()

        serial.write('w'.encode())
        time.sleep(.1)
        water = serial.read()

        data = {
            "eletricity" : int(eletricity),
            "water" : int(water)
        }

        server.publish(data, "data")

    
if __name__ == "__main__":
    main()
