from modules.AWSServer import MQTTServer
import json
import os

def main():
    print (os.getcwd())
    server = MQTTServer("a2cr09xzlv9lkb-ats.iot.us-east-2.amazonaws.com", "src/resources/root-CA.crt",
                         "src/resources/eee132ef2d-private.pem.key", "src/resources/eee132ef2d-certificate.pem.crt", "smartWECS_RBPi")
    server.connect()
    json0 = json.loads('{ "state" : "boa" }')
    server.publish(json0, "state")

if __name__ == "__main__":
    main()