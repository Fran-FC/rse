import paho.mqtt.client as mqtt

THE_BROKER = "test.mosquitto.org"
THE_TOPIC = "spain/valencia/upv/chat"
CLIENT_ID = "Fran"

def on_connect (client, userdata, flags, rc):
    client.subscribe(THE_TOPIC, qos=0)

def on_message(client, userdata, msg): 
    #print(msg.payload.decode("utf-8"))
    print("recieved: {}".format(msg.payload.decode("utf-8")))
    
client = mqtt.Client(client_id=CLIENT_ID,
                        clean_session=True,
                        userdata=None,
                        protocol=mqtt.MQTTv311,
                        transport="tcp")

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(CLIENT_ID, password=None)
client.connect(THE_BROKER, port=1883, keepalive=60)


client.loop_start()

while True:
    send_message = input()
    
    client.publish(THE_TOPIC,
                    payload=send_message,
                    qos=0,
                    retain=False)
    
client.loop_stop()
