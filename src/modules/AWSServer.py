from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json

class MQTTServer:
    def __init__(self, host, rootca_path, privkey_path, cert_path, client_id, endpoint_port=8883, connect_delay=1, backoff_time=32,
                 stable_time=20,offline_publish=-1, draining_freq=2, con_discon_timeout=10, operation_timeout=5):

        # Init AWSIoTMQTTClient
        self.myAWSIoTMQTTClient = None
        self.myAWSIoTMQTTClient = AWSIoTMQTTClient(client_id)
        self.myAWSIoTMQTTClient.configureEndpoint(host, 8883)
        self.myAWSIoTMQTTClient.configureCredentials(rootca_path, privkey_path, cert_path)
                                                     
        # AWSIoTMQTTClient connection configuration
        self.myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(connect_delay, backoff_time, stable_time)
        self.myAWSIoTMQTTClient.configureOfflinePublishQueueing(offline_publish) 
        self.myAWSIoTMQTTClient.configureDrainingFrequency(draining_freq) 
        self.myAWSIoTMQTTClient.configureConnectDisconnectTimeout(con_discon_timeout)  
        self.myAWSIoTMQTTClient.configureMQTTOperationTimeout(operation_timeout)

    def connect(self): 
        self.myAWSIoTMQTTClient.connect()

    def publish(self, json_message, topic, qos=1):
        json_message = json.dumps(json_message)
        self.myAWSIoTMQTTClient.publish(topic, json_message, qos)

    def subscribe(self, callback, topic, qos=1):
        self.myAWSIoTMQTTClient.subscribe(topic, qos, callback)

    def disconnect(self):
        self.myAWSIoTMQTTClient.disconnect()

