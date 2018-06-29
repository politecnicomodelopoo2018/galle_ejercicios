class Vuelos (object):

    avion = None

    fecha = None

    hora = None

    origen = None

    destino = None

    def __init__(self):

        self.lista_pasajeros = []

        self.lista_tripulantes = []

    def deserializar(self, unVuelo):
        self.avion=unVuelo['avion']
        self.fecha = unVuelo['fecha']
        self.hora = unVuelo['hora']
        self.origen = unVuelo['origen']
        self.destino = unVuelo['destino']
        self.lista_pasajeros = unVuelo['pasajeros']#preguntar profe
        self.lista_tripulantes = unVuelo['tripulacion']#preguntar profe



    def personas_por_vuelo (self): #ejercicio 1

        return self.lista_pasajeros



    def Cantidad_necesaria(self):#ejercicio 3


        if len(self.lista_tripulantes) < self.avion.cant_necesaria_tripulantes:

            return "El vuelo no alcanza tripulacion minima"

        else:

            return "El vuelo si alcanza tripulacion minima"



    def Vuelos_no_Autorizados(self):  #ejercicio 4 parte 1

        for tripulante in self.lista_tripulantes:

            for avionesPuedeVolar in tripulante.lista_modelos_aviones:

                if avionesPuedeVolar == self.avion.modelo_avion:

                    return 1

                else:

                    return 0



    def Personas_VIP_Especiales(self): #ejercicio 6

        lista_personas_VIP_o_especiales = []

        for item in self.lista_pasajeros:

            if item.vip == 1 or item.necesidades_especiales != None:

               lista_personas_VIP_o_especiales.append(item)



    def Idiomas_Hablados_Por_Vuelo(self): #ejercicio 7

        lista_idiomas_por_vuelo = []

        for item in self.lista_tripulantes:

            if item.__name__ == 'Servicio':

                for idioma in item.lista_idiomas:

                    if idioma not in lista_idiomas_por_vuelo:

                        lista_idiomas_por_vuelo.append(idioma)

        return lista_idiomas_por_vuelo