from persona import Persona

class Tripulante(Persona):
    def __init__(self, cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo, puesto, experienciaAnos, horasMax):
        super().__init__(cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo)
        self.puesto = puesto
        self.experienciaAnos = experienciaAnos
        self.horasMax = horasMax

    def getPuesto(self):
        return self.puesto

    def getExperienciaAnos(self):
        return self.experienciaAnos

    def getHorasMax(self):
        return self.horasMax

    def setPuesto(self, puesto):
        self.puesto = puesto

    def setExperienciaAnos(self, experienciaAnos):
        self.experienciaAnos = experienciaAnos

    def setHorasMax(self, horasMax):
        self.horasMax = horasMax
