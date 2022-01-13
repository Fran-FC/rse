# P9. Docker Thread
## Francesc Folch Company

### 1. Indica los datos del “Operation Dataset” que has creato:
- Network Key: c5ed76596401db8ea08af4ad0c8ca450
- Network Name: OpenThread-33d7
- PAN ID: 0x33d7


### 2. Indica la direccion link-local de tu dispositivo.
- link-local: fe80:0:0:0:b473:cb03:79c7:a841

### 3. Indica el Endpoint Identifier (EID) de tu dispositivo.
- EID: fda4:8632:fe78:4813:710:5451:9e0b:925c

### 4. Indica la latencia del ping al node 1 desde el node 2.

Tal y como se muestra en el output:

```
> ping fda4:8632:fe78:4813:710:5451:9e0b:925c
16 bytes from fda4:8632:fe78:4813:710:5451:9e0b:925c: icmp_seq=1 hlim=64 time=7ms
1 packets transmitted, 1 packets received. Packet loss = 0.0%. Round-trip min/avg/max = 7/7.0/7 ms.
```

Hay 7ms de latencia.

### 5. Indica el documento a entregar el mensaje obtenido en pantalla despues del Join.

```
Commissioner: Joiner connect d65e64fa83f81cf7
00:03:52.526 [NONE]-MESH-CP-: =========[[THCI] direction=recv | type=JOIN_FIN.req | len=047]==========
00:03:52.526 [NONE]-MESH-CP-: | 10 01 01 21 0A 4F 50 45 | 4E 54 48 52 45 41 44 22 | ...!.OPENTHREAD"
00:03:52.526 [NONE]-MESH-CP-: | 0A 53 49 4D 55 4C 41 54 | 49 4F 4E 23 0A 67 37 31 | .SIMULATION#.g71
00:03:52.526 [NONE]-MESH-CP-: | 65 62 61 63 63 61 35 25 | 06 18 B4 30 00 00 10 .. | ebacca5%..40....
00:03:52.526 [NONE]-MESH-CP-: ------------------------------------------------------------------------
00:03:52.526 [NONE]-MESH-CP-: =========[[THCI] direction=send | type=JOIN_FIN.rsp | len=003]==========
00:03:52.526 [NONE]-MESH-CP-: | 10 01 01 .. .. .. .. .. | .. .. .. .. .. .. .. .. | ................
00:03:52.526 [NONE]-MESH-CP-: ------------------------------------------------------------------------
```


