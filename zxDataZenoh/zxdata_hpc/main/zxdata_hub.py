import paho.mqtt.client as mqtt
import time
import json

def on_connect(client, userdata, flags, reason_code, properties):
  print(f"Connected with result code {reason_code}")
  client.subscribe("zxdata/move1")
  client.subscribe("zxdata/move2")

def on_message(client, userdata, msg):
  print("Recieved: " + msg.topic+" "+str(msg.payload))
  json_data = json.loads(str(msg.payload)
  if json_data['command'] == "move":
    mqttc.publish('zxdata/display1', json_data['data'], qos=1)






def on_publish(client, userdata, mid, reason_code, properties):
  print("mid: "+str(mid))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("192.168.0.101", 8080, 60)
mqttc.loop_forever()
