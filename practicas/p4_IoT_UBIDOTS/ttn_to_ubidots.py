import time, json
import paho.mqtt.client as mqtt

ttn_options = {
    "Broker": "eu1.cloud.thethings.network",
    "Topic": "v3/+/devices/#",
    "Username": "lopys2ttn@ttn",
    "Password": "NNSXS.A55Z2P4YCHH2RQ7ONQVXFCX2IPMPJQLXAPKQSWQ.A5AB4GALMW623GZMJEWNIVRQSMRMZF4CHDBTTEQYRAOFKBH35G2A"
} 

ubidots_options = {
    "Broker": "industrial.api.ubidots.com",
    "Topic": "/v1.6/devices/ffc_dev",
    "Username": "BBFF-VpeiFJ10vcBONas4u9Zur50P8T9qBN",
    "Password": None
}

def on_connectTTN(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

    client.subscribe(ttn_options["Topic"])

def on_connectUBI(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

# The callback for when a message is received from the server.
def on_messageTTN(client, userdata, msg):
#    print("sisub: msg received with topic: {} and payload: {}".format(msg.topic, str(msg.payload)))
    print("sisub: msg received with topic: {} ".format(msg.topic))

    if (msg.topic == "v3/lopys2ttn@ttn/devices/lopy4sense/up"):

        themsg = json.loads(msg.payload.decode("utf-8"))
        dpayload = themsg["uplink_message"]["decoded_payload"]
        print(dpayload["temperature"])
        
        # craft message to publish in ubidots
        ubi_msg = {"ttn_temperature" : dpayload["temperature"]}

       # print("@%s >> temp=%.3f hum=%.3f lux=%.3f" % (time.strftime("%H:%M:%S"), dpayload["temperature"], dpayload["lux"], dpayload["humidity"]))

        clientUBI.publish(
            ubidots_options["Topic"],
            payload=json.dumps(ubi_msg)
        )



clientTTN = mqtt.Client()
clientUBI = mqtt.Client()

clientTTN.on_connect = on_connectTTN
clientTTN.on_message = on_messageTTN
clientUBI.on_connect = on_connectUBI

clientTTN.username_pw_set(ttn_options["Username"], password=ttn_options["Password"])
clientTTN.connect(ttn_options["Broker"])

clientUBI.username_pw_set(ubidots_options["Username"], ubidots_options["Password"])
clientUBI.connect(ubidots_options["Broker"])

clientTTN.loop_forever()
