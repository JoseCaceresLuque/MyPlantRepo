import paho.mqtt.client as mqtt
import time
import datetime
import os

## message receive callback
def on_message(client, userdata, message):
    msg=str(message.payload.decode("utf-8"))
    print("message received " ,msg)
    print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
    f = open(today, "a")
    f.write("\n")
    f.write(message.topic+"\t"+msg)
    f.close()

####  connect callback
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=","bad call")

## returnt today date in a string
def dateString():
    x = datetime.datetime.today()
    day=x.strftime("%d")
    month=x.strftime("%B")
    year=x.strftime("%Y")
    today = day+"_"+month+"_"+year
    return today

#### create file with date Name
today = dateString()+".txt"
f = open(today, "a")
f.write("here the file start!")
f.close()


#host_name="localhost:1883"
host_name="192.168.0.143"
topic ="temperatura1"
#Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
client =mqtt.Client("p1")
client.on_connect=on_connect        #bind call back function
client.on_message=on_message        #attach function to callback

#connect(host, port=1883, keepalive=60, bind_address="")
client.connect(host_name)
client.loop_start()             #start the loop
client.subscribe(topic)

client.publish("prueba","toma eso cabron")

time.sleep(20) # wait
client.loop_stop() #stop the loop



