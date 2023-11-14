from persona import Persona

class Pasajero(Persona):
    def __init__(self, cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo, nacionalidad, cntMaletas, infoMedica):
        super().__init__(cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo)
        self.nacionalidad = nacionalidad
        self.cntMaletas = cntMaletas
        self.infoMedica = infoMedica

    def getNacionalidad(self):
        return self.nacionalidad

    def getCntMaletas(self):
        return self.cntMaletas

    def getInfoMedica(self):
        return self.infoMedica

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def setCntMaletas(self, cntMaletas):
        self.cntMaletas = cntMaletas

    def setInfoMedica(self, infoMedica):
        self.infoMedica = infoMedica
