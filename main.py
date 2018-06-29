import json
import datetime
from persona import Persona
from tripulacion import Tripulacion
from servicio import Servicio
from pasajeros import Pasajeros
from sistema import Sistema
from vuelos import Vuelos
from avion import Avion

a = Sistema()
a.cargar()




f = open('datos.json',r)

diccionario = json.loads(f.read())
