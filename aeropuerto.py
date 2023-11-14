from pasajero import Pasajero
from vuelo import Vuelo
from aeronave import Helicoptero, Avion, Jets
from tripulante import Tripulante

class Aeropuerto:

    def __init__(self, nameAirport):
        self.nombre = nameAirport
        self.pasajeros = []
        self.puertas = []

    def getPuertas(self):
        return self.puertas

    def addPuerta(self, puerta):
        self.puertas.append(puerta)

    def getVuelos(self):
        return self.vuelos
    
    def getPasajeros(self):
        return self.pasajeros

    def addPasajero(self, passenger):
        self.pasajeros.append(passenger)

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

    def consultarVuelo(self):
        numvuelo = input("Ingrese un número de vuelo: ")
        flag = False

        for vuelo in self.vuelos:
            if (
                vuelo.getNumIdent() == numvuelo
                and vuelo.getAeronaveAsignada() is not None
            ):
                flag = True
                print("Número de Vuelo:", vuelo.getNumIdent())
                print("Ciudad de Origen:", vuelo.getCiudadOrigen())
                print("Ciudad de Destino:", vuelo.getCiudadDestino())
                print("Fecha del Vuelo:", vuelo.getFecha())
                print("Marca Aeronave:", vuelo.getAeronaveAsignada().get_marca())
                print("Modelo Aeronave:", vuelo.getAeronaveAsignada().get_modelo())
                print()

        if not flag:
            print("No se encontró un vuelo con ese número.")

    def anadirVuelo(self):
        flight = Vuelo()
        opcion = int(input("Digite el tipo de vuelo:\n1. Vuelo Comercial\n2. Vuelo de Carga\n3. Helicóptero\n4. Jet Privado\n"))
        flight.setTipoVuelo(opcion)
        x = 0
        tmp3 = None

        if len(self.vuelos) == 0 :
            if opcion == 1:
                marca = (input("Ingrese la marca del avión (texto): "))
                modelo = (int(input("Ingrese el modelo del avión (número): ")))
                capacidad_pasajeros = (int(input("Ingrese la cantidad de asientos del avión: ")))
                velocidad_maxima = (int(input("Ingrese la velocidad máxima del avión (número): ")))
                autonomia = (int(input("Ingrese la autonomía del avión (número): ")))
                ano_fabricacion = (int(input("Ingrese el año de fabricación del avión (número): ")))
                estado = 1
                ct_vuelos = x
                altitud_max = (input("Ingrese la altitud máxima del avión (texto): "))
                cant_motores = (int(input("Ingrese la cantidad de motores del avión (número): ")))
                AvionComercial = Avion(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, altitud_max, cant_motores)
                tmp3 = AvionComercial
            elif opcion == 2:
                marca = (input("Ingrese la marca del avión (texto): "))
                modelo = (int(input("Ingrese el modelo del avión (número): ")))
                capacidad_pasajeros = (int(input("Ingrese la cantidad de asientos del avión: ")))
                velocidad_maxima = (int(input("Ingrese la velocidad máxima del avión (número): ")))
                autonomia = (int(input("Ingrese la autonomía del avión (número): ")))
                ano_fabricacion = (int(input("Ingrese el año de fabricación del avión (número): ")))
                estado = 1
                ct_vuelos = x
                altitud_max = (input("Ingrese la altitud máxima del avión (texto): "))
                cant_motores = (int(input("Ingrese la cantidad de motores del avión (número): ")))
                AvionCarga = Avion(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, altitud_max, cant_motores)
                tmp3 = AvionCarga
            elif opcion == 3:
                Marca = (input("Ingrese la marca del helicóptero (texto): "))
                Modelo = (int(input("Ingrese el modelo del helicóptero (número): ")))
                CapacidadPasajeros = (int(input("Ingrese la cantidad de asientos del helicóptero: ")))
                VelocidadMaxima = (int(input("Ingrese la velocidad máxima del helicóptero (número): ")))
                Autonomia = (int(input("Ingrese la autonomía del helicóptero (número): ")))
                AnoFabricacion = (int(input("Ingrese el año de fabricación del helicóptero (número): ")))
                Estado = 1
                CtVuelos = x
                CntRotores = (int(input("Ingrese la cantidad de rotores del helicóptero (número): ")))
                CapacidadElevacion = (input("Ingrese la capacidad de elevación del helicóptero (texto): "))
                uso = int(input("Digite el tipo de uso:\n1. Rescate\n2. Turismo\n3. Transporte\n4. Medicina\n"))
                Uso = uso
                heli = Helicoptero(Marca, Modelo, CapacidadPasajeros, VelocidadMaxima, Autonomia, AnoFabricacion ,Estado, CntRotores, CapacidadElevacion, Uso)
                tmp3 = heli
            elif opcion == 4:

                Marca = (input("Ingrese la marca del jet (texto): "))
                Modelo = (int(input("Ingrese el modelo del jet (número): ")))
                CapacidadPasajeros = (int(input("Ingrese la cantidad de asientos del jet: ")))
                VelocidadMaxima = (int(input("Ingrese la velocidad máxima del jet (número): ")))
                Autonomia = (int(input("Ingrese la autonomía del jet (número): ")))
                AnoFabricacion = (int(input("Ingrese el año de fabricación del jet (número): ")))
                Estado = 1
                CtVuelos = x
                Propietario = (input("Ingrese el nombre del propietario del jet (texto): "))


                servicios = set()
                flag = False
                while not flag:
                    servicio = int(input("Digite el tipo de uso:\n1. Bar\n2. Entretenimiento VIP\n3. Dormitorio privado\n4. Chef privado\n5. Salir\n"))
                    if servicio == 5:
                        flag = True
                    elif servicio == 1:
                        servicios.add("Bar")
                    elif servicio == 2:
                        servicios.add("Entretenimiento VIP")
                    elif servicio == 3:
                        servicios.add("Dormitorio privado")
                    elif servicio == 4:
                        servicios.add("Chef privado")
                    else:
                        print("Opción inválida")

                Servicios = (list(servicios))

                destinos = set()
                ct = int(input("Digite cuántos destinos frecuentes desea (número): "))
                for i in range(ct):
                    destino = input("Digite los destinos Frecuentes (texto): ")
                    destinos.add(destino)

                DestinosFrec = (list(destinos))

                jet = Jets(Marca, Modelo, CapacidadPasajeros, VelocidadMaxima, Autonomia, AnoFabricacion, Estado, Propietario, Servicios, DestinosFrec)

                tmp3 = jet

            else:
                print("Opción inválida.")
            flight.setAeronaveAsignada(tmp3)
        else:
            naveAsignada = False
            for it in self.vuelos:
                if opcion == it.getTipoVuelo() and it.getAeronaveAsignada().getCtVuelos() < 3:
                    flight.setAeronaveAsignada(it.getAeronaveAsignada())
                    print(flight.getAeronaveAsignada().getMarca())
                    z = it.getAeronaveAsignada().getCtVuelos() + 1
                    it.getAeronaveAsignada().setCtVuelos(z)
                    naveAsignada = True
                    break

            if not naveAsignada:
                print("No hay naves disponibles con menos de 3 vuelos del tipo seleccionado, por favor, crea una nueva nave.")
                if opcion == 1:
                    marca = (input("Ingrese la marca del avión (texto): "))
                    modelo = (int(input("Ingrese el modelo del avión (número): ")))
                    capacidad_pasajeros = (int(input("Ingrese la cantidad de asientos del avión: ")))
                    velocidad_maxima = (int(input("Ingrese la velocidad máxima del avión (número): ")))
                    autonomia = (int(input("Ingrese la autonomía del avión (número): ")))
                    ano_fabricacion = (int(input("Ingrese el año de fabricación del avión (número): ")))
                    estado = 1
                    ct_vuelos = x
                    altitud_max = (input("Ingrese la altitud máxima del avión (texto): "))
                    cant_motores = (int(input("Ingrese la cantidad de motores del avión (número): ")))
                    AvionComercial = Avion(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia,
                                           ano_fabricacion, estado, altitud_max, cant_motores)
                    tmp3 = AvionComercial
                elif opcion == 2:
                    marca = (input("Ingrese la marca del avión (texto): "))
                    modelo = (int(input("Ingrese el modelo del avión (número): ")))
                    capacidad_pasajeros = (int(input("Ingrese la cantidad de asientos del avión: ")))
                    velocidad_maxima = (int(input("Ingrese la velocidad máxima del avión (número): ")))
                    autonomia = (int(input("Ingrese la autonomía del avión (número): ")))
                    ano_fabricacion = (int(input("Ingrese el año de fabricación del avión (número): ")))
                    estado = 1
                    ct_vuelos = x
                    altitud_max = (input("Ingrese la altitud máxima del avión (texto): "))
                    cant_motores = (int(input("Ingrese la cantidad de motores del avión (número): ")))
                    AvionCarga = Avion(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion,
                                       estado, altitud_max, cant_motores)
                    tmp3 = AvionCarga
                elif opcion == 3:
                    Marca = (input("Ingrese la marca del helicóptero (texto): "))
                    Modelo = (int(input("Ingrese el modelo del helicóptero (número): ")))
                    CapacidadPasajeros = (int(input("Ingrese la cantidad de asientos del helicóptero: ")))
                    VelocidadMaxima = (int(input("Ingrese la velocidad máxima del helicóptero (número): ")))
                    Autonomia = (int(input("Ingrese la autonomía del helicóptero (número): ")))
                    AnoFabricacion = (int(input("Ingrese el año de fabricación del helicóptero (número): ")))
                    Estado = 1
                    CtVuelos = x
                    CntRotores = (int(input("Ingrese la cantidad de rotores del helicóptero (número): ")))
                    CapacidadElevacion = (input("Ingrese la capacidad de elevación del helicóptero (texto): "))
                    uso = int(input("Digite el tipo de uso:\n1. Rescate\n2. Turismo\n3. Transporte\n4. Medicina\n"))
                    Uso = uso
                    heli = Helicoptero(Marca, Modelo, CapacidadPasajeros, VelocidadMaxima, Autonomia, AnoFabricacion,
                                       Estado, CntRotores, CapacidadElevacion, Uso)
                    tmp3 = heli
                elif opcion == 4:

                    Marca = (input("Ingrese la marca del jet (texto): "))
                    Modelo = (int(input("Ingrese el modelo del jet (número): ")))
                    CapacidadPasajeros = (int(input("Ingrese la cantidad de asientos del jet: ")))
                    VelocidadMaxima = (int(input("Ingrese la velocidad máxima del jet (número): ")))
                    Autonomia = (int(input("Ingrese la autonomía del jet (número): ")))
                    AnoFabricacion = (int(input("Ingrese el año de fabricación del jet (número): ")))
                    Estado = 1
                    CtVuelos = x
                    Propietario = (input("Ingrese el nombre del propietario del jet (texto): "))

                    servicios = set()
                    flag = False
                    while not flag:
                        servicio = int(input(
                            "Digite el tipo de uso:\n1. Bar\n2. Entretenimiento VIP\n3. Dormitorio privado\n4. Chef privado\n5. Salir\n"))
                        if servicio == 5:
                            flag = True
                        elif servicio == 1:
                            servicios.add("Bar")
                        elif servicio == 2:
                            servicios.add("Entretenimiento VIP")
                        elif servicio == 3:
                            servicios.add("Dormitorio privado")
                        elif servicio == 4:
                            servicios.add("Chef privado")
                        else:
                            print("Opción inválida")

                    Servicios = (list(servicios))

                    destinos = set()
                    ct = int(input("Digite cuántos destinos frecuentes desea (número): "))
                    for i in range(ct):
                        destino = input("Digite los destinos Frecuentes (texto): ")
                        destinos.add(destino)

                    DestinosFrec = (list(destinos))

                    jet = Jets(Marca, Modelo, CapacidadPasajeros, VelocidadMaxima, Autonomia, AnoFabricacion, Estado,
                               Propietario, Servicios, DestinosFrec)

                    tmp3 = jet

                else:
                    print("Opción inválida.")
            flight.setAeronaveAsignada(tmp3)

        capitan = Tripulante("12345", "Juan", "01/01/1980", "Masculino", "Calle 123", "123456789", "juan@gmail.com", "Capitan", 10, 1000)
        azafata = Tripulante("67890", "María", "05/12/1992", "Femenino", "Avenida Principal", "987654321", "maria@outlook.com", "Azafata", 5, 800)
        copiloto = Tripulante("6789", "Carlos", "02/05/1985", "Masculino", "Calle Principal 456", "987654321", "carlos@yahoo.es", "Copiloto", 8, 900)
        auxiliarDeVuelo = Tripulante("5678", "Laura", "15/09/1990", "Femenino", "Avenida Secundaria 789", "123456789", "laura@gmail.com", "Auxiliar de Vuelo", 6, 850)
        flight.addTripulantesAbordo(capitan)
        flight.addTripulantesAbordo(azafata)
        flight.addTripulantesAbordo(copiloto)
        flight.addTripulantesAbordo(auxiliarDeVuelo)
        num_ident = input("Digite el numero del vuelo: ")
        flight.setNumIdent(num_ident)

        fecha = input("Digite la fecha del vuelo(numero): ")
        flight.setFecha(fecha)

        ciudad_origen = input("Digite la ciudad de origen del vuelo(texto): ")
        flight.setCiudadOrigen(ciudad_origen)

        ciudad_destino = input("Digite la ciudad de destino del vuelo(texto): ")
        flight.setCiudadDestino(ciudad_destino)

        self.vuelos.append(flight)