from Model import model
from View import view
import streamlit as st
import requests
import json


class controller:

    def __init__(self):
        self.model = model()
        self.view = view()

    def showMenu(self):
        opcion = st.sidebar.selectbox("Selecciona una opción",
                                      ["Guía Paises", "Usuario Aerolinea", "Usuario Aeropuerto", "Torre de Control"])
        if opcion == "Guía Paises":
            self.menu_paises()
        elif opcion == "Usuario Aeropuerto":
            self.menu_aeropuerto()
        elif opcion == "Usuario Aerolinea":
            self.menu_aerolinea()
        elif opcion == "Torre de Control":
            self.menu_TorreDeControl()

    def menu_TorreDeControl(self):
        st.title("Menú de Torre De Control")
        opcion = st.sidebar.selectbox("Opciones",
                                      ["Asignar Aeronaves", "Pedir Actualización", "Iniciar Vuelo", "Finalizar Vuelo",
                                       "Crear Puerta Embarque", "Asignar Puertas", "Consultar Puertas"])
        if opcion == "Asignar Aeronaves":
            self.asignarAeronave()
            pass

        elif opcion == "Pedir Actualización":
            pass

        elif opcion == "Iniciar Vuelo":
            pass

        elif opcion == "Crear Puerta Embarque":
            self.crearPuertaEmbarque()
            pass

        elif opcion == "Finalizar Vuelo":
            pass

        elif opcion == "Asignar Puertas":
            self.asignarPuerta()
            pass

        elif opcion == "Consultar Puertas":
            self.mostrarPuertaEmbarque()
            pass

    def menu_aeropuerto(self):
        st.title("Menú de Usuario Aeropuerto")
        opcion = st.sidebar.selectbox("Opciones", ["Crear Pasajero", "Ver Pasajeros", "Ver vuelos", "Comprar vuelos"])
        if opcion == "Crear Pasajero":
            self.crearPasajero()
            pass
        elif opcion == "Ver Pasajeros":
            self.mostrarPasajeros()
            pass
        elif opcion == "Ver vuelos":
            self.mostrarVuelos()
            pass

    def menu_aerolinea(self):
        st.title("Menú de Usuario Aerolínea")
        opcion = st.sidebar.selectbox("Opciones",
                                      ["Crear Aerolínea", "Crear Aeronave", "Mostrar Aeronaves", "Crear Vuelo", ])
        if opcion == "Crear Aerolínea":
            self.crearAerolinea()
            pass
        elif opcion == "Crear Vuelo":
            self.crearVuelos()
            pass
        elif opcion == "Crear Aeronave":
            self.crearAeronave()
            pass
        elif opcion == "Mostrar Aeronaves":
            self.mostrarAeronaves()
            pass

    def crearPasajero(self):
        passenger = self.view.crearPasajero()
        if passenger != None:
            self.model.crearPasajero(passenger["cedula"], passenger["nombre"], passenger["fechaNacimiento"],
                                     passenger["genero"], passenger["direccion"], passenger["telefono"],
                                     passenger["correo"], passenger["nacionalidad"], passenger["ctMaletas"],
                                     passenger["infoMedica"])


    def menu_paises(self):
        st.header("Bienvenido a la Guía de Paises")
        st.markdown("## Información")
        st.markdown("Digita el país para conocer más acerca de él")
        pais = st.text_input("País: ")
        but = st.button("Conocer más")
        if but:
            self.getPaises(pais)

    def getPaises(self, pais):
        url = "https://restcountries.com/v3.1/name/" + pais
        respuesta =requests.get(url)
        if respuesta.status_code == 200:
            datos = json.loads(respuesta.text)
            st.write("Nombre: ", datos[0]["name"]["common"])
            lista = list(datos[0]["currencies"].keys())
            value = lista[0]
            st.write("Moneda: ", datos[0]["currencies"][value])
            st.write("Ciudad Capital: ", datos[0]["capital"][0])
            st.write("Región: ", datos[0]["region"])
            st.write("Población: ", datos[0]["population"])
            st.image(datos[0]["flags"]["png"])
        else:
            st.warning("No se pudo encontrar el país")

    def crearAerolinea(self):
        aeroline = self.view.crearAerolinea()
        if aeroline != None:
            self.model.crearAerolinea(aeroline["aeroline"])

    def mostrarPasajeros(self):
        list = self.model.getPassengers()
        self.view.mostrarPasajeros(list)

    def crearVuelos(self):
        flight = self.view.crearVuelo()
        if flight != None:
            self.model.crearVuelo(flight["hora"], flight["fecha"], flight["numIdent"], flight["ciudadOrigen"],
                                  flight["ciudadDestino"], None, flight["aerolinea"])

    def mostrarVuelos(self):
        aerolineVuelos = self.model.mostrarVuelos()
        self.view.mostrarVuelos(aerolineVuelos)

    def crearAeronave(self):
        aeronave = self.view.crearAeronave()
        if aeronave != None:
            if aeronave["tipo"] == "avion":
                self.model.crearAvion(aeronave["marca"], aeronave["modelo"], aeronave["capacidadPasajeros"],
                                      aeronave["velocidadMax"], aeronave["autono"], aeronave["fechaFabri"],
                                      aeronave["aerolineaSel"])
            elif aeronave["tipo"] == "helicoptero":
                self.model.crearHelicoptero(aeronave["marca"], aeronave["modelo"], aeronave["capacidadPasajeros"],
                                            aeronave["velocidadMax"], aeronave["autono"], aeronave["fechaFabri"],
                                            aeronave["cntRotores"], aeronave["capacidadElevacion"], aeronave["uso"],
                                            aeronave["aerolineaSel"])
            else:
                self.model.crearJet(aeronave["marca"], aeronave["modelo"], aeronave["capacidadPasajeros"],
                                    aeronave["velocidadMax"], aeronave["autono"], aeronave["fechaFabri"],
                                    aeronave["propietario"],
                                    aeronave["servicios"], aeronave["destinos"], aeronave["aerolineaSel"])

    def mostrarAeronaves(self):
        aeronaves = self.model.mostrarAeronaves()
        self.view.mostrarAeronaves(aeronaves)
        return

    def crearPuertaEmbarque(self):
        puerta = self.view.crearPuertaEmbarque()
        if puerta is not None:
            self.model.crearPuertaEmbarque(puerta["identificacion"], puerta["ubicacion"])

    def mostrarPuertaEmbarque(self):
        lista = self.model.getPuertaEmbarque()
        self.view.mostrarPuertaEmbarque(lista)

    def asignarPuerta(self):
        puertas = self.model.getPuertaEmbarque()
        vuelos = self.model.mostrarVuelos()
        selec = self.view.asignarPuerta(puertas, vuelos)
        if selec is not None:
            self.model.asignarPuerta(selec["puertaAsignada"], selec["vueloAsignado"], selec["disponible"], puertas)

    def asignarAeronave(self):
        avion = self.model.getModeloAviones()
        heli = self.model.getModeloHelicopteros()
        jet = self.model.getModeloJets()
        if len(avion) == 0 and len(heli) == 0 and len(jet) == 0: 
            st.error("Sin aeronaves disponibles")
        else:
            vuelos = self.model.getVuelosAerolinea()
            selec = self.view.asignarAeronaveVuelo(avion, heli, jet, vuelos)
            if selec != None:
                self.model.asignarAeronaveVuelo(selec["aerolinea"], selec["tipo"], selec["selec"], selec["vuelo"])