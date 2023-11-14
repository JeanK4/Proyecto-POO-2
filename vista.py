class UsuarioView:
    def mostrar_usuario(self, usuario):
        print(f"Nickname: {usuario.getNickname()}")
        print(f"Password: {usuario.getPassword()}")

class PersonaView:
    def imprimir_persona(self, persona):
        print(f"Cedula: {persona.cedula}")
        print(f"Nombre: {persona.nombre}")
        print(f"Fecha de Nacimiento: {persona.fechaNacimiento}")
        print(f"Genero: {persona.genero}")
        print(f"Direccion: {persona.direccion}")
        print(f"Telefono: {persona.telefono}")
        print(f"Correo: {persona.correo}")

class PasajeroView(PersonaView):
    def imprimir_pasajero(self, pasajero):
        print("Información del Pasajero:")
        print(f"Nacionalidad: {pasajero.getNacionalidad()}")
        print(f"Cantidad de Maletas: {pasajero.getCntMaletas()}")
        print(f"Información Médica: {pasajero.getInfoMedica()}")
        # También podemos imprimir la información de la persona llamando al método de la clase base
        super().imprimir_persona(pasajero)

class TripulanteView(PersonaView):
    def imprimir_tripulante(self, tripulante):
        print("Información del Tripulante:")
        print(f"Puesto: {tripulante.getPuesto()}")
        print(f"Años de Experiencia: {tripulante.getExperienciaAnos()}")
        print(f"Horas Máximas de Vuelo: {tripulante.getHorasMax()}")
        # También podemos imprimir la información de la persona llamando al método de la clase base
        super().imprimir_persona(tripulante)

class VueloView:
    def imprimir_vuelo(self, vuelo):
        print("Información del Vuelo:")
        print(f"Número de Identificación: {vuelo.getNumIdent()}")
        print(f"Hora: {vuelo.getHora()}")
        print(f"Fecha: {vuelo.getFecha()}")
        print(f"Ciudad de Origen: {vuelo.getCiudadOrigen()}")
        print(f"Ciudad de Destino: {vuelo.getCiudadDestino()}")
        print(f"Altitud: {vuelo.getAltitud()}")
        print(f"Aeronave Asignada: {vuelo.getAeronaveAsignada()}")
        print(f"Tipo de Vuelo: {vuelo.getTipoVuelo()}")
        print(f"Personas a Bordo: {vuelo.getPersonasAbordo()}")
        print(f"Tripulantes a Bordo: {vuelo.getTripulantesAbordo()}")

class PuertaEmbarqueView:
    def imprimir_puerta_embarque(self, puerta):
        print("Información de la Puerta de Embarque:")
        print(f"Identificación: {puerta.getIdentificacion()}")
        print(f"Ubicación: {puerta.getUbicacion()}")
        print(f"Hora: {puerta.getHora()}")
        print(f"Disponible: {puerta.getDisponible()}")
        print(f"Vuelo Asignado: {puerta.getVuelo()}")
        print(f"Historial de Vuelos: {puerta.getHistorial()}")

class TorreControlView:
    def imprimir_torre_control(self, torre_control):
        print("Estado de la Torre de Control:")
        print("Puertas de Embarque:")
        for puerta in torre_control.Puertas:
            print(f"  Puerta #{puerta.getIdentificacion()}: ", end="")
            if puerta.getDisponible():
                print("Disponible, Ubicacion: " + puerta.getUbicacion())
            else:
                print("No Disponible, Ubicacion: " + puerta.getUbicacion())
                if puerta.getVuelo():
                    print("  Numero de vuelo asignado: " + puerta.getVuelo().getNumIdent())
        print("")


class AeronaveVista:
    def imprimir_aeronave(self, aeronave):
        print("Marca:", aeronave.get_marca())
        print("Modelo:", aeronave.get_modelo())
        print("Capacidad de Pasajeros:", aeronave.get_capacidad_pasajeros())
        print("Velocidad Máxima:", aeronave.get_velocidad_maxima())
        print("Autonomía:", aeronave.get_autonomia())
        print("Año de Fabricación:", aeronave.get_ano_fabricacion())
        print("Estado:", aeronave.get_estado())
        print("Cantidad de Vuelos:", aeronave.get_ct_vuelos())

class AvionVista(AeronaveVista):
    def imprimir_avion(self, avion):
        super().imprimir_aeronave(avion)
        print("Altitud Máxima:", avion.get_altitud_max())
        print("Cantidad de Motores:", avion.get_cant_motores())

class HelicopteroVista(AeronaveVista):
    def imprimir_helicoptero(self, helicoptero):
        super().imprimir_aeronave(helicoptero)
        print("Cantidad de Rotores:", helicoptero.get_cnt_rotores())
        print("Capacidad de Elevación:", helicoptero.get_capacidad_elevacion())
        print("Uso:", helicoptero.get_uso())

class JetsVista(AeronaveVista):
    def imprimir_jets(self, jets):
        super().imprimir_aeronave(jets)
        print("Propietario:", jets.get_propietario())
        print("Servicios:", jets.get_servicios())
        print("Destinos Frecuentes:", jets.get_destinos_frec())

class AeropuertoVista:
    def mostrar_menu(self):
        print("1. Reservar Vuelo")
        print("2. Consultar Vuelo")
        print("3. Añadir Vuelo")
        print("4. Salir")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def obtener_opcion(self):
        try:
            opcion = int(input("Ingrese su opción: "))
            return opcion
        except ValueError:
            return None



