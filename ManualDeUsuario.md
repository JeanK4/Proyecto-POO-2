#### Integrantes: Benjamín Ortíz Morales y Jean Karlo Buitrago Orozco
---
#### UML - https://github.com/JeanK4/UML/blob/main/Proyecto2.drawio
---

# Manual de Usuario - Aeropuerto Alfonso Bonilla Aragón

## Tabla de contenido
1. [Introducción](#1-introducción)
2. [Instalación](#2-instalación)
3. [Uso para Usuarios](#3-uso-para-usuarios)
    1. [Guía Paises](#31-guía-paises)
    2. [Usuario Aeropuerto](#32-usuario-aeropuerto)
        1. [Ver Pasajeros](#321-ver-pasajeros)
        2. [Ver Vuelos](#322-ver-vuelos)
        3. [Comprar Vuelo](#323-comprar-vuelo)
        4. [Ver Tripulantes](#324-ver-tripulantes)
4. [Uso para Empleados](#4-uso-para-empleados)
    1. [Usuario Aerolinea](#41-usuario-aerolinea)
        1. [Crear Aerolinea](#411-crear-aerolinea)
        2. [Crear Aeronave](#412-crear-aeronave)
        3. [Mostrar Aeronaves](#413-mostrar-aeronaves)
        4. [Crear Vuelo](#414-crear-vuelo)
        5. [Crear Tripulante](#415-crear-tripulante)
    2. [Torre de Control](#42-torre-de-control)
        1. [Asignar Aeronaves](#421-asignar-aeronaves)
        2. [Pedir Actualización](#422-pedir-actualización)
        3. [Iniciar Vuelo](#423-iniciar-vuelo)
        4. [Finalizar Vuelo](#424-finalizar-velo)
        5. [Crear Puerta de Embarque](#425-crear-puerta-embarque)
        6. [Asignar Puertas](#426-asignar-puertas)
        7. [Consultar Puertas](#427-consultar-puertas)


## 1. Introducción

Este manual está diseñado para brindarte una guía completa sobre la utilización de la plataforma interactiva que hemos desarrollado para facilitar tu experiencia en el Aeropuerto Internacional Alfonso Bonilla Aragón. Esta herramienta, construida con la versátil biblioteca Streamlit, te proporcionará acceso a información como empleado del aeropuerto como para un pasajero/usuario del aeropuerto.

## 2. Instalación

Para instalar la aplicación, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.
2. Descarga el proyecto de este [repositorio](https://github.com/JeanK4/Proyecto-POO-2).
3. Navega al directorio del proyecto desde la línea de comandos.
4. Instala las dependencias utilizando el siguiente comando:

    bash
    pip install -r requirements.txt (requirements.txt en el repositorio)
  

5. Ejecuta la aplicación usando el siguiente comando:

    bash
    streamlit run main.py
    
6. Abre tu navegador web y accede a la URL proporcionada por Streamlit.

## 3. Uso para Usuarios

### 3.1 Guía Paises

Al ingresar al sistema del aeropuerto te encontraras con unos menus desplegables donde el primero es "Guía paises". En este menú podrás buscar algún pais con sus datos más relevantes para asesorarmiento de vuelo por si no sabes donde viajer aún.

### 3.2 Usuario Aeropuerto

Desde este menú se pueden realizar diversas consultas y acciones


### 3.2.1 Ver Pasajeros

Selecciona "Ver Pasajeros" para listar en una tabla la información de aquellos que hayan realizado una compra de vuelo

### 3.2.2 Ver Vuelos

Selecciona "Ver vuelos" para mostrar la información de los vuelos separados por su respectiva aerolínea.

### 3.2.3 Comprar Vuelo

Selecciona "Comprar Vuelos" para llegar a un menu donde puedes elegir la aerolinea y el vuelo de tu elección y posteriormente digitar tus datos para ser agregado a la base de datos.

### 3.2.4 Ver Tripulantes

Seleccion "Ver Tripulantes" para listar los tripulantes de cada aerolinea.

## 4. Uso para Empleados

### 4.1 Usuario Aerolinea

Selecciona "Usuario Aerolinea" para acceder al meno de aerolinea.

### 4.1.1 Crear Aerolinea

Selecciona "Crear Aerolínea" para agregar una nueva aerolínea al sistema del aeropuerto.

### 4.1.2 Crear Aeronave

Selecciona "Crear Aeronave" para ir al menu de creación de aeronave, donde se te piden los datos respectivos para la creación de el diferente tipo de aeronave.

### 4.1.3 Mostrar Aeronaves

Selecciona "Mostrar Aeronaves" para listar las aeronaves con algunos datos de estas separadas por la aeronalinea que las tiene.

### 4.1.4 Crear Vuelo

Selecciona "Crear Vuelo" para ir al menu de creación de vuelo. En este menú se te pedirá seleccionar una aerolinea a la cual se asignara el vuelo y posteriormente datos de este.

### 4.1.5 Crear Tripulante

Selecciona "Crear Tripulante" para crear un tripulante seleccionando una aerolinea para asignarlo a esta.

### 4.2 Torre de Control

Selecciona "Torre de Control" para acceder al menú de opciones de la torre de control.

### 4.2.1 Asignar Aeronaves

Selecciona "Asignar Aeronaves" para asignar una aeronave a un vuelo. En este menú se pedirá una aerolinea, un vuelo y una aeronave de esta aerolinea para poder ser asignado.

### 4.2.2 Pedir Actualización

Selecciona "Pedir Actualizacion" para listar la información del estado de las aeronaves para saber si se esta en Servicio, Totalmente asignada, Mantenimiento, En Puerta o En el Aire.

### 4.2.3 Iniciar Vuelo

Selecciona "Iniciar Vuelo" para elegir una puerta que contenga un vuelo, liberar la puerta e iniciar el vuelo de la aeronave, cambiando el estado de esta.

### 4.2.4 Finalizar Vuelo

Selecciona "Finalizar Vuelo" para finalizar el vuelo de alguna aeronave que se encuentre en el estado "En el aire" y pasar a mantenimiento esta aeronave.


### 4.2.5 Crear Puerta de Embarque

Selecciona "Crear Puerta Embarque" para ingresar al menú de creación de puertas, donde te pide una ubicación y una identificación de esta.

### 4.2.6 Asignar Puertas

Selecciona "Asignar Puertas" para asignar un vuelo a una puerta deseada cambiando el estado de la puerta a ocupado.

### 4.2.7 Consultar Puertas

Selecciona "Consultar Puertas" para listar en una tabla las puertas de embarque existentes con su estado ubicación e identificación.


¡Ahora estás listo para explorar todas las funcionalidades que ofrece nuestra aplicación del Aeropuerto en Streamlit! Si surge alguna pregunta o necesitas asistencia, te invitamos a explorar nuestra sección de ayuda o a ponerte en contacto con nuestro equipo de soporte técnico. ¡Disfruta de tu experiencia y buen viaje!

---

© 2023 Jeank-y-Benja | [Soporte técnico](https://github.com/JeanK4)
