import random

class Vuelo:
    def __init__(self, hora, fecha, numIdent, ciudadOrigen, ciudadDestino, aeronaveAsignada):
        self.hora = hora
        self.fecha = fecha
        self.tipoVuelo = 0
        self.altitud = random.randint(10000, 12000)
        self.idPuerta = ""
        self.numIdent = numIdent
        self.ciudadOrigen = ciudadOrigen
        self.ciudadDestino = ciudadDestino
        self.aeronaveAsignada = aeronaveAsignada
        self.personasAbordo = []
        self.tripulantesAbordo = []

    def getNumIdent(self):
        return self.numIdent

    def getAltitud(self):
        return self.altitud

    def getFecha(self):
        return self.fecha

    def getCiudadOrigen(self):
        return self.ciudadOrigen

    def getTipoVuelo(self):
        return self.tipoVuelo

    def getCiudadDestino(self):
        return self.ciudadDestino

    def getPersonasAbordo(self):
        return self.personasAbordo

    def getLenPersonasAbordo(self):
        return len(self.personasAbordo)

    def getAeronaveAsignada(self):
        return self.aeronaveAsignada

    def getTripulantesAbordo(self):
        return self.tripulantesAbordo

    def setNumIdent(self, NumID):
        self.numIdent = NumID

    def setFecha(self, Fecha):
        self.fecha = Fecha

    def setCiudadOrigen(self, COrigen):
        self.ciudadOrigen = COrigen

    def setCiudadDestino(self, CDestino):
        self.ciudadDestino = CDestino

    def addPersonasAbordo(self, p):
        self.personasAbordo.append(p)

    def setAeronaveAsignada(self, n):
        self.aeronaveAsignada = n

    def addTripulantesAbordo(self, t):
        self.tripulantesAbordo.append(t)

    def setTipoVuelo(self, x):
        self.tipoVuelo = x

    def getIdPuerta(self):
        return self.idPuerta

    def setIdPuerta(self, identificacion):
        self.idPuerta = identificacion

    def getHora(self):
        return self.hora

    def setHora(self, hour):
        self.hora = hour
