import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import csv
from matplotlib.animation import FuncAnimation
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

def iteraKmeans (dataset,centroides,cantidad,parada):
    nuevoCentroides = []
    nuevoCentroides.append(centroides)
    grupos = generarCluster(dataset,centroides,cantidad)
    centroideAux = Kmeans(dataset,centroides,cantidad)
    i=0
    flag=0
    while i <= parada and flag == 0:
        centroideAux1 = centroideAux
        nuevoCentroides.append(centroideAux)
        centroideAux = Kmeans(dataset,centroideAux,cantidad)
        if(centroideAux1 == centroideAux):
            flag = 1
            print (len(nuevoCentroides))
        grupos = generarCluster(dataset,centroideAux,cantidad)
        i=i+1
        #graficar(centroideAux,grupos,"foto" + str(i))
    return nuevoCentroides

def graficar(centroides,clusters,nombre):
    colores = ['b', 'g', 'r', 'c']
    for i, cluster in enumerate(clusters):
        X = [point[0] for point in cluster]
        Y = [point[1] for point in cluster]
        plt.scatter(X, Y, label=f'Cluster {i + 1}', c=colores[i])

    X_centroides = [centroide[0] for centroide in centroides]
    Y_centroides = [centroide[1] for centroide in centroides]
    plt.scatter(X, Y)
    plt.scatter(X_centroides, Y_centroides, marker='x', label='Centroides', c='k')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.savefig(nombre)
    
    # Cerrar la figura para liberar recursos
    plt.close()

def actualizar_grafico(dataset,listaCentroides,cantidad_cluster,canvas):
        global i
        hasta = len(listaCentroides)
        if(i<hasta):
            print(i)
            centroide = listaCentroides[i]
            grupos1 = generarCluster(dataset, centroide, cantidad_cluster)
            plt.clf()   
            graficar_cluster(centroide, grupos1)
            canvas.draw()
            i=i+1
def recuperadata (i):
    
    urls=['aplicacion/dataset_1.csv','aplicacion/dataset_2.csv','aplicacion/dataset_3.csv']
    formatted_data = []
    with open(urls[i-1], newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Omite la primera línea
        for row in reader:
            formatted_data.append([float(row[0].replace(',', '.')), float(row[1].replace(',', '.'))])
    coordenadas = formatted_data
        
    
    return coordenadas

def Kmeans(data,centroidesAleatorio,cantidad):
    centroidesNuevos = []
    aux = []
    grupos = generarCluster(data,centroidesAleatorio,cantidad)
    for i, grupo in enumerate(grupos):
        centroide = calculoNuevoCentroide(grupo)
        centroidesNuevos.append([centroide[0], centroide[1]])
    
    #graficar(grupos,centroidesNuevos)
    return centroidesNuevos

def distanciaEuclideana(dato, centroide):
    return np.sqrt((dato[0] - centroide[0])**2 + (dato[1] - centroide[1])**2)

def generarCluster(datos, centroides,cantidad):
    clusters = [[] for _ in range(cantidad)]
    
    for dato in datos:
        clusterAux = 0
        distanciaMin = float('inf')
        
        for i, centroide in enumerate(centroides):
            distancia = distanciaEuclideana(dato, centroide)
            if distancia < distanciaMin:
                distanciaMin = distancia
                clusterAux = i
        
        clusters[clusterAux].append(dato)
    
    return clusters

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

def generaAleatorio(dataset,cantidad):
    x = []
    y = []
    dataset_np = np.array(dataset)
    minX = dataset_np[:, 0].min()
    maxX = dataset_np[:, 0].max()
    minY = dataset_np[:, 1].min()
    maxY = dataset_np[:, 1].max()
    centroides = []
    for i in range(cantidad):
        aleatorioX = random.uniform(minX, maxX)
        aleatorioY = random.uniform(minY, maxY)
        centroides.append([aleatorioX, aleatorioY])
    return centroides




#print (listaCentroides)

def graficar_cluster(centroides, cluster):
    colores = ['b', 'g', 'r', 'c', 'y','m']
    
    for i, puntos in enumerate(cluster):
        X = [point[0] for point in puntos]
        Y = [point[1] for point in puntos]
        plt.scatter(X, Y, label=f'Cluster {i + 1}', c=colores[i-1])
    
    X_centroides = [centroide[0] for centroide in centroides]
    Y_centroides = [centroide[1] for centroide in centroides]
    plt.scatter(X_centroides, Y_centroides, marker='x', label='Centroides', c='k')
    
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()

def kmeans_plus(dataset, n_clusters):
    # Selecciona el primer centroide al azar
    dataset = np.array(dataset)
    centroids = [dataset[np.random.choice(len(dataset))]]
    
    while len(centroids) < n_clusters:
        # Calcula las distancias ponderadas para cada punto de datos
        dinstancias = []
        for data in dataset:
            distanciaMin = float('inf')
            for i, centroide in enumerate(centroids):
                distancia = distanciaEuclideana(data, centroide)
                if distancia < distanciaMin:
                    distanciaMin = distancia
        
            dinstancias.append(distanciaMin**2)
        
        # Calcula la probabilidad de selección para cada punto
        prob = dinstancias / sum(dinstancias)
        # Elige el siguiente centroide con probabilidad proporcional
        next_centroid = dataset[np.random.choice(len(dataset), p=prob)]
        
        centroids.append(next_centroid)
    
    return (centroids)

#class vistaPrincipal(QMainWindow):
    