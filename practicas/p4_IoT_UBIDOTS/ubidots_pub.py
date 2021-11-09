import paho.mqtt.client as mqtt
import json, random, time

broker = "industrial.api.ubidots.com"
topic = "/v1.6/devices/ffc_dev"

username = "BBFF-VpeiFJ10vcBONas4u9Zur50P8T9qBN"
passwd = None

def on_connect(client, userdata, flags, rc):
    print("Connected")

def on_publish(client, userdata, mid):
    print("published (mid={})".format(mid))

client = mqtt.Client(
    client_id=username,
    clean_session=True,
    userdata=None 
)

client.on_connect = on_connect
client.on_publish = on_publish

client.username_pw_set(username, password=passwd)
client.connect(broker, port=1883)

client.loop_start()

while True:
    send_message = json.dumps({"test_var": str(random.randint(0, 100))})
    #send_message = "{\"random_number\":{}}".format(random.randint(0,100))
    print("sending " + json.dumps(send_message))

    client.publish(
        topic,
        payload=send_message
    )
    time.sleep(1)

client.loop_stop()
