class Persona (object):

    nombre = None

    apellido = None

    fecha_nac = None

    DNI = None


    def agregarPersona (self,nombre,apellido,DNI,fecha_nac):

        self.nombre = nombre

        self.apellido = apellido

        self.fecha_nac = fecha_nac

        self.DNI = DNI



    def deserializar(self, unaPersona):
        self.nombre=unaPersona['nombre']
        self.apellido = unaPersona['apellido']
        self.fecha_nac = unaPersona['fechaNacimiento']
        self.DNI = unaPersona['dni']
