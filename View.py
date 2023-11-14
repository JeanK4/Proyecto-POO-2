import streamlit as st
from datetime import date


class view:

    def __init__(self):
        st.title("Aeropuerto Alfonso Bonilla Aragón")
        st.divider()

    def crearAerolinea(self):
        aeroline = st.text_input("Nombre Aerolinea: ")
        but = st.button("Crear Aerolinea", type="primary")
        if but:
            return {"aeroline": aeroline}
        else:
            return None

    def mostrarPasajeros(self, lista_pasajeros):
        st.header("Pasajeros")
        data = []
        for i, pasajero in enumerate(lista_pasajeros, start=1):
            data.append({
                "Cédula": pasajero.getCedula(),
                "Nombre": pasajero.getNombre(),
                "Fecha de Nacimiento": pasajero.getFechaNacimiento(),
                "Género": pasajero.getGenero(),
                "Direccion": pasajero.getDireccion(),
                "Teléfono": pasajero.getTelefono(),
                "Correo": pasajero.getCorreo(),
                "Nacionalidad": pasajero.getNacionalidad(),
                "Cantidad de Maletas": pasajero.getCntMaletas(),
                "Información Médica": pasajero.getInfoMedica()
            })

        tabla_container = st.empty()
        if not hasattr(tabla_container, 'table_created'):
            tabla_container.table(data)
            tabla_container.table_created = True
        else:
            tabla_container.table(data)

    def crearVuelo(self):
        aerolineas = st.session_state['Aerolinea']
        aerolinea_seleccionada = st.selectbox("Seleccione Aerolínea", list(aerolineas.keys()))
        hora = st.text_input("Hora del vuelo:")
        fecha = st.date_input("Fecha del vuelo: ")
        numIdent = st.text_input("Número del vuelo: ")
        ciudadOrigen = st.text_input("Ciudad de Origen: ")
        ciudadDestino = st.text_input("Ciudad de Destino: ")
        but = st.button("Crear Vuelo", type="primary")
        if but and aerolinea_seleccionada != None:
            return {
                "aerolinea": aerolinea_seleccionada,
                "hora": hora,
                "fecha": fecha,
                "numIdent": numIdent,
                "ciudadOrigen": ciudadOrigen,
                "ciudadDestino": ciudadDestino
            }
        else:
            return None

    def mostrarVuelos(self, aerolineVuelos):
        st.divider()
        caption1 = ""
        caption2 = ""
        caption3 = ""
        caption4 = ""
        caption5 = ""
        caption6 = ""
        for aero in aerolineVuelos:
            aerolinea = f"Aerolinea {aero}"
            st.header(aerolinea)
            if len(aerolineVuelos[aero]) != 0:
                for flight in aerolineVuelos[aero]:
                    st.write(f"- Vuelo {flight}")
                    for j in range(len(aerolineVuelos[aero][flight])):
                        if j == 0:
                            caption1 += f"Hora: {aerolineVuelos[aero][flight][j]}"
                        elif j == 1:
                            caption2 += f"Fecha: {aerolineVuelos[aero][flight][j]}"
                        elif j == 2:
                            caption3 += f"Origen: {aerolineVuelos[aero][flight][j]}"
                        elif j == 3:
                            caption4 += f"Destino: {aerolineVuelos[aero][flight][j]}"
                        elif j == 4:
                            caption5 += f"Tipo de Vuelo: {aerolineVuelos[aero][flight][j]}"
                        else:
                            caption6 += f"Aeronave asignada: {aerolineVuelos[aero][flight][j]}"
                    st.markdown(caption1)
                    st.markdown(caption2)
                    st.markdown(caption3)
                    st.markdown(caption4)
                    st.markdown(caption5)
                    st.markdown(caption6)
                    caption1 = ""
                    caption2 = ""
                    caption3 = ""
                    caption4 = ""
                    caption5 = ""
                    caption6 = ""
                st.divider()
            else:
                st.info("Aerolinea sin vuelos")

    def comprarVuelo(self, vuelos):
        aerolinea = st.session_state['Aerolinea']
        aerolineas = list(aerolinea.keys())
        aerolinea_seleccionada = st.selectbox("Seleccione una aerolinea: ", aerolineas)
        tmp = []
        for aero in vuelos:
            for flight in vuelos[aero]:
                if aero == aerolinea_seleccionada:
                    tmp.append(f"{flight}")
        vuelo = st.selectbox("Seleccione un vuelo: ", tmp)
        cedula = st.text_input("Cédula: ")
        nombre = st.text_input("Nombre: ")
        fechaNacimiento = st.text_input("Fecha de Nacimiento: ")
        genero = st.selectbox('Género:', ['Masculino', 'Femenino', 'Otro'])
        direccion = st.text_input("Direccion: ")
        telefono = st.text_input("Teléfono: ")
        correo = st.text_input("Correo: ")
        nacionalidad = st.text_input("Nacionalidad: ")
        ctMaletas = st.number_input("Cantidad de maletas: ", min_value=1)
        infoMedica = st.text_input("Información médica: ")       
        but = st.button("Comprar Vuelo")
        if but:
            st.success("Vuelo comprado con éxito")
            return {
                "cedula": cedula,
                "nombre": nombre,
                "fechaNacimiento": fechaNacimiento,
                "genero": genero,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo,
                "nacionalidad": nacionalidad,
                "ctMaletas": ctMaletas,
                "infoMedica": infoMedica,
                "vuelo": vuelo,
                "aerolinea": aerolinea_seleccionada,
            }
        else:
            return None

    def mostrarAeronaves(self, aeronaves):
        st.divider()
        caption1 = ""
        caption2 = ""
        caption3 = ""
        caption4 = ""
        for aero in aeronaves:
            aerolinea = f"Aerolinea {aero}"
            st.header(aerolinea)
            for aeronave in aeronaves[aero]:
                if len(aeronave) >= 7 and len(aeronave) < 13:
                    st.write(f"- Avion {aeronaves[aero][aeronave][0]}")
                elif len(aeronave) >= 13 and len(aeronave) < 16:
                    st.write(f"- Helicoptero {aeronaves[aero][aeronave][0]}")
                elif len(aeronave) == 5 and len(aeronave) < 7:
                    st.write(f"- Jet {aeronaves[aero][aeronave][0]}")
                for j in range(1, len(aeronaves[aero][aeronave])):
                    if j == 1:
                        caption1 += f"Cantidad de Vuelos Asignados: {aeronaves[aero][aeronave][j]}"
                    elif j == 2:
                        caption2 += f"Capacidad de Pasajeros: {aeronaves[aero][aeronave][j]}"
                    elif j == 3:
                        if aeronaves[aero][aeronave][j] == 1:
                            caption3 += f"Estado de la aeronave: Servicio"
                        elif aeronaves[aero][aeronave][j] == 2:
                            caption3 += f"Estado de la aeronave: Totalmente asignado"
                        elif aeronaves[aero][aeronave][j] == 3:
                            caption3 += f"Estado de la aeronave: Mantenimiento"
                        elif aeronaves[aero][aeronave][j] == 4:
                            caption3 += f"Estado de la aeronave: En puerta"
                        else:
                            caption3 += f"Estado de la aeronave: En el aire"
                    elif j == 4:
                        caption4 += f"Modelo: {aeronaves[aero][aeronave][j]}"
                st.markdown(caption1)
                st.markdown(caption2)
                st.markdown(caption3)
                st.markdown(caption4)
                caption1 = ""
                caption2 = ""
                caption3 = ""
                caption4 = ""
                st.divider()

    def crearAeronave(self):
        st.header("Creacion de aeronave")
        aerolineas = st.session_state['Aerolinea']
        aerolinea_seleccionada = st.selectbox("Seleccione Aerolínea", list(aerolineas.keys()))
        tipoAeronave = st.selectbox("Tipo de Aeronave", ("Avion", "Avion de carga", "Helicoptero", "Jet privado"))
        if tipoAeronave == "Avion" or tipoAeronave == "Avion de carga":
            marca = st.text_input("Marca del avión: ")
            modelo = st.text_input("Modelo del avión: ")
            capacidadPasajeros = st.number_input("Ingrese el número de pasajeros", min_value=1)
            velocidadMax = st.text_input("Velocidad máxima del avión: ")
            autono = st.text_input("Autonomia del avión: ")
            fechaFabri = st.text_input("Año de fabricación: ")
            avion = "avion"
            but = st.button("Crear Avion ")
            if but:
                return {
                    "aerolineaSel": aerolinea_seleccionada,
                    "tipo": avion,
                    "marca": marca,
                    "modelo": modelo,
                    "capacidadPasajeros": capacidadPasajeros,
                    "velocidadMax": velocidadMax,
                    "autono": autono,
                    "fechaFabri": fechaFabri
                }
            else:
                return None
        elif tipoAeronave == "Helicoptero":
            uso = st.selectbox("Uso del helicoptero", ("Rescate", "Turismo", "Transporte", "Medicina"))
            marca = st.text_input("Marca del helicoptero: ")
            modelo = st.text_input("Modelo del helicoptero: ")
            capacidadPasajeros = st.number_input("Ingrese el número de pasajeros", min_value=1)
            velocidadMax = st.text_input("Velocidad máxima del helicoptero: ")
            autono = st.text_input("Autonomia del helicoptero: ")
            fechaFabri = st.text_input("Año de fabricación: ")
            cntRotores = st.text_input("Cantidad de Rotores: ")
            capacidadElevacion = st.text_input("Capacidad de Elevación: ")
            helicoptero = "helicoptero"
            but = st.button("Crear Helicoptero ")
            if but:
                return {
                    "aerolineaSel": aerolinea_seleccionada,
                    "tipo": helicoptero,
                    "marca": marca,
                    "modelo": modelo,
                    "capacidadPasajeros": capacidadPasajeros,
                    "velocidadMax": velocidadMax,
                    "autono": autono,
                    "fechaFabri": fechaFabri,
                    "cntRotores": cntRotores,
                    "capacidadElevacion": capacidadElevacion,
                    "uso": uso
                }
            else:
                return None
        else:
            marca = st.text_input("Marca del jet ")
            modelo = st.text_input("Modelo del jet: ")
            capacidadPasajeros = st.number_input("Ingrese el número de pasajeros", min_value=1)
            velocidadMax = st.text_input("Velocidad máxima del jet: ")
            autono = st.text_input("Autonomia del jet: ")
            fechaFabri = st.text_input("Año de fabricación: ")
            propietario = st.text_input("Propietario del jet: ")
            servicios = st.text_area("Ingresar Servicios (Separados por salto de linea):", "")
            datosServicios = servicios.split('\n')
            destinos = st.text_area("Ingresar sus destinos frecuentes (Separados por salto de linea):", "")
            datosDestinos = destinos.split('\n')
            jet = "Jet"
            but = st.button("Crear Jet: ")
            if but:
                return {
                    "aerolineaSel": aerolinea_seleccionada,
                    "tipo": jet,
                    "propietario": propietario,
                    "marca": marca,
                    "modelo": modelo,
                    "capacidadPasajeros": capacidadPasajeros,
                    "velocidadMax": velocidadMax,
                    "autono": autono,
                    "fechaFabri": fechaFabri,
                    "servicios": datosServicios,
                    "destinos": datosDestinos
                }
            else:
                return None

    def mostrarPuertaEmbarque(self, listaPuertas):
        st.header("Puertas de Embarque")
        data = []
        disponible = ""
        for s in listaPuertas:
            if s.getDisponible():
                disponible = "Disponible"
                data.append({
                    "Identificación": s.getIdentificacion(),
                    "Ubicación": s.getUbicacion(),
                    "Estado": disponible

                })
            else:
                disponible = "Ocupado"
                data.append({
                    "Identificación": s.getIdentificacion(),
                    "Ubicación": s.getUbicacion(),
                    "Estado": disponible

                })

        tabla_container = st.empty()
        if not hasattr(tabla_container, 'table_created'):
            tabla_container.table(data)
            tabla_container.table_created = True
        else:
            tabla_container.table(data)

    def crearPuertaEmbarque(self):
        st.header("Creacion de Puertas de Embarque")
        ubicacion = st.text_input("Ubicación: ")
        identificacion = st.text_input("Identificación: ")
        but = st.button("Crear Puerta", type="primary")
        if but:
            st.success(f"Puerta creada con éxito.")
            return {
                "ubicacion": ubicacion,
                "identificacion": identificacion
            }
        else:
            return None

    def asignarPuerta(self, puertas, vuelos):
        global vueloAsignado
        data = []
        aux = None
        for i, puerta in enumerate(puertas, start=1):
            data.append(puerta.getUbicacion())

        st.header("Asignación de Puertas de Embarque")
        aerolineas = st.session_state['Aerolinea']
        puertaAsignada = st.selectbox("Seleccione Puerta de Embarque", data)

        for puerta in puertas:
            if puertaAsignada == puerta.getUbicacion():
                aux = puerta.getDisponible()

        if aux:
            aerolinea_seleccionada = st.selectbox("Seleccione Aerolínea", list(aerolineas.keys()))

            for aero in vuelos:
                aux = []
                if aero == aerolinea_seleccionada:
                    for flight in vuelos[aero]:
                        aux.append(flight)
                    vueloAsignado = st.selectbox("Seleccione Vuelo Asignado", aux)

            but = st.button("Asignar Puerta de Embarque", type="primary")
            if but:
                st.success(f"Puerta Asignada Con Éxito!!")
                return {
                    "puertaAsignada": puertaAsignada,
                    "vueloAsignado": vueloAsignado,
                    "aerolineaSelec": aerolinea_seleccionada,
                    "disponible": False
                }
            else:
                return None
        else:
            st.error("No hay puertas disponibles")

    def asignarAeronaveVuelo(self, avion, heli, jet, vuelos):
        global selec
        aerolinea = st.session_state['Aerolinea']
        aerolineas = list(aerolinea.keys())
        aero = st.selectbox("Seleccione la aerolinea: ", aerolineas)
        vuelo = st.selectbox("Seleccione un vuelo: ", vuelos[aero])
        tipo = st.selectbox("Seleccione el tipo de aeronave: ", ["Avión", "Helicoptero", "Jet"])
        if tipo == "Avión" and len(avion) != 0:

            aux = avion[aero]
            selec = st.selectbox("Seleccione el avión:", aux)
        elif tipo == "Helicoptero" and len(heli) != 0:
            aux = heli[aero]
            selec = st.selectbox("Seleccione el helicoptero", aux)
        elif tipo == "Jet" and len(jet) != 0:
            aux = jet[aero]
            selec = st.selectbox("Seleccione el Jet", aux)
        but = st.button("Seleccionar Aeronave")
        if but:
            st.success(f"Aeronave Asignada Con Éxito!!")
            return {"aerolinea": aero,
                    "tipo": tipo,
                    "selec": selec,
                    "vuelo": vuelo
                    }
        else:
            return None
        
    def iniciarVuelo(self, puertas):
        data = []
        for i, puerta in enumerate(puertas, start=1):
            data.append(puerta.getUbicacion())

        st.header("Inicio de Vuelo")
        puertaAsignada = st.selectbox("Seleccione Puerta de Embarque donde se ubica el vuelo", data)

        for puerta in puertas:
            if(puerta.getUbicacion() == puertaAsignada):
                puertaAsignada = puerta

        but = st.button("Iniciar Vuelo")
        if but:
            st.success(f"Vuelo iniciado con exito.")
            return puertaAsignada
        else:
            return None

    def finalizarVuelo(self, vuelos, objVuelos):
        st.header("Finalizar Vuelos")
        aux = []
        for i in range(len(objVuelos)):
            if(objVuelos[i].getAeronaveAsignada() is not None):
                if(objVuelos[i].getAeronaveAsignada().get_estado() == 5):
                    aux.append(objVuelos[i].getNumIdent())

        vueloAsig = st.selectbox("Seleccione el vuelo", aux)

        but = st.button("Finalizar Vuelo")
        if but:
            st.success(f"Vuelo iniciado con exito.")
            return vueloAsig
        else:
            return None
        
    def pedirActualizacion(self, vuelos):
        for aero in vuelos:
            for flight in vuelos[aero]:
                if vuelos[aero][flight][1] == 5:
                    st.write(f"- Vuelo {flight}")
                    st.write(f"Altitud: {vuelos[aero][flight][0]}")
                    if vuelos[aero][flight][1] == 1:
                        st.write(f"Estado: Servicio")
                    elif vuelos[aero][flight][1] == 2:
                        st.write(f"Estado: Totalmente asignado")
                    elif vuelos[aero][flight][1] == 3:
                        st.write(f"Estado: Mantenimiento")
                    elif vuelos[aero][flight][1] == 4:
                        st.write(f"Estado: En Puerta")
                    elif vuelos[aero][flight][1] == 5:
                        st.write(f"Estado: En el aire")
                else:
                    st.write(f"- Vuelo {flight}")
                    if vuelos[aero][flight][1] == 1:
                        st.write(f"Estado: Servicio")
                    elif vuelos[aero][flight][1] == 2:
                        st.write(f"Estado: Totalmente asignado")
                    elif vuelos[aero][flight][1] == 3:
                        st.write(f"Estado: Mantenimiento")
                    elif vuelos[aero][flight][1] == 4:
                        st.write(f"Estado: En Puerta")
                    elif vuelos[aero][flight][1] == 5:
                        st.write(f"Estado: En el aire")
    
    def crearTripulante(self):
        aerolinea = st.session_state['Aerolinea']
        aerolineas = list(aerolinea.keys())
        aero = st.selectbox("Seleccione la aerolinea: ", aerolineas)
        cedula = st.text_input("Digite su cedula: ")
        nombre = st.text_input("Digite su nombre: ")
        fechaNacimiento = st.text_input("Digite su fecha de nacimiento: ")
        genero = st.selectbox('Género:', ['Masculino', 'Femenino', 'Otro'])
        direccion = st.text_input("Direccion: ")
        telefono = st.text_input("Telefono: ")
        correo = st.text_input("Correo: ")
        puesto = st.text_input("Puesto: ")
        experienciaAnos = st.text_input("Años de Experiencia: ")
        horasMax = st.text_input("Horas Máximas:")
        but = st.button("Crear Tripulante")
        if but:
            st.success("Tripulante creado con éxito")
            return{
                "cedula": cedula,
                "nombre": nombre,
                "fechaNacimiento": fechaNacimiento,
                "genero": genero,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo,
                "puesto": puesto,
                "experienciaAnos": experienciaAnos,
                "horasMax": horasMax,
                "aerolinea": aero
            }
        else:
            return None
    
    def mostrarTripulantes(self, dic_tripulacion):
        st.divider()
        st.header("Tripulantes")
        for aero in dic_tripulacion:
            st.header(f"Aerolinea {aero}")
            data = []
            for i, tripulante in enumerate(dic_tripulacion[aero], start=1):
                data.append({
                    "Cédula": tripulante.getCedula(),
                    "Nombre": tripulante.getNombre(),
                    "Fecha de Nacimiento": tripulante.getFechaNacimiento(),
                    "Género": tripulante.getGenero(),
                    "Direccion": tripulante.getDireccion(),
                    "Teléfono": tripulante.getTelefono(),
                    "Correo": tripulante.getCorreo(),
                    "Puesto": tripulante.getPuesto(),
                    "Años Experiencia": tripulante.getExperienciaAnos(),
                    "Horas": tripulante.getHorasMax()
                })

            tabla_container = st.empty()
            if not hasattr(tabla_container, 'table_created'):
                tabla_container.table(data)
                tabla_container.table_created = True
            else:
                tabla_container.table(data)