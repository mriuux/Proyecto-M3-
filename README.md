# Proyecto-M3/
# Proyecto Módulo 3 – Máquina de Galton

## Descripción

Este proyecto consiste en la simulación de una Máquina de Galton utilizando el lenguaje de programación Python.

La simulación representa el recorrido de 3,000 canicas a través de 12 niveles de obstáculos. En cada nivel, cada canica toma una dirección aleatoria, ya sea hacia la izquierda o hacia la derecha, hasta llegar a un contenedor final.

Los resultados obtenidos se almacenan en una lista y posteriormente se representan mediante un histograma para visualizar la distribución de las canicas.

## Tecnologías utilizadas

- **Python:** Lenguaje de programación utilizado para desarrollar la simulación.
- **Random:** Módulo utilizado para generar decisiones aleatorias durante el recorrido de las canicas.
- **Matplotlib:** Biblioteca utilizada para generar el histograma y representar gráficamente los resultados.
- **Visual Studio Code:** Editor utilizado para escribir y ejecutar el código.
- **Git y GitHub:** Herramientas utilizadas para el control de versiones y almacenamiento del proyecto.

## Funcionamiento del programa

El programa se desarrolla mediante los siguientes pasos:

1. Se importan los módulos "random" y "matplotlib.pyplot"
2. Se define la función "simular_canica()", encargada de representar el recorrido de una canica a través de 12 niveles.
3. En cada nivel se genera una decisión aleatoria entre izquierda y derecha.
4. Se utiliza un ciclo para ejecutar la simulación de 3,000 canicas.
5. Los resultados de cada recorrido se almacenan en una lista llamada "resultados".
6. Se define la función "graficar_resultados()", que recibe la lista y genera un histograma.
7. Finalmente, se muestra la cantidad de canicas que terminaron en cada contenedor.

## Funciones principales

### simular_canica(niveles=12)

Realiza la simulación individual del recorrido de una canica. Recibe como parámetro el número de niveles y retorna un número entero que representa el contenedor final.

### graficar_resultados(datos)

Recibe la lista de resultados de las simulaciones y genera un histograma utilizando Matplotlib.

## Instalación y ejecución

**1. Instalar Python**

Es necesario contar con Python instalado en el equipo.

**2. Instalar Matplotlib**

Abrir la terminal y ejecutar el siguiente comando:

"bash
py -m pip install matplotlib"

**3. Ejecutar el programa**

Abrir el archivo Python en Visual Studio Code y ejecutar el código.

El programa realizará las 3,000 simulaciones y mostrará el histograma con los resultados obtenidos.

## Reflexión

Durante el desarrollo de este proyecto pude comprender la importancia de utilizar funciones para organizar y reutilizar el código en Python.

También aprendí a trabajar con módulos como "random", que permite generar decisiones aleatorias, y "matplotlib", que facilita la representación visual de los datos obtenidos.

La realización de las simulaciones me permitió comprender cómo almacenar y procesar una cantidad considerable de resultados mediante listas y ciclos.

Finalmente, aprendí que la modularidad y la documentación ayudan a mantener un código más organizado, comprensible y fácil de modificar.
