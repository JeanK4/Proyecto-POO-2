import random

class Aeronave:
    def __init__(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion):
        self.marca = marca
        self.ct_vuelos = 0
        self.modelo = modelo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.velocidad_maxima = velocidad_maxima
        self.autonomia = autonomia
        self.ano_fabricacion = ano_fabricacion
        self.estado = 1

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_capacidad_pasajeros(self):
        return self.capacidad_pasajeros

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def get_autonomia(self):
        return self.autonomia

    def get_ano_fabricacion(self):
        return self.ano_fabricacion

    def get_estado(self):
        return self.estado

    def get_ct_vuelos(self):
        return self.ct_vuelos

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_capacidad_pasajeros(self, capacidad_pasajeros):
        self.capacidad_pasajeros = capacidad_pasajeros

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def set_autonomia(self, autonomia):
        self.autonomia = autonomia

    def set_ano_fabricacion(self, ano_fabricacion):
        self.ano_fabricacion = ano_fabricacion

    def set_estado(self, estado):
        self.estado = estado

    def set_ct_vuelos(self, ct_vuelos):
        self.ct_vuelos = ct_vuelos

class Avion(Aeronave):
    def __init__(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, altitud_max=random.randint(10000, 12000)):
        super().__init__(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion)
        self.altitud_max = altitud_max
        self.cant_motores = 4

    def get_altitud_max(self):
        return self.altitud_max

    def get_cant_motores(self):
        return self.cant_motores

    def set_altitud_max(self, altitud_max):
        self.altitud_max = altitud_max

    def set_cant_motores(self, cant_motores):
        self.cant_motores = cant_motores

class Helicoptero(Aeronave):
    def __init__(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, cnt_rotores, capacidad_elevacion, uso):
        super().__init__(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion)
        self.cnt_rotores = cnt_rotores
        self.capacidad_elevacion = capacidad_elevacion
        self.uso = uso


    def get_cnt_rotores(self):
        return self.cnt_rotores

    def get_capacidad_elevacion(self):
        return self.capacidad_elevacion

    def get_uso(self):
        return self.uso

    def set_cnt_rotores(self, cnt_rotores):
        self.cnt_rotores = cnt_rotores

    def set_capacidad_elevacion(self, capacidad_elevacion):
        self.capacidad_elevacion = capacidad_elevacion

    def set_uso(self, uso):
        self.uso = uso

class Jets(Aeronave):
    def __init__(self, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion, propietario, servicios, destinos_frec):
        super().__init__(marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, ano_fabricacion)
        self.estado = 1
        self.propietario = propietario
        self.servicios = servicios
        self.destinos_frec = destinos_frec

    def get_propietario(self):
        return self.propietario

    def get_servicios(self):
        return self.servicios

    def get_destinos_frec(self):
        return self.destinos_frec

    def set_propietario(self, propietario):
        self.propietario = propietario

    def set_servicios(self, servicios):
        self.servicios = servicios

    def set_destinos_frec(self, destinos_frec):
        self.destinos_frec = destinos_frec