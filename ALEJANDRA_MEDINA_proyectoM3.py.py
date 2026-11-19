#Proyecto Módulo 3 - Semana 12
#Calidad y despliegue

import random
import matplotlib.pyplot as plt

#Función para simular el recorrido de un canica
def simular_canica(niveles=12):
    """ 
    Simula el recorrido de una canica a través de varios niveles
    
    Parámetros: 
        niveles (int): Número de niveles que recorrerá la canica. Por defecto 12.

    Retorna: 
        int: Número del contenedor final donde termina la canica.
    """

    contenedor = 0

    #Ciclo para simular el recorrido de la canica
    for _ in range(niveles):

        #Decidir aleatoriamente hacia dónde se mueve
        direccion = random.choice(["izquierda", "derecha"])

        if direccion == "derecha":
            contenedor += 1

    return contenedor

#Función para graficar los resultados
def graficar_resultados(datos):
    """
    Genera un histograma de los resultados de la simulación de canicas.

    Parámetros:
        datos (list): Lista con los contenedores finales de las canicas.
    """
    #Generar el histograma
    plt.hist(datos, bins=range(14), edgecolor="black")

    #Agregar etiquetas y título al gráfico
    plt.title("Resultados de la simulación de 3,000 canicas")
    plt.xlabel("Distribución de canicas")
    plt.ylabel("Cantidad de canicas")

    #Mostrar el gráfico
    plt.show()

#Lista para almacenar los resultados de la canicas
resultados = []

#Simular el recorrido de 3,000 canicas
for _ in range(3000):

    resultado = simular_canica()
    resultados.append(resultado)

#Mostrar los resultados de la simulación
print("======== SIMULACIÓN DE 3,000 CANICAS ========")
print("Cantidad de canicas simuladas", len(resultados))
print("Primeros 10 resultados:", resultados[:10])

#Generar el histograma con los resultados de la simulación
graficar_resultados(resultados)