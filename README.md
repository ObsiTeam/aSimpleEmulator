# aSimpleEmulator
VR Glasses with Arduino &amp; Python
El Primer paso es descargar Python3.7.4 marcando en el instalador la casilla de Add Python PATH y tras ello, instalar
los móludos necesarios los cuales son:

WINDOWS:
pip install flask
pip install serial
pip install pyserial
pip install pyscreenshot
pip install pywin32


LINUX:
pip3 install flask
pip3 install serial
pip3 install pyserial
pip3 install pyscreenshot
pip3 install pywin32


El Segundo paso es descargar ARDUINO con su librería wire.h en caso de que no venga incluida en el setup

Para abrir asisi.ino solo hay que seleccionar el archivo y subirlo a la placa Arduino


El Tercero paso es utilizar python para abrir el archivo asisi.py con la placa Arduino aun conectada
y tras ello, realizar una conexión fuera o dentro de LAN

Server interno: ejecutar el archivo screen.py en el equipo server y conectarse a la direccion del server con el puerto 5000 desde el equipo cliente

Server externo: discord/skype/gotomeeting/anydesk/teamviewer ect...

GAFAS: https://es.rs-online.com/web/p/gafas-de-seguridad/1845936/
CABLES: https://www.amazon.es/Bheema-cables-puente-hembra-Arduino/dp/B00INWWVKY
ARDUINO: https://es.aliexpress.com/item/32823856284.html
MODULO: https://es.aliexpress.com/item/32957289299.html
CABLE: https://es.aliexpress.com/item/32787738829.html

[!] Si no eres desarrollador ni sabes nada de programación, no cambies esto [!]


Customizar controles:
DELANTE: asisi.py linea: 134 / 140
DETRAS: asisi.py linea: 137 / 141
DERECHA: asisi.py linea: 128
IZQUIERDA: asisi.py linea: 124


Customizar sesibilidad:
DERECHA: asisi.py linea: 125
IZQUIERDA: asisi.py linea: 121


YOUTUBE: www.youtube.com/c/masonrapa
TWITTER: www.twitter.com/masonrapa
INSTAGRAM: www.instagram.com/masonrapa
GITHUB: www.github.com/masonrapa

INDEX: sites.google.com/view/masonrapa
