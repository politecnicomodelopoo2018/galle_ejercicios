from persona import Persona

class Tripulacion (Persona):

    habilitacion_vuelo = None

    def __init__(self):

        self.lista_modelos_aviones = []



    def deserializar(self, unaPersona):
        self.nombre=unaPersona['nombre']
        self.apellido = unaPersona['apellido']
        self.fecha_nac = unaPersona['fechaNacimiento']
        self.DNI = unaPersona['dni']


