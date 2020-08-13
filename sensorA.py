import paho.mqtt.client as mqtt
import time
import datetime
import os
import random

random.seed(2)


## message receive callback
def on_message(client, userdata, message):
    msg=str(message.payload.decode("utf-8"))
    print("message received " ,msg)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    f = open(today, "a")
    f.write("\n")
    f.write(msg)
    f.close()

####  connect callback
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=","bad call")


#host_name="localhost:1883"
host_name="192.168.0.143"
topic ="prueba"
#Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
client =mqtt.Client("p2")
client.on_connect=on_connect        #bind call back function
client.on_message=on_message        #attach function to callback

#connect(host, port=1883, keepalive=60, bind_address="")
client.connect(host_name)
client.loop_start()             #start the loop

for i in range(10):
    temp1 =str(random.random()+i)
    temp2 =str(random.random()+i)

    client.publish("temperatura1",temp1)
    client.publish("temperatura2",temp2)
    print(temp1)
    print(temp2)
    time.sleep(1) # wait

client.loop_stop() #stop the loop
