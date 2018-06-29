class Avion (object):

    modelo_avion = None

    cant_max_pasajeros = None

    cant_necesaria_tripulantes = None



    def deserializar(self, unAvion):
        self.modelo_avion=unAvion['codigoUnico']
        self.cant_max_pasajeros = unAvion['cantidadDePasajerosMaxima']
        self.cant_necesaria_tripulantes = unAvion['cantidadDeTripulaciónNecesaria']
