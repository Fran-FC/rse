import paho.mqtt.client as mqtt

mqtt_options = {
    "Broker": "eu1.cloud.thethings.network",
    "Username": "lopys2ttn@ttn",
    "Password": "NNSXS.A55Z2P4YCHH2RQ7ONQVXFCX2IPMPJQLXAPKQSWQ.A5AB4GALMW623GZMJEWNIVRQSMRMZF4CHDBTTEQYRAOFKBH35G2A",
    "Topic": "v3/+/devices/#"
}

def on_connect(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

    client.subscribe(mqtt_options["Topic"])
    
def on_message(client, userdata, msg):
    print(msg.payload.decode("utf-8"))

    
client = mqtt.Client(
    client_id="",
    clean_session=True,
    userdata=None,
    protocol=mqtt.MQTTv311,
    transport="tcp"
)

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(mqtt_options["Username"], password=mqtt_options["Password"])
client.connect(mqtt_options["Broker"])

client.loop_forever()



