from pasajero import Pasajero
from vuelo import Vuelo
from aeronave import Helicoptero, Avion, Jets
from tripulante import Tripulante


class Aerolinea:

    def __init__(self, nameAerolinea):
        self.nameAerolinea = nameAerolinea
        self.vuelos = []
        self.aeronaves = []
        self.tripulacion = []
    
    def getTripulacion(self):
        return self.tripulacion
    
    def addTripulacion(self, tripulante):
        self.tripulacion.append(tripulante)

    def setPasajeroVuelo(self, pasajero, vuelo):
        for i in range(len(self.vuelos)):
            aeronave = self.vuelos[i].getAeronaveAsignada()
            print(aeronave.get_capacidad_pasajeros())
            if self.vuelos[i].getNumIdent() == vuelo and len(self.vuelos[i].getPersonasAbordo()) < aeronave.get_capacidad_pasajeros():
                self.vuelos[i].addPersonasAbordo(pasajero)

    def setAeronaveVuelo(self, numIdent, aeronave, tipo):
        for i in range(len(self.vuelos)):
            if self.vuelos[i].getNumIdent() == numIdent:
                if tipo == "Avión" and type(aeronave) is Avion:
                    tmp = aeronave.get_ct_vuelos()
                    aeronave.set_ct_vuelos(tmp+1)
                    if aeronave.get_ct_vuelos() == 3:
                        aeronave.set_estado(2)
                    self.vuelos[i].setAeronaveAsignada(aeronave)
                elif tipo == "Helicoptero" and type(aeronave) is Helicoptero:
                    tmp = aeronave.get_ct_vuelos()
                    aeronave.set_ct_vuelos(tmp + 1)
                    if aeronave.get_ct_vuelos() == 3:
                        aeronave.set_estado(2)
                    self.vuelos[i].setAeronaveAsignada(aeronave)
                elif tipo == "Jet" and type(aeronave) is Jets:
                    tmp = aeronave.get_ct_vuelos()
                    aeronave.set_ct_vuelos(tmp + 1)
                    if aeronave.get_ct_vuelos() == 3:
                        aeronave.set_estado(2)
                    self.vuelos[i].setAeronaveAsignada(aeronave)


    def buscarVueloModelo(self, modelo):
        for i in range(len(self.aeronaves)):
            if self.aeronaves[i].get_modelo() == modelo:
                aeronave = self.aeronaves[i]
        return aeronave

    def addVuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def getAeronaves(self):
        return self.aeronaves

    def addAeronave(self, aeronave):
        self.aeronaves.append(aeronave)

    def getVuelos(self):
        return self.vuelos

    def getNameAerolinea(self):
        return self.nameAerolinea

    def reservarVuelo(self):
        global opcion, numvuelo
        print("1. Vuelo Comercial")
        print("2. Vuelo de Carga")
        print("3. Helicóptero")
        print("4. Jet Privado")

        entradaValida = False
        while not entradaValida:
            try:
                opcion = int(input("Ingrese su opción: "))
                if opcion < 1 or opcion > 4:
                    raise ValueError
                entradaValida = True
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese un número entero válido (1-4).")

        if self.vuelos:
            permiso = True
            for i, vuelo in enumerate(self.vuelos):
                aeronave = vuelo.getAeronaveAsignada()
                if (
                        aeronave.get_capacidad_pasajeros() > 0
                        and aeronave.get_ct_vuelos() < 3
                        and vuelo.getTipoVuelo() == opcion
                ):
                    x = i + 1
                    permiso = False
                    print(
                        f"{x}. Vuelo #{vuelo.getNumIdent()} programado para la fecha {vuelo.getFecha()} con ciudad de origen {vuelo.getCiudadOrigen()} y ciudad de destino {vuelo.getCiudadDestino()}"
                    )

            if not permiso:
                entradaValida = False
                while not entradaValida:
                    try:
                        numvuelo = int(input("Seleccione un vuelo -> ")) - 1
                        if numvuelo < 0 or numvuelo >= len(self.vuelos):
                            raise ValueError
                        entradaValida = True
                    except ValueError:
                        print("Error: Entrada inválida. Por favor, ingrese un número válido.")

                vuelo_seleccionado = self.vuelos[numvuelo]
                aeronave = vuelo_seleccionado.getAeronaveAsignada()
                aeronave.set_capacidad_pasajeros(aeronave.get_capacidad_pasajeros() - 1)

                if aeronave.get_capacidad_pasajeros() == 0:
                    aeronave.set_estado(2)
                    aeronave.set_ct_vuelos(aeronave.get_ct_vuelos() + 1)

                usuario = Pasajero()
                usuario.setCedula(input("Ingrese su cedula: "))
                usuario.setNombre(input("Ingrese su nombre: "))
                usuario.setFechaNacimiento(input("Ingrese su fecha de nacimiento: "))
                usuario.setGenero(input("Ingrese su género: "))
                usuario.setDireccion(input("Ingrese su dirección: "))
                usuario.setTelefono(input("Ingrese su teléfono: "))
                usuario.setCorreo(input("Ingrese su correo: "))
                usuario.setNacionalidad(input("Ingrese su nacionalidad: "))
                usuario.setInfoMedica(input("Ingrese su información médica: "))
                usuario.setCntMaletas(int(input("Ingrese su cantidad de maletas: ")))

        else:
            print("No hay vuelos disponibles")