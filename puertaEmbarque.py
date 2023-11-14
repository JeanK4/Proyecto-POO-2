from vuelo import Vuelo


class PuertaEmbarque:
    def __init__(self, identificacion, ubicacion):
        self.disponible = True
        self.identificacion = identificacion
        self.ubicacion = ubicacion
        self.hora = ""
        self.vueloAsignado = None
        self.historial = []

    def addHistorial(self, fly: Vuelo):
        self.historial.append(fly)

    def getDisponible(self):
        return self.disponible

    def getIdentificacion(self):
        return self.identificacion

    def getUbicacion(self):
        return self.ubicacion

    def getHora(self):
        return self.hora

    def getVuelo(self):
        return self.vueloAsignado

    def getHistorial(self):
        return self.historial

    def setDisponible(self, estado):
        self.disponible = estado

    def setIdentificacion(self, ID):
        self.identificacion = ID

    def setUbicacion(self, Ubicacion):
        self.ubicacion = Ubicacion

    def setHora(self, Hora):
        self.hora = Hora

    def setVuelo(self, fly: Vuelo):
        self.vueloAsignado = fly
