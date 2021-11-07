# Práctica 3. MQTT y Python

## Francesc Folch Company

### 1. Ejecuta sisub.py y explica el resultado obtenido.

El script `sisub.py` se conceta al broker test.mosquitto.org, que es utilizado para testear aplicaciones de IoT, una vez conectado, se suscribe al  *topic* $SYS, que como se ve en este [enlace](http://test.mosquitto.org/sys/) , coniene todos los *subtopics* de mosquitto. 

El manejador de eventos cuando se recibe un mensaje es la función `on_message` que simplemente mostrará el mensaje por consola , especificando el *topic* del mensaje y el *payload* asociado, es decir, el mensaje.

### 2. Ejecuta sipub.py y explica el resultado obtenido.

El script `sipub.py` se conecta a mosquitto de la misma manera, pero en lugar de añadir un *listener* para los mensajes entrantes, se define una función para cuando se publica un mensaje (`on_publish`), simplemente se mostrará por consola el mensaje publicado.


### 3. Modifica `sisub.py` para poder recibir los datos por `sipub.py`.

Para recibir mensajes solo de `sipub.py` habrá que modificar la variable `THE_TOPIC` para que coincida con el topic donde se publican los mensajes, en este caso `PMtest/rndvalue`.

### 4. Using the code from Question 3, set as topic for the “subscriber” the value Spain/Valencia/UPV and execute it. Now modify the code of the “producer” so that it uses the topic spain/valencia/upv and as the message use the text that you want. Execute the “producer”.

Los *topics* de MQTT son *case sensitive* por lo que hay que tener especial cuidado a la hora de utilizarlo, ya que aunque se esté publicado en el *topic* `spain/valencia/upv`, por el hecho de no haberse suscrito de manera correcta no se están recibiendo los mensajes correctos y en cambio se están recibiendo mensajes con el *payload* `b'caminhar'`.

### 5. Prueba los siguientes pasos:
- Publica un mensaje con la opcion de retained a “False”. ¿Qué recibe el “subscriber”?
    El *subscriber* no recibe nada, ya que se ha perdido el mensaje al no ser retenido.

- Publica un mensaje con la opcion de retained a “True”. ¿Qué recibe el “subscriber”?   
    Nada más conectarse recibirá el mensaje que envió el *publisher* antes de que el *subscriber* se conectara. 

- Publica varios mensajes (diferentes) con la opcion de retained a “True” antes de activar el “subscriber”.
    Nada más conectarse recibirá el último mensaje que envió el *publisher* antes de que el *subscriber* se conectara. Después seguirá recibiendo mensajes a medida que se vayan enviando.
    
### 6. Crea una aplicación de chat muy básica, donde todos los mensajes publicados de cualquiera de los miembros sean recibidos solo por los miembros del grupo.

Se ha creado el script chat.py, primero se establece un id del cliente aleatorio para asegurarse de que no hayan dos iguales (la mayoría de las veces, en este caso de prueba nos vale). Después se procederá a suscribirse al *topic* `spain/valencia/upv/chat`. Todos los miembros del grupo podrán enviar y recibir mensajes en ese *topic*.
```Python
import paho.mqtt.client as mqtt
import random

THE_BROKER = "test.mosquitto.org"
THE_TOPIC = "spain/valencia/upv/chat"
CLIENT_ID = str(random.randint(0, 100000)) # make sure it does not repeate

def on_connect (client, userdata, flags, rc):
    print("\n Connected  \n")
    client.subscribe(THE_TOPIC, qos=0)
    
def on_subscribe(client, userdata, flags, rc):
    print("\n subscribed \n")

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
client.on_subscribe = on_subscribe

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
```

### 7. Crea una aplicacion en python para replicar el ejemplo del Seminario 4 en el que, utilizando el cliente mqtt-explorer leiamos datos desde TTN. En este caso es suficiente imprimir todo el JSON que llega. 

```Python
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
```

Se mostrará el siguiente JSON:

```json
{
  "end_device_ids": {
    "device_id": "lopy3sense",
    "application_ids": {
      "application_id": "lopys2ttn"
    },
    "dev_eui": "70B3D5499EAA6C64",
    "join_eui": "70B3D57ED002AE7C",
    "dev_addr": "260B2681"
  },
  "correlation_ids": [
    "as:up:01FKXQDQYE7A7B77H972D8FCSQ",
    "gs:conn:01FKNQ3QGSJ3HBS3VMRMY0HNK8",
    "gs:up:host:01FKNQ3QHJR0K31XHZQ5MRX7VF",
    "gs:uplink:01FKXQDQQRY2GVG26DR4DK987B",
    "ns:uplink:01FKXQDQQTX3QYTSM0DRXVHH8R",
    "rpc:/ttn.lorawan.v3.GsNs/HandleUplink:01FKXQDQQSC1GRVAC6QM60DGKM",
    "rpc:/ttn.lorawan.v3.NsAs/HandleUplink:01FKXQDQYDX2E0C8CD9ERQ59SC"
  ],
  "received_at": "2021-11-07T17:34:04.239434664Z",
  "uplink_message": {
    "session_key_id": "AXx9ahQWLrp45Lpno7DT9w==",
    "f_port": 2,
    "f_cnt": 30204,
    "frm_payload": "QeHONEIH7Wi/gAAA",
    "decoded_payload": {
      "humidity": 33.981842041015625,
      "lux": -1,
      "temperature": 28.225685119628906
    },
    "rx_metadata": [
      {
        "gateway_ids": {
          "gateway_id": "main-gtw-grc",
          "eui": "B827EBFFFE7FE28A"
        },
        "time": "2021-11-07T17:34:03.998416Z",
        "timestamp": 1479021484,
        "rssi": -3,
        "channel_rssi": -3,
        "snr": 8.8,
        "location": {
          "latitude": 39.482534878470204,
          "longitude": -0.3463913363006933,
          "altitude": 9,
          "source": "SOURCE_REGISTRY"
        },
        "uplink_token": "ChoKGAoMbWFpbi1ndHctZ3JjEgi4J+v//n/iihCsp6DBBRoLCIycoIwGEJu12Asg4K+z5IXuPQ==",
        "channel_index": 7
      },
      {
        "gateway_ids": {
          "gateway_id": "rak-gtw-grc",
          "eui": "B827EBFFFE336296"
        },
        "timestamp": 4058875412,
        "rssi": -99,
        "channel_rssi": -99,
        "snr": 6,
        "location": {
          "latitude": 39.48272119427445,
          "longitude": -0.3471749450839346,
          "altitude": 9,
          "source": "SOURCE_REGISTRY"
        },
        "uplink_token": "ChkKFwoLcmFrLWd0dy1ncmMSCLgn6//+M2KWEJSMto8PGgsIjJygjAYQlqiJDyCg/M6+kLw9",
        "channel_index": 7
      },
      {
        "gateway_ids": {
          "gateway_id": "packetbroker"
        },
        "packet_broker": {
          "message_id": "01FKXQDQSE6Q1J45XW56TCP51W",
          "forwarder_net_id": "000013",
          "forwarder_tenant_id": "ttnv2",
          "forwarder_cluster_id": "ttn-v2-eu-3",
          "forwarder_gateway_eui": "3133303725006A00",
          "forwarder_gateway_id": "eui-3133303725006a00",
          "home_network_net_id": "000013",
          "home_network_tenant_id": "ttn",
          "home_network_cluster_id": "eu1.cloud.thethings.network"
        },
        "time": "2021-11-07T17:34:26.196177Z",
        "rssi": -98,
        "channel_rssi": -98,
        "snr": 7,
        "location": {
          "latitude": 39.47876459,
          "longitude": -0.33391551
        },
        "uplink_token": "eyJnIjoiWlhsS2FHSkhZMmxQYVVwQ1RWUkpORkl3VGs1VE1XTnBURU5LYkdKdFRXbFBhVXBDVFZSSk5GSXdUazVKYVhkcFlWaFphVTlwU1hoVFYzaE1XbXBHVEdKR1VrSmFNakZzVlROQ2VFbHBkMmxrUjBadVNXcHZhVTFHUmtOaVNHUjJUVEpXYWxwVmVFdGFXRUpNWVZjMVMxUnViR2hrZVVvNUxubFJjREl0WldabU5GcFdjbTFvV0daUlFVMHdWMmN1VkZoNVlVSmtRM1JKYlRKNWNuQnBVaTQxTTBzMmVXMURaRWxFVDBONlN6WmFaWEJ6YW1weE1rWXpUazQxVUdKNGNYUktNa0pFTFVkYWFFeElSbUptY0hjM2RVazRXa2RUVURsM1NrbHJaSGhUWjJKa05FOXVUR3h4T1VGNU5Xd3RWSE4zYUZCSFdXOU5lbkZQV0ZoMVpGaDJaMlpVTVRGdE9WQnlNMlp6Y21jM2VGa3lNM1UzV1c5aVJYZGhjSEJ4WkZwbGJHRnFjR1JFTTNWdGNsSjBjWEZDVFZsV1dEWjZUa2R4WWxWRGIzaGxUM0JXTW5wYVkyWlVRUzVDV2xKS1RsaFFhV2RCVlhoV1UxOHRTWGhJWlRobiIsImEiOnsiZm5pZCI6IjAwMDAxMyIsImZ0aWQiOiJ0dG52MiIsImZjaWQiOiJ0dG4tdjItZXUtMyJ9fQ=="
      }
    ],
    "settings": {
      "data_rate": {
        "lora": {
          "bandwidth": 125000,
          "spreading_factor": 12
        }
      },
      "coding_rate": "4/5",
      "frequency": "867900000",
      "timestamp": 1479021484,
      "time": "2021-11-07T17:34:03.998416Z"
    },
    "received_at": "2021-11-07T17:34:04.026085747Z",
    "consumed_airtime": "1.482752s",
    "network_ids": {
      "net_id": "000013",
      "tenant_id": "ttn",
      "cluster_id": "ttn-eu1"
    }
  }
}
```

