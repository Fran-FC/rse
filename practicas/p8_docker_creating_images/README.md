# Practica 8 - creating a web page using Flask
## Francesc Folch Company

### 1. Describe el fichero Dockerfile
1. Se declara la imagen base desde donde partir 
2. Se instalan las dependencias (python, pip y flask)
3. Se copian los archivos `app.py` y `templates/index.html` en la imagen.
4. Se abre el puerto 5000.
5. Ejecutamos la aplicación `app.py` con Python3.

### 2. Cual es el uso del parámetro -p 8888:5000.
Se redirecciona el tráfico local del puerto 8888 al puerto 5000 del contenedor que hemos creado *myfirstapp*.

### 3. Nombre de la imagen Docker.
- [frafolcm/myfirstapp](https://hub.docker.com/r/frafolcm/myfirstapp)

### 4. Imagen docker para un subscriber al broker `broker.hivemq.com` para los mensajes con topic `test/#`.
La imagen se ha subido a DockerHub con el tag [frafolcm/thehub](https://hub.docker.com/r/frafolcm/thesub).