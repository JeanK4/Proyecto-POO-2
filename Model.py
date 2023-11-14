from aeronave import Aeronave, Avion, Helicoptero, Jets
from aerolinea import Aerolinea
from aeropuerto import Aeropuerto
from pasajero import Pasajero
from persona import Persona
from tripulante import Tripulante
from usuario import Usuario
from vuelo import Vuelo
from torreDeControl import TorreControl
from puertaEmbarque import PuertaEmbarque
import streamlit as st


class model:
    def __init__(self):
        if 'Aerolinea' not in st.session_state:
            self.Aerolinea = st.session_state['Aerolinea'] = {}
        else:
            self.Aerolinea = st.session_state['Aerolinea']

        if 'Aeropuerto' not in st.session_state:
            self.Aeropuerto = st.session_state['Aeropuerto'] = Aeropuerto("Aeropuerto Alfonso Bonilla")
        else:
            self.Aeropuerto = st.session_state['Aeropuerto']

    def crearAerolinea(self, nameAerolinea):
        new_Aerolinea = Aerolinea(nameAerolinea)
        self.Aerolinea[nameAerolinea] = new_Aerolinea
        st.success(f"Aerolinea '{nameAerolinea}' creada exitosamente.")

    def crearVuelo(self, hora, fecha, numIdent, ciudadOrigen, ciudadDestino, aeronaveAsignada, aeroline):
        new_Vuelo = Vuelo(hora, fecha, numIdent, ciudadOrigen, ciudadDestino, aeronaveAsignada)
        self.Aerolinea[aeroline].addVuelo(new_Vuelo)
        st.success(f"Vuelo '{numIdent}' creado exitosamente.")

    def crearAvion(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, aeroline):
        new_Aeronave = Avion(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion)
        self.Aerolinea[aeroline].addAeronave(new_Aeronave)
        st.success(f"Aeronave creada exitosamente.")

    def crearHelicoptero(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion,
                         cnt_rotores, capacidad_elevacion, uso, aeroline):
        new_Aeronave = Helicoptero(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion,
                                   cnt_rotores, capacidad_elevacion, uso)
        self.Aerolinea[aeroline].addAeronave(new_Aeronave)
        st.success(f"Aeronave creada exitosamente.")

    def crearJet(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, propietario,
                 servicios, destinos_frec, aeroline):
        new_Aeronave = Jets(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion,
                            propietario, servicios, destinos_frec)
        self.Aerolinea[aeroline].addAeronave(new_Aeronave)
        st.success(f"Aeronave creada exitosamente.")

    def crearPasajero(self, cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo, nacionalidad,
                      cntMaletas, infoMedica):
        new_Passenger = Pasajero(cedula, nombre, fechaNacimiento, genero, direccion, telefono, correo, nacionalidad,
                                 cntMaletas, infoMedica)
        self.Aeropuerto.addPasajero(new_Passenger)

    def getPassengers(self):
        return self.Aeropuerto.getPasajeros()

    def mostrarVuelos(self):
        dic = {}
        aerolinea = st.session_state['Aerolinea']
        aerolineas = list(aerolinea.keys())
        i = 0
        while i < len(aerolineas):
            dic1 = {}
            listatmp = aerolinea[aerolineas[i]].getVuelos()
            for j in range(len(listatmp)):
                lista = []
                lista.append(listatmp[j].getHora())
                lista.append(listatmp[j].getFecha())
                lista.append(listatmp[j].getCiudadOrigen())
                lista.append(listatmp[j].getCiudadDestino())
                lista.append(listatmp[j].getTipoVuelo())
                aeronaveAsignada = listatmp[j].getAeronaveAsignada()
                ans = None
                if type(aeronaveAsignada) == Avion:
                    ans = f"Avion {aeronaveAsignada.get_modelo()}"
                elif type(aeronaveAsignada) == Helicoptero:
                    ans = f"Helicoptero {aeronaveAsignada.get_modelo()}"
                elif type(aeronaveAsignada) == Jets:
                    ans = f"Jet {aeronaveAsignada.get_modelo()}"
                lista.append(ans)
                dic1[listatmp[j].getNumIdent()] = lista
            dic[aerolineas[i]] = dic1
            i += 1
        return dic

    def mostrarAeronaves(self):
        dic = {}
        aerolinea = st.session_state['Aerolinea']
        aerolineas = list(aerolinea.keys())
        i = 0
        while i < len(aerolineas):
            dic1 = {}
            listatmp = aerolinea[aerolineas[i]].getAeronaves()
            for j in range(len(listatmp)):
                lista = []
                if type(listatmp[j]) == Avion:
                    lista.append(listatmp[j].get_marca())
                    lista.append(listatmp[j].get_ct_vuelos())
                    lista.append(listatmp[j].get_capacidad_pasajeros())
                    lista.append(listatmp[j].get_estado())
                    lista.append(listatmp[j].get_modelo())
                    dic1[f"Avion {j + 1}"] = lista
                elif type(listatmp[j]) == Helicoptero:
                    lista.append(listatmp[j].get_marca())

                    lista.append(listatmp[j].get_ct_vuelos())
                    lista.append(listatmp[j].get_capacidad_pasajeros())
                    lista.append(listatmp[j].get_estado())
                    lista.append(listatmp[j].get_modelo())
                    dic1[f"Helicoptero {j + 1}"] = lista
                else:
                    lista.append(listatmp[j].get_marca())

                    lista.append(listatmp[j].get_ct_vuelos())
                    lista.append(listatmp[j].get_capacidad_pasajeros())
                    lista.append(listatmp[j].get_estado())
                    lista.append(listatmp[j].get_modelo())
                    dic1[f"Jet {j + 1}"] = lista
            dic[aerolineas[i]] = dic1
            i += 1
        return dic

    def crearPuertaEmbarque(self, identificacion, ubicacion):
        puerta = PuertaEmbarque(identificacion, ubicacion)
        self.Aeropuerto.addPuerta(puerta)

    def getPuertaEmbarque(self):
        return self.Aeropuerto.getPuertas()

    def asignarPuerta(self, puerta, vuelo, disponible, puertas):
        for p in puertas:
            if p.getUbicacion() == puerta:
                p.setDisponible(disponible)
                p.setVuelo(vuelo)
                p.addHistorial(vuelo)

    def asignarAeronaveVuelo(self, aeroline, tipo, model, vuelo):
        aeronave = self.Aerolinea[aeroline].buscarVueloModelo(model)
        self.Aerolinea[aeroline].setAeronaveVuelo(vuelo, aeronave, tipo)

    def getVuelosAerolinea(self):
        ans = {}
        for aeroline in self.Aerolinea:
            ans1 = []
            lista = self.Aerolinea[aeroline].getVuelos()
            for i in range(len(lista)):
                if lista[i].getAeronaveAsignada() is None:
                    ans1.append(lista[i].getNumIdent())
            ans[aeroline] = ans1
        return ans

    def getAerolineas(self):
        aerolinea = st.session_state['Aerolinea']
        aerolineas = list(aerolinea.keys())
        return aerolineas

    def getModeloAviones(self):
        ct = 0
        ans = {}
        for aeroline in self.Aerolinea:
            lista = self.Aerolinea[aeroline].getAeronaves()
            ans[aeroline] = []
            for i in range(len(lista)):
                if type(lista[i]) is Avion and lista[i].get_ct_vuelos() < 3:
                    ans[aeroline].append(lista[i].get_modelo())
            if len(ans[aeroline]) == 0:
                ct += 1
        if ct == len(self.Aerolinea):
            ans  = {}
        return ans

    def getModeloHelicopteros(self):
        ct = 0
        ans = {}
        for aeroline in self.Aerolinea:
            lista = self.Aerolinea[aeroline].getAeronaves()
            ans[aeroline] = []
            for i in range(len(lista)):
                if type(lista[i]) is Helicoptero and lista[i].get_ct_vuelos() < 3:
                    ans[aeroline].append(lista[i].get_modelo())
            if len(ans[aeroline]) == 0:
                ct += 1
        if ct == len(self.Aerolinea):
            ans  = {}
        return ans

    def getModeloJets(self):
        ct = 0
        ans = {}
        for aeroline in self.Aerolinea:
            lista = self.Aerolinea[aeroline].getAeronaves()
            ans[aeroline] = []
            for i in range(len(lista)):
                if type(lista[i]) is Jets and lista[i].get_ct_vuelos() < 3:
                    ans[aeroline].append(lista[i].get_modelo())
            if len(ans[aeroline]) == 0:
                ct += 1
        if ct == len(self.Aerolinea):
            ans  = {}
        return ans
    

    