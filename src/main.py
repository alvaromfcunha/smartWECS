from modules.AWSServer import MQTTServer
import json
import os

def main():
    server = MQTTServer("a2cr09xzlv9lkb-ats.iot.us-east-2.amazonaws.com", "resources/root-CA.crt",
                         "resources/654373ba50-private.pem.key", "resources/654373ba50-certificate.pem.crt", "smartwecs_thing")
    server.connect()
    json0 = json.loads('{ "state" : "boa" }')
    server.publish(json0, "state")

if __name__ == "__main__":
    main()