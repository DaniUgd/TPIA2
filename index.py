import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def graficar(grupos,centroideNuevo):
    colorGrupo=['blue','red','green','brown','black']
    for i, grupo in enumerate(grupos):
        x_grupo, y_grupo = zip(*grupo)
        plt.scatter(x_grupo, y_grupo, label='Grupo 1', c=colorGrupo[i], marker='o')
    print(grupos)
    print(centroideNuevo)
    #for i, ce in enumerate(centroideNuevo):
     #   x_Centroide,y_centroide = zip(*ce)
      #  plt.scatter(x_Centroide, y_centroide, label='centroide', c='yellow', marker='x')
    # Crear el gráfico de dispersión para cada grupo
    
    # Etiquetas de los ejes y leyenda
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

def recuperadata (i):
    if (i==1):
        with open('dataset_1.csv', 'r') as file:
            lines = file.readlines()[1:]  # Excluir la primera fila
            formatted_lines = [line.replace(',', '.') for line in lines]  # Reemplazar comas por puntos
            coordenadas = np.loadtxt(formatted_lines, delimiter=';')
    elif(i==2):
        with open('dataset_2.csv', 'r') as file:
            lines = file.readlines()[1:]  # Excluir la primera fila
            formatted_lines = [line.replace(',', '.') for line in lines]  # Reemplazar comas por puntos
            coordenadas = np.loadtxt(formatted_lines, delimiter=';')
        
    elif(i==3):
        coordenadas = np.loadtxt('dataset_3.csv', delimiter=';',skiprows=1, decimal=',')
    return coordenadas

def Kmeans(data,centroidesAleatorio):
    
    grupos = group_points(data,centroidesAleatorio)
    centroidesNuevos = []
    for i, grupo in enumerate(grupos):
        x,y = calculoNuevoCentroide(grupo)
        nuevo_centroide = np.array([[x], [y]])
        centroidesNuevos.append(nuevo_centroide) 

    graficar(grupos,centroidesNuevos)
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def group_points(data_matrix, reference_matrix):
    grouped_points = [[] for _ in range(reference_matrix.shape[0])]
    
    for data_point in data_matrix:
        closest_reference_index = 0
        min_distance = float('inf')
        
        for i, reference_point in enumerate(reference_matrix):
            distance = euclidean_distance(data_point, reference_point)
            if distance < min_distance:
                min_distance = distance
                closest_reference_index = i
        
        grouped_points[closest_reference_index].append(data_point)
    
    return grouped_points

 ##NO SIRVE YA QUE HAY QUE CALCULAR LA SUMA EUCLIDIANA DE CADA GRUPO Y DE LOS EJES DE LAS X , DE LAS Y
def calculoNuevoCentroide(grupos):
    sumaX=0
    sumaY=0
    a=0
    for j in grupos:
        for i, c in enumerate(j):
            if(i==0):
                sumaX=sumaX+c
            if(i==1):
                sumaY=sumaY+c
        a=a+1
    sumaX=sumaX/a
    sumaY=sumaY/a
    return sumaX, sumaY
centroides = np.array([
        [4, 2],
        [6, 7.5]
    ])
dataset=recuperadata(1)
Kmeans(dataset,centroides)





## PREGUNTAR COMO CALCULAR EL ALEATORIO  DE LA K