import paho.mqtt.client as mqtt
import time
import json
import random
from pymongo import MongoClient

DB_CONNECTION_STRING=f"mongodb://127.0.0.1:27017/" # set your mongodb connection string

def on_connect(client, userdata, flags, reason_code, properties):
     print(f"Connected with result code {reason_code}")
     client.subscribe("ecub/tx")
     client.subscribe("ecuf/tx")

count = 0

def on_message(client, userdata, msg):
    ran = random.randint(1, 10)
    try:
        json_data = json.loads(str(msg.payload.decode('utf-8')))
        print("Recieved from "+ str(userdata) + ": " + msg.topic+" -> "+ str(json_data))
        return_data="{\"user\":\"" + json_data['user'] + "\",\"command\":\"ecu\", \"data\":\"" +json_data['data']+"_"+str(ran)+ "\"}"

        if json_data['command'] == "to_ecub":
            print("Sending to ecub/rx..." +return_data)
            mqttc.publish('ecub/rx', return_data, qos=1)
        if json_data['command'] == "to_ecuf":
            print("Sending to ecuf/rx..." + return_data)
            mqttc.publish('ecuf/rx', return_data, qos=1)
    
        collection.insert_one({"userdata": userdata, "message": json_data})
    
    
    
    
    except(json.decoder.JSONDecodeError, KeyError):
        print("Error: Cannot parse: " + json_data)

def on_publish(client, userdata, mid, reason_code, properties):
    print("mid: "+str(mid))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("192.168.0.101", 8080, 60)

client = MongoClient(DB_CONNECTION_STRING)
db = client['car']
collection = db['messages']

mqttc.loop_forever()