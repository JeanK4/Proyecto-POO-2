from vuelo import Vuelo
from aereonave import Avion, Helicoptero, Jets
class UsuarioController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def actualizar_usuario(self, nickname, password):
        self.model.set_usuario(nickname, password)

    def mostrar_usuario(self):
        usuario = self.model.get_usuario()
        self.view.mostrar_usuario(usuario)

class PersonaController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def set_persona(self, cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo):
        self.modelo.cedula = cedula
        self.modelo.nombre = nombre
        self.modelo.fechaNacimiento = fechaNacimiento
        self.modelo.genero = genero
        self.modelo.direccion = direccion
        self.modelo.telefono = telefono
        self.modelo.correo = correo

    def actualizar_vista(self):
        self.vista.imprimir_persona(self.modelo)

class PasajeroController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def set_pasajero(self, cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo, nacionalidad, cntMaletas, infoMedica):
        # Utilizamos los métodos set de la clase base para configurar la información personal
        self.modelo.setCedula(cedula)
        self.modelo.setNombre(nombre)
        self.modelo.setFechaNacimiento(fechaNacimiento)
        self.modelo.setGenero(genero)
        self.modelo.setDireccion(direccion)
        self.modelo.setTelefono(telefono)
        self.modelo.setCorreo(correo)

        # Configuramos la información específica de Pasajero
        self.modelo.setNacionalidad(nacionalidad)
        self.modelo.setCntMaletas(cntMaletas)
        self.modelo.setInfoMedica(infoMedica)

    def actualizar_vista(self):
        self.vista.imprimir_pasajero(self.modelo)

class TripulanteController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def set_tripulante(self, cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo, puesto, experienciaAnos, horasMax):
        # Utilizamos los métodos set de la clase base para configurar la información personal
        self.modelo.setCedula(cedula)
        self.modelo.setNombre(nombre)
        self.modelo.setFechaNacimiento(fechaNacimiento)
        self.modelo.setGenero(genero)
        self.modelo.setDireccion(direccion)
        self.modelo.setTelefono(telefono)
        self.modelo.setCorreo(correo)

        # Configuramos la información específica de Tripulante
        self.modelo.setPuesto(puesto)
        self.modelo.setExperienciaAnos(experienciaAnos)
        self.modelo.setHorasMax(horasMax)

    def actualizar_vista(self):
        self.vista.imprimir_tripulante(self.modelo)

class VueloController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def set_vuelo(self, numIdent, hora, fecha, ciudadOrigen, ciudadDestino, tipoVuelo):
        self.modelo.setNumIdent(numIdent)
        self.modelo.setHora(hora)
        self.modelo.setFecha(fecha)
        self.modelo.setCiudadOrigen(ciudadOrigen)
        self.modelo.setCiudadDestino(ciudadDestino)
        self.modelo.setTipoVuelo(tipoVuelo)

    def actualizar_vista(self):
        self.vista.imprimir_vuelo(self.modelo)

class PuertaEmbarqueController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def set_puerta_embarque(self, identificacion, ubicacion):
        self.modelo.setIdentificacion(identificacion)
        self.modelo.setUbicacion(ubicacion)

    def asignar_vuelo(self, vuelo):
        self.modelo.setVuelo(vuelo)

    def actualizar_vista(self):
        self.vista.imprimir_puerta_embarque(self.modelo)

class TorreControlController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def finalizar_vuelo(self, num_ident, aeropuerto):
        self.modelo.finalizarVuelo(num_ident, aeropuerto)

    def solicitar_altitud(self, num_ident, aeropuerto):
        self.modelo.solicitarAltitud(num_ident, aeropuerto)

    def asignar_puerta(self, aeropuerto):
        self.modelo.asignarPuerta(aeropuerto)

    def iniciar_vuelo(self, num_ident, aeropuerto):
        self.modelo.iniciarVuelo(num_ident, aeropuerto)

    def consultar_puertas(self):
        self.modelo.consultarPuertas()

    def add_puerta(self, puerta):
        self.modelo.addPuerta(puerta)

    def actualizar_vista(self):
        self.vista.imprimir_torre_control(self.modelo)

class AeronaveControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def obtener_aeronave(self):
        return self.modelo.obtener_aeronave()

    def actualizar_aeronave(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos):
        self.modelo.actualizar_aeronave(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos)
        #self.vista.imprimir_aeronave(self.modelo.obtener_aeronave())

class AvionControlador(AeronaveControlador):
    def __init__(self, modelo, vista):
        super().__init__(modelo, vista)

    def obtener_avion(self):
        return self.modelo.obtener_avion()

    def actualizar_avion(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos, altitud_max, cant_motores):
        self.modelo.actualizar_avion(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos, altitud_max, cant_motores)
        #self.vista.imprimir_avion(self.modelo.obtener_avion())

class HelicopteroControlador(AeronaveControlador):
    def __init__(self, modelo, vista):
        super().__init__(modelo, vista)

    def obtener_helicoptero(self):
        return self.modelo.obtener_helicoptero()

    def actualizar_helicoptero(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos, cnt_rotores, capacidad_elevacion, uso):
        self.modelo.actualizar_helicoptero(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos, cnt_rotores, capacidad_elevacion, uso)
        #self.vista.imprimir_helicoptero(self.modelo.obtener_helicoptero())

class JetsControlador(AeronaveControlador):
    def __init__(self, modelo, vista):
        super().__init__(modelo, vista)

    def obtener_jets(self):
        return self.modelo.obtener_jets()

    def actualizar_jets(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos, propietario, servicios, destinos_frec):
        self.modelo.actualizar_jets(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos, propietario, servicios, destinos_frec)
        #self.vista.imprimir_jets(self.modelo.obtener_jets())

class ControladorTotal:
    def __init__(self, modelo, vista, avion, helicoptero, jet, tripulante, vuelo):
        self.modelo = modelo
        self.vista = vista
        self.controllerAvion = avion
        self.controllerHelicoptero = helicoptero
        self.controllerJet = jet
        self.controllerTripulante = tripulante
        self.controllerVuelo = vuelo


    def ejecutar(self):
        opcion = 0
        while opcion != 4:
            self.vista.mostrar_menu()
            opcion = self.vista.obtener_opcion()

            if opcion == 1:
                self.reservar_vuelo()
            elif opcion == 2:
                self.consultar_vuelo()
            elif opcion == 3:
                self.anadir_vuelo()
            elif opcion == 4:
                self.vista.mostrar_mensaje("Saliendo del programa.")
            else:
                self.vista.mostrar_mensaje("Opción no válida. Inténtelo de nuevo.")

    def reservar_vuelo(self):
        if self.modelo.vuelos:
            # Mostrar opciones de vuelos disponibles
            for i, vuelo in enumerate(self.modelo.vuelos):
                aeronave = vuelo.getAeronaveAsignada()
                if (
                        aeronave.get_capacidad_pasajeros() > 0
                        and aeronave.get_ct_vuelos() < 3
                ):
                    print(
                        f"{i + 1}. Vuelo #{vuelo.getNumIdent()} programado para la fecha {vuelo.getFecha()} con ciudad de origen {vuelo.getCiudadOrigen()} y ciudad de destino {vuelo.getCiudadDestino()}"
                    )

            # Solicitar al usuario seleccionar un vuelo
            try:
                num_vuelo = int(input("Seleccione un vuelo -> ")) - 1
                if 0 <= num_vuelo < len(self.modelo.vuelos):
                    vuelo_seleccionado = self.modelo.vuelos[num_vuelo]

                    # Realizar la reserva
                    aeronave = vuelo_seleccionado.getAeronaveAsignada()
                    aeronave.set_capacidad_pasajeros(aeronave.get_capacidad_pasajeros() - 1)

                    if aeronave.get_capacidad_pasajeros() == 0:
                        aeronave.set_estado(2)
                        aeronave.set_ct_vuelos(aeronave.get_ct_vuelos() + 1)
                else:
                    print("Error: Número de vuelo no válido.")
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese un número válido.")

        else:
            print("No hay vuelos disponibles")

    def consultar_vuelo(self):
        num_vuelo = input("Ingrese un número de vuelo: ")
        flag = False

        for vuelo in self.modelo.vuelos:
            if (
                    vuelo.getNumIdent() == num_vuelo
                    and vuelo.getAeronaveAsignada() is not None
            ):
                flag = True
                print("Número de Vuelo:", vuelo.getNumIdent())
                print("Ciudad de Origen:", vuelo.getCiudadOrigen())
                print("Ciudad de Destino:", vuelo.getCiudadDestino())
                print("Fecha del Vuelo:", vuelo.getFecha())


        if not flag:
            print("No se encontró un vuelo con ese número.")

    def anadir_vuelo(self):
        flight = Vuelo()

        opcion = int(input("Digite el tipo de vuelo:\n1. Vuelo Comercial\n2. Vuelo de Carga\n3. Helicóptero\n4. Jet Privado\n"))
        flight.setTipoVuelo(opcion)
        x = 0
        tmp3 = None

        if len(self.modelo.vuelos) == 0:
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
                flight.setAeronaveAsignada(tmp3)
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
                self.controllerAvion.actualizar_avion(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, 0, altitud_max, cant_motores)
                AvionCarga = self.controllerAvion.obtener_avion()
                tmp3 = AvionCarga
                flight.setAeronaveAsignada(tmp3)
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
                heli = self.controllerHelicoptero.actualizar_helicoptero(Marca, Modelo, CapacidadPasajeros, VelocidadMaxima, Autonomia, AnoFabricacion ,Estado, CntRotores, CapacidadElevacion, Uso)
                tmp3 = heli
                flight.setAeronaveAsignada(tmp3)
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

                jet = self.controllerJet.actualizar_jets(Marca, Modelo, CapacidadPasajeros, VelocidadMaxima, Autonomia, AnoFabricacion, Estado, Propietario, Servicios, DestinosFrec)

                tmp3 = jet
                flight.setAeronaveAsignada(tmp3)
            else:
                print("Opción inválida.")

        else:
            naveAsignada = False
            for it in self.modelo.vuelos:
                if opcion == it.getTipoVuelo() and it.getAeronaveAsignada().get_ct_vuelos() < 3:
                    flight.setAeronaveAsignada(it.getAeronaveAsignada())
                    print(flight.getAeronaveAsignada().get_marca())
                    z = it.getAeronaveAsignada().get_ct_vuelos() + 1
                    it.getAeronaveAsignada().set_ct_vuelos(z)
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
                    self.controllerAvion.actualizar_avion(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia,ano_fabricacion, estado, 0, altitud_max, cant_motores)
                    AvionComercial = self.controllerAvion.obtener_avion()
                    tmp3 = AvionComercial
                    flight.setAeronaveAsignada(tmp3)
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
                    AvionCarga = self.controllerAvion.actualizar_avion(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion,estado, altitud_max, cant_motores)
                    tmp3 = AvionCarga
                    flight.setAeronaveAsignada(tmp3)
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
                    heli = self.controllerHelicoptero.actualizar_helicoptero(Marca, Modelo, CapacidadPasajeros, VelocidadMaxima, Autonomia, AnoFabricacion,
                                       Estado, CntRotores, CapacidadElevacion, Uso)
                    tmp3 = heli
                    flight.setAeronaveAsignada(tmp3)
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

                    jet = self.controllerJet.actualizar_jets(Marca, Modelo, CapacidadPasajeros, VelocidadMaxima, Autonomia, AnoFabricacion, Estado,
                               Propietario, Servicios, DestinosFrec)

                    tmp3 = jet
                    flight.setAeronaveAsignada(tmp3)

                else:
                    print("Opción inválida.")

        capitan = self.controllerTripulante.set_tripulante("12345", "Juan", "01/01/1980", "Masculino", "Calle 123", "123456789", "juan@gmail.com", "Capitan", 10, 1000)
        azafata = self.controllerTripulante.set_tripulante("67890", "María", "05/12/1992", "Femenino", "Avenida Principal", "987654321", "maria@outlook.com", "Azafata", 5, 800)
        copiloto = self.controllerTripulante.set_tripulante("6789", "Carlos", "02/05/1985", "Masculino", "Calle Principal 456", "987654321", "carlos@yahoo.es", "Copiloto", 8, 900)
        auxiliarDeVuelo = self.controllerTripulante.set_tripulante("5678", "Laura", "15/09/1990", "Femenino", "Avenida Secundaria 789", "123456789", "laura@gmail.com", "Auxiliar de Vuelo", 6, 850)
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

        self.modelo.vuelos.append(flight)
