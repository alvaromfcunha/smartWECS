import time
from modules.AWSServer import MQTTServer
from modules.UARTSerial import Serial
   
def main():

    serial = Serial("/dev/ttyS0", 9600, 5)
    server = MQTTServer("a2cr09xzlv9lkb-ats.iot.us-west-2.amazonaws.com", "resources/root-CA.crt",
                         "resources/cert.key", "resources/cert.crt", "")
    server.connect() 

    while(1):
        serial.write('e'.encode())
        eletricity = serial.read()

        print("ELE:", eletricity)

        serial.write('w'.encode())
        water = serial.read()

        if (water == b''):
            water = b'0'

        if (eletricity == b''):
            eletricity = b'0'

        print("WAT:", water)

        data = {
            "electricity" : int(eletricity),
            "water" : int(water)
        }

        server.publish(data, "data")

    
if __name__ == "__main__":
    main()
