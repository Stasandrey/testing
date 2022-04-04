import time
import datetime
import json
import psutil
import paho.mqtt.client as mqttc
USER = "homeassistant"
PWD = "baziliy2205"
IP_ADDRESS = "144.21.42.50"
PORT = 1883
TOPIC = "status"


class Mqtt:

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.mqtt = mqttc.Client("homeassistant")
        self.mqtt.username_pw_set(USER, PWD)

        self.mqtt.connect(self.address, self.port)

    def sent_message(self, topic, msg):
        self.mqtt.publish(topic, msg)


def main():
    print("Init MQTT client.")
    mqtt = Mqtt(IP_ADDRESS, PORT)

    while True:
        s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {'data':s}
        mqtt.sent_message("book/time", json.dumps(data))
        data = {'cpu_temp':psutil.sensors_temperatures()['coretemp'][0].current}
        mqtt.sent_message("book/cpu_temp", json.dumps(data))
        time.sleep(1)


if __name__ == "__main__":
    main()
    print( type(psutil.sensors_temperatures()['coretemp'][0]))
    print(psutil.sensors_temperatures()['coretemp'][0].current)