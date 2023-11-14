from usuario import Usuario
from aereonave import Aeronave, Avion, Helicoptero, Jets
import random

class UsuarioModel:
    def __init__(self):
        self.usuario = Usuario()

    def set_usuario(self, nickname, password):
        self.usuario.setNickname(nickname)
        self.usuario.setPassword(password)

    def get_usuario(self):
        return self.usuario

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


class Pasajero(Persona):
    def __init__(self, cedula=None, nombre=None, fechaNacimiento=None, genero=None, direccion=None, telefono=None, correo=None, nacionalidad=None, cntMaletas=None, infoMedica=None):
        super().__init__(cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo)
        self.nacionalidad = nacionalidad
        self.cntMaletas = cntMaletas
        self.infoMedica = infoMedica

    # Métodos getters y setters específicos para Pasajero
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

class Tripulante(Persona):
    def __init__(self, cedula = None, nombre = None, fechaNacimiento = None, genero = None, direccion = None, telefono = None, correo = None, puesto = None, experienciaAnos = None, horasMax = None):
        super().__init__(cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo)
        self.puesto = puesto
        self.experienciaAnos = experienciaAnos
        self.horasMax = horasMax

    # Métodos getters y setters específicos para Tripulante
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


class Vuelo:
    def __init__(self):
        self.hora = ""
        self.fecha = ""
        self.tipoVuelo = 0
        self.altitud = random.randint(10000, 12000)
        self.idPuerta = ""
        self.numIdent = ""
        self.ciudadOrigen = ""
        self.ciudadDestino = ""
        self.aeronaveAsignada = None
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

class PuertaEmbarque:
    def __init__(self, identificacion, ubicacion):
        self.disponible = True
        self.identificacion = identificacion
        self.ubicacion = ubicacion
        self.hora = ""
        self.vueloAsignado = None
        self.historial = []

    # Métodos getters y setters
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

    def addHistorial(self, fly: Vuelo):
        self.historial.append(fly)

class TorreControl:
    instance = None

    def __init__(self):
        self.Puertas = []

    def finalizarVuelo(self, numIdent, Aeropuerto):
        fly = None
        for i, vuelo in enumerate(Aeropuerto):
            if vuelo.getNumIdent() == numIdent:
                fly = vuelo
                del Aeropuerto[i]

    def solicitarAltitud(self, numIdent, Aeropuerto):
        for vuelo in Aeropuerto:
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
        for vuelo in Aeropuerto:
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
        fly = None
        for vuelo in Aeropuerto:
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

class AeronaveModelo:
    def __init__(self):
        self.aeronave = Aeronave()

    def obtener_aeronave(self):
        return self.aeronave

    def actualizar_aeronave(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos):
        self.aeronave.set_marca(marca)
        self.aeronave.set_modelo(modelo)
        self.aeronave.set_capacidad_pasajeros(capacidad_pasajeros)
        self.aeronave.set_velocidad_maxima(velocidad_maxima)
        self.aeronave.set_autonomia(autonomia)
        self.aeronave.set_ano_fabricacion(ano_fabricacion)
        self.aeronave.set_estado(estado)
        self.aeronave.set_ct_vuelos(ct_vuelos)

class AvionModelo(AeronaveModelo):
    def __init__(self):
        super().__init__()
        self.avion = Avion()

    def obtener_avion(self):
        return self.avion

    def actualizar_avion(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos, altitud_max, cant_motores):
        super().actualizar_aeronave(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos)
        self.avion.set_altitud_max(altitud_max)
        self.avion.set_cant_motores(cant_motores)

class HelicopteroModelo(AeronaveModelo):
    def __init__(self):
        super().__init__()
        self.helicoptero = Helicoptero()

    def obtener_helicoptero(self):
        return self.helicoptero

    def actualizar_helicoptero(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos, cnt_rotores, capacidad_elevacion, uso):
        super().actualizar_aeronave(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos)
        self.helicoptero.set_cnt_rotores(cnt_rotores)
        self.helicoptero.set_capacidad_elevacion(capacidad_elevacion)
        self.helicoptero.set_uso(uso)

class JetsModelo(AeronaveModelo):
    def __init__(self):
        super().__init__()
        self.jets = Jets()

    def obtener_jets(self):
        return self.jets

    def actualizar_jets(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos, propietario, servicios, destinos_frec):
        super().actualizar_aeronave(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, estado, ct_vuelos)
        self.jets.set_propietario(propietario)
        self.jets.set_servicios(servicios)
        self.jets.set_destinos_frec(destinos_frec)

class Aeropuerto:
    def __init__(self):
        self.vuelos = []

    def get_vuelos(self):
        return self.vuelos

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)