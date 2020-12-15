import mqtt_link as mqtt
import json

mqtt_test = mqtt.MQTTLink("ece180d/MEAT/imu")

def handleIMU(action):
    mqtt_test.addText(action, "Siri")
    mqtt_test.send()

if __name__ == "__main__":
    handleIMU("test test")