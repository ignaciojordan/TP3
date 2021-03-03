import random
import os
import sys
from grafo import Grafo, Nodo_heap, vertice
import heapq
from collections import deque


def random_walks(grafo,vertice,largo,visitados):
	if largo > 0:
		adyacentes = grafo.adyacentes_vertice(vertice)
		siguiente = random.choice(adyacentes.keys())
		if (not siguiente in visitados.keys()):
			visitados[siguiente] = 1
		else:
			visitados[siguiente] += 1
		random_walks(grafo,siguiente,largo-1,visitados)
	return

def bfs(grafo, origen):
    visitados = {} #diccionario
    orden = {}
    orden[origen] = 0
    bfs_visitar(grafo, origen, visitados, orden)
    return orden

def bfs_visitar(grafo, origen, visitados, orden):
    q = deque()
    q.append(origen)
    visitados[origen] = True
    while len(q) > 0:
        v = q.popleft()
        for w in grafo.adyacentes_vertice(v):
            if w not in visitados:
                visitados[w] = True
                orden[w] = orden[v] + 1
                q.append(w)




youtube = Grafo()
with open(sys.argv[1], "r") as archivo:
	auxiliar = 0
	for linea in archivo:
		if auxiliar >= 4:
			ids = linea.split('\t',1)
			aux = ids[1].split('\n',1)
			id1 = ids[0]
			id2 = aux[0]
			youtube.agregar_vertice(id1)
			youtube.agregar_vertice(id2)
			youtube.agregar_arista(id1,id2)
		auxiliar += 1

linea=raw_input("Ingrese comandoXxxdd:")
while (cmp(linea,"fin") != 0):
	comando = linea.split(' ',1)
	print comando
	if (cmp(comando[0],"estadisticas") == 0):
		cant_vertices = youtube.cantidad_vertices()
		print "Cantidad de Vertices:" + str(cant_vertices)
		cant_aristas = 0
		for v in youtube:
			aux = youtube.adyacentes_vertice(v)
			cant_aristas += len(aux)
		cant_aristas = cant_aristas/2
		grado = cant_aristas/cant_vertices
		print "Cantidad de Aristas:" + str(cant_aristas)
		print "Promedio de grado de entrada de cada vértice:" + str(grado)
		print "Promedio de grado de salida de cada vértice:" + str(grado)
		print "Densidad del grafo:" + str(float(2*cant_aristas/(cant_vertices*(cant_vertices-1))))
	#if(cmp(comando[0],"comunidades") == 0):#comunidades
	if(cmp(comando[0],"similares") == 0):
		parametro = comando[1].split(' ',1)
		visitados = {}
		random_walks(youtube,parametro[0],500,visitados)
		heap = []
		for vertice in visitados:
			nodo = Nodo_heap(visitados[vertice], vertice)
			heapq.heappush(heap, nodo)
		i = 0
		h = int(parametro[1])
		while i < h:
			nodo = heapq.heappop(heap)
			if (nodo.vertice != parametro[0]):
				print nodo.vertice
				i +=1
	if(cmp(comando[0],"distancias") == 0):
		caminos = bfs(youtube,comando[1])
		distancia = []
		i = 0
		while i < len(caminos):
			distancia[i] = 0
			i+=1
		for vertice in caminos:
			distancia[caminos[vertice]] += 1
		for i in range (0, len(distancia)):
			print "Distancia " + str(i) +":"+ str(distancia[i])
			

	#if(cmp(comando[0],"centralidad") == 0):
	#	parametro = un_parametro(linea, len(comando) + 1)
	#if(cmp(comando[0],"camino") == 0):
	#	parametros = dos_parametros(linea, len(comando) + 1)
	if(cmp(comando[0],"recomendar") == 0):
		parametro = comando[1].split(' ',1)
		visitados = {}
		random_walks(youtube,parametro[0],500,visitados)
		heap = []
		for vertice in visitados:
			nodo = Nodo_heap(visitados[vertice], vertice)
			heapq.heappush(heap, nodo)
		i = 0
		while i < int(parametro[1]):
			nodo = heapq.heappop(heap)
			if (not youtube.son_adyacente(parametro[0],nodo.vertice) and parametro[0] != nodo.vertice):
				i += 1
				print nodo.vertice

	linea = raw_input("Ingrese comando:")



