import paho.mqtt.client as mqtt
import time
import json

def on_connect(client, userdata, flags, reason_code, properties):
     print(f"Connected with result code {reason_code}")
     client.subscribe("move1")
     client.subscribe("move2")

def on_message(client, userdata, msg):
    print("Recieved from "+ str(userdata) + ": " + msg.topic+" "+str(msg.payload.decode('utf-8')))
    try:
        json_data = json.loads(str(msg.payload.decode('utf-8')))

        if json_data['command'] == "move2":
            print("Sending to disp2..." + str(json_data['data']))
            mqttc.publish('disp2', "{\"command\":\"display\", \"data\":\"" +json_data['data']+"\"}", qos=1)
        if json_data['command'] == "move1":
            print("Sending to disp1..." + str(json_data['data']))
            mqttc.publish('disp1', "{\"command\":\"display\", \"data\":\"" +json_data['data']+"\"}", qos=1)
    except(json.decoder.JSONDecodeError):
        print("Error: Cannot parse: " + str(msg.payload.decode('utf-8')))

def on_publish(client, userdata, mid, reason_code, properties):
    print("mid: "+str(mid))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("192.168.0.101", 8080, 60)
#mqttc.loop_forever()

mqttc.loop_start()

while True:
    mqttc.publish('disp1', "{\"command\":\"display\", \"data\":\"display1\"}", qos=1)
    print("Sending to display1 ...")
    time.sleep(5)