
class TorreControl:
    instance = None

    def __init__(self):
        self.Puertas = []

    def finalizarVuelo(self, numIdent, Aeropuerto):
        vuelos = Aeropuerto.getVuelos()
        fly = None
        for i, vuelo in enumerate(vuelos):
            if vuelo.getNumIdent() == numIdent:
                fly = vuelo
                del vuelos[i]

    def solicitarAltitud(self, numIdent, Aeropuerto):
        vuelos = Aeropuerto.getVuelos()
        for vuelo in vuelos:
            if vuelo.getNumIdent() == numIdent:
                if vuelo.getAeronaveAsignada().get_estado() == 5:
                    print(f"Vuelo #{numIdent} con altitud: {vuelo.getAltitud()}")
                else:
                    print(f"Vuelo #{numIdent} no se encuentra en el aire")

    @staticmethod
    def getInstance():
        if TorreControl.instance is None:
            TorreControl.instance = TorreControl()
        return TorreControl.instance

    def asignarPuerta(self, Aeropuerto):
        flag = False
        i = 0
        vuelos = Aeropuerto.getVuelos()
        for vuelo in vuelos:
            if vuelo.getAeronaveAsignada().get_estado() == 2:
                while i < len(self.Puertas) and not flag:
                    if self.Puertas[i].getDisponible():
                        self.Puertas[i].setDisponible(False)
                        self.Puertas[i].addHistorial(vuelo)
                        vueloAsignado = vuelo
                        self.Puertas[i].setVuelo(vueloAsignado)
                        self.Puertas[i].setHora(vuelo.getHora())
                        vuelo.getAeronaveAsignada().set_estado(4)
                        vuelo.setIdPuerta(self.Puertas[i].getIdentificacion())
                        flag = True

                if not flag:
                    print("No hay puertas disponibles")

    def iniciarVuelo(self, numIdent, Aeropuerto):
        vuelos = Aeropuerto.getVuelos()
        fly = None
        for vuelo in vuelos:
            if vuelo.getNumIdent() == numIdent:
                fly = vuelo

        if fly.getAeronaveAsignada().get_estado() == 4:
            tmp = fly.getIdPuerta()
            for puerta in self.Puertas:
                if puerta.getIdentificacion() == tmp:
                    puerta.setDisponible(True)
                    fly.getAeronaveAsignada().set_estado(5)
                    puerta.setVuelo(None)
                    puerta.setHora("")
        else:
            print("No es posible iniciar el vuelo sin asignar una puerta con anterioridad")

    def consultarPuertas(self):
        for puerta in self.Puertas:
            print(f"Puerta #{puerta.getIdentificacion()}: ", end="")
            if puerta.getDisponible():
                print("Disponible, Ubicacion: " + puerta.getUbicacion())
            else:
                print("No Disponible, Ubicacion: " + puerta.getUbicacion())
                print("Numero de vuelo asignado: " + puerta.getVuelo().getNumIdent())

    def addPuerta(self, puerta):
        self.Puertas.append(puerta)

