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

