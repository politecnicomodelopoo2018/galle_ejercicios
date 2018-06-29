import json
from avion import Avion
from persona import Persona
from vuelos import Vuelos
from pasajeros import Pasajeros
from tripulacion import Tripulacion
from servicio import Servicio
class Sistema (object):

    def __init__(self):

        self.lista_persona = []

        self.lista_vuelos = []

        self.lista_aviones = []


    def pasajero_mas_joven(self , vuelo ): #ejercicio 2

        menor = None

        for item in vuelo.lista_pasajeros:

            for item2 in vuelo.lista_pasajeros:

                if item.fecha_nac < item2.fecha_nac:

                    menor = item2

        return menor



    def Vuelos_no_Habilitados (self): #ejercicio 4 parte 2

        lista_vuelos_no_autorizados = []

        for vuelos in self.lista_vuelos:

            if vuelos.Vuelos_no_Autorizados() == 0:

                lista_vuelos_no_autorizados.append(vuelos)


        return lista_vuelos_no_autorizados


    def cargarAvion(self):
        f=open("datos.json", "r")
        d=json.loads(f.read())
        for item in d["Aviones"]:
            unAvion=Avion()
            unAvion.deserializar(item)
            self.lista_aviones.append(unAvion)

        print(self.lista_aviones )

    def cargarPersonas(self):
        f=open("datos.json", "r")
        d=json.loads(f.read())
        for item in d["Personas"]:
            if item['tipo'] == 'Pasajero':
                unaPersona = Pasajeros()
                unaPersona.deserializar(item)
                self.lista_aviones.append(unaPersona)
            if item['tipo'] == 'Piloto':
                unaPersona = Pasajeros()
                unaPersona.deserializar(item)
                self.lista_aviones.append(unaPersona)
            if item['tipo'] == 'Servicio':
                unaPersona = Pasajeros()
                unaPersona.deserializar(item)
                self.lista_aviones.append(unaPersona)

        print(self.lista_persona )

    def cargarVuelo(self):
        f=open("datos.json", "r")
        d=json.loads(f.read())
        for item in d["Vuelos"]:
            unVuelo=Vuelos()
            unVuelo.deserializar(item)
            self.lista_vuelos.append(unVuelo)

        print(self.lista_vuelos )
