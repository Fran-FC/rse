# P1. Mininet
## Francesc Folch Company

### 1. Prueba a ejecutar el comando route en los diferentes dispositivos. Este comando se utiliza cuando se quiere trabajar con la tabla de enrutamiento IP/kernel. Se utiliza principalmente para configurar rutas estáticas a hosts o redes específicas a través de una interfaz. Se utiliza para mostrar o actualizar la tabla de enrutamiento IP/kernel.

```
mininet> c0 route
Kernel IP routing table
Destination     Gateway         Genmask         ...   Iface
default         fedora          0.0.0.0         ...   eth0
172.17.0.0      0.0.0.0         255.255.0.0     ...   eth0

mininet> h1 route
Kernel IP routing table
Destination     Gateway         Genmask         ...   Iface
10.0.0.0        0.0.0.0         255.0.0.0       ...   h1-eth0

mininet> h2 route
Kernel IP routing table:w
Destination     Gateway         Genmask         ...   Iface
10.0.0.0        0.0.0.0         255.0.0.0       ...   h2-eth0

mininet> s1 route 
Kernel IP routing table
Destination     Gateway         Genmask         ...   Iface
default         fedora          0.0.0.0         ...   eth0
172.17.0.0      0.0.0.0         255.255.0.0     ...   eth0
```

Como vemos, el Gateway de c0 es la máquina local que ejecuta ubuntu en una máquina virtual. 

### 2. Tras ejecutar `# mn --test pingall --topo linear,4` dibuja la estructura de red que obtienes con este ultimo.

<img src="images/ej2p1RSE.drawio.png" width="200px">

### 3. Utilizando `ping` calcula la diferencia con el caso sin definir los "link parameters".

Observamos que, con un link delay de 10ms, el retraso de un ping pasa a ser de 40ms, ya que se suman 10ms por cada nodo que pasa el mensaje (h1-s1, s1-h2, h2-s1, s1-h1).
```
mininet> h1 ping h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=43.3 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=43.0 ms
```
Mientras que una configuración con un link por defecto el delay por ping ronda en torno a 1ms.

### 4. Ahora repite lo mismo pero utilizando el comando iperf. ¿Como?

Midiendo el ancho de banda de los link entre h1 y h2 con la configuración de `# mn --link tc,bw=10,delay=10ms` obtenemos:
```
mininet> iperf
*** Iperf: testing TCP bandwidth between h1 and h2 
*** Results: ['8.64 Mbits/sec', '11.3 Mbits/sec']
```
Mientras que con una configuración estandar el ancho de banda llega a los 49Gbits/s.



