from tripulacion import Tripulacion

class Servicio (Tripulacion):

    def __init__(self):

        self.lista_idiomas = []


    def deserializar(self, unaPersona):
        self.nombre=unaPersona['nombre']
        self.apellido = unaPersona['apellido']
        self.fecha_nac = unaPersona['fechaNacimiento']
        self.DNI = unaPersona['dni']