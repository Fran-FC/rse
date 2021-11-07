# Práctica 3. MQTT y Python

## Francesc Folch Company

### 1. Ejecuta sisub.py y explica el resultado obtenido.

El script `sisub.py` se conceta al broker test.mosquitto.org, que es utilizado para testear aplicaciones de IoT, una vez conectado, se suscribe al  *topic* $SYS, que como se ve en este [enlace](http://test.mosquitto.org/sys/) , coniene todos los *subtopics* de mosquitto. 

El manejador de eventos cuando se recibe un mensaje es la función `on_message` que simplemente mostrará el mensaje por consola , especificando el *topic* del mensaje y el *payload* asociado.
