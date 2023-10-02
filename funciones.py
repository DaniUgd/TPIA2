import numpy as np
import random
import csv
import time
from PyQt5.QtCore import QCoreApplication

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


def graficar_en_bucle(dataset, listaCentroides, cantidad_cluster, km):
    hasta = len(listaCentroides)
    km.iniciar_estado()
    estado = km.obtener_estado()
    ##agregar algo para bloquear estado
    i = km.obtener_i()
    while estado !=1:
        if(i<(hasta-1)):
            graficar_siguiente(dataset,listaCentroides,cantidad_cluster,km)
            QCoreApplication.processEvents()
            time.sleep(1)
            i=km.obtener_i()
        else:
            estado = 1  

def detener_grafico(km):
    km.parar_estado() 

def graficar_siguiente(dataset,listaCentroides,cantidad_cluster,km):
        km.canvas.axes.clear()
        hasta = len(listaCentroides)
        i=km.obtener_i()
        if(i<hasta):
            km.incrementar_i()
            i=km.obtener_i()
            grupos1 = generarCluster(dataset, listaCentroides[i], cantidad_cluster) 
            graficar_cluster(km.canvas.axes,listaCentroides[i], grupos1)
            km.canvas.draw()

def inicia_grafico(dataset,listaCentroides,cantidad_cluster,km):
        km.canvas.axes.clear()
        i=km.obtener_i()
        grupos1 = generarCluster(dataset, listaCentroides[i], cantidad_cluster)  
        graficar_cluster(km.canvas.axes,listaCentroides[i], grupos1)
        km.canvas.draw()            

def graficar_anterior(dataset,listaCentroides,cantidad_cluster,km):
        km.canvas.axes.clear()
        i=km.obtener_i()
        if(i>0):
            km.decrementar_i()
            i=km.obtener_i()
            grupos1 = generarCluster(dataset, listaCentroides[i], cantidad_cluster) 
            graficar_cluster(km.canvas.axes,listaCentroides[i], grupos1)
            km.canvas.draw()

            

def recuperadata (i):
    
    urls=['dataset_1.csv','dataset_2.csv','dataset_3.csv']
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
   
    """
     #en esta parte se obtiene los indices de los cluster vacios (pueden ser mas de 1)
    clusters_vacios = [i for i, cluster in enumerate(grupos) if not cluster]
    if clusters_vacios:
        #se calcula los sse (qe es la distancia cuadrad, nos ayudamos del la distancia euclidiana)
        print("Clusters vacíos:", clusters_vacios)
        sse=calcularSSE(grupos,centroidesAleatorio)
        indices_mayores_sse = sorted(range(len(sse)), key=lambda i: sse[i], reverse=True)[:len(clusters_vacios)]
        agregarClusterVacios(grupos,sse,clusters_vacios,indices_mayores_sse)

        print("son los sse")
        print(sse)
        """
    for i, grupo in enumerate(grupos):
        centroide = calculoNuevoCentroide(grupo)
        centroidesNuevos.append([centroide[0], centroide[1]])
    
    #graficar(grupos,centroidesNuevos)
    return centroidesNuevos

def distanciaEuclideana(dato, centroide):
    return np.sqrt((dato[0] - centroide[0])**2 + (dato[1] - centroide[1])**2)

def calcularSSE(clusters, centroides):
    sses = []  # Lista para almacenar los SSE de cada cluster
    for i, cluster in enumerate(clusters):
        centroide = centroides[i]
        sse = 0
        for dato in cluster:
            distancia = distanciaEuclideana(dato, centroide)
            sse += distancia ** 2
        sses.append(sse)  # Agregar el SSE del cluster actual a la lista
    return sses
#esta funcion agrega 1 dato para cada cluster vacio para que sea el centroides
#def agregarClusterVacios(grupos,sse,clusters_vacios,indices_mayores_sse):



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
def graficar_dataset(plt, dataset):
    X_centroides = [centroide[0] for centroide in dataset]
    Y_centroides = [centroide[1] for centroide in dataset]
    plt.scatter(X_centroides, Y_centroides, marker='x', label='Dataset', c='b')
    '''
    plt.scatter(X_centroides, Y_centroides, marker='x', label='Dataset', c='b')
    
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
'''
def graficar_cluster(plt,centroides, cluster):
    colores = ['b', 'g', 'r', 'c', 'y','m']
    
    for i, puntos in enumerate(cluster):
        X = [point[0] for point in puntos]
        Y = [point[1] for point in puntos]
        plt.scatter(X, Y, label=f'Cluster {i + 1}', c=colores[i-1])
    
    X_centroides = [centroide[0] for centroide in centroides]
    Y_centroides = [centroide[1] for centroide in centroides]
    plt.scatter(X_centroides, Y_centroides, marker='x', label='Centroides', c='k')
    
    '''plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()'''

def kmeans_plus(dataset, n_clusters):
    # Selecciona el primer centroide al azar
    dataset = np.array(dataset)
    centroideInicial = dataset[np.random.choice(len(dataset))]
    centroides = []
    centroides.append([centroideInicial[0],centroideInicial[1]])
    while len(centroides) < n_clusters:
        # Calcula las distancias ponderadas para cada punto de datos
        dinstancias = []
        for data in dataset:
            distanciaMin = float('inf')
            for i, centroide in enumerate(centroides):
                distancia = distanciaEuclideana(data, centroide)
                if distancia < distanciaMin:
                    distanciaMin = distancia
        
            dinstancias.append(distanciaMin**2)
        
        # Calcula la probabilidad de selección para cada punto
        prob = dinstancias / sum(dinstancias)
        # Elige el siguiente centroide con probabilidad proporcional
        centroide_aux = dataset[np.random.choice(len(dataset), p=prob)]
        centroides.append([centroide_aux[0],centroide_aux[1]])
    return (centroides)
