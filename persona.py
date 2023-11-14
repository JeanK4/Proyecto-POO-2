class Persona:
    def __init__(self, cedula=None, nombre=None, fechaNacimiento=None, genero=None, direccion=None, telefono=None, correo=None):
        self.cedula = cedula
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def getCedula(self):
        return self.cedula

    def getNombre(self):
        return self.nombre

    def getFechaNacimiento(self):
        return self.fechaNacimiento

    def getGenero(self):
        return self.genero

    def getDireccion(self):
        return self.direccion

    def getTelefono(self):
        return self.telefono

    def getCorreo(self):
        return self.correo

    def setCedula(self, cedula):
        self.cedula = cedula

    def setNombre(self, nombre):
        self.nombre = nombre

    def setFechaNacimiento(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento

    def setGenero(self, genero):
        self.genero = genero

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setCorreo(self, correo):
        self.correo = correo
