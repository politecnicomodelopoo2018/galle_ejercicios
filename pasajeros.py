from persona import Persona

class Pasajeros (Persona):

    vip = None

    necesidades_especiales = None


    def deserializar(self, unaPersona):
        Persona.deserializar(self, unaPersona)
        self.vip=unaPersona['vip']

        try:

            solicitudAux = Persona['solicitudesEspeciales']

        except:

             pass
        self.necesidades_especiales = solicitudAux























