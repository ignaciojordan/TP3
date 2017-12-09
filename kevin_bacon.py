import random
import os
import sys
from grafo import Grafo, Nodo_heap
import heapq
from collections import deque

imdb = grafo_crear(sys.argv[1])

linea=raw_input("Ingrese comando:")
while (cmp(linea,"fin") != 0):
	comando = linea.split(' ',1)
	if(cmp(comando[0],"cantidad_actores") == 0):
		cant_actores = imdb.cantidad_actores() '''hay que ver si podemos crear esta funcion en seis_grados.py'''
		print "El dataset contiene" + str(cant_actores) + "actores"
	if(cmp(comando[0],"cantidad_peliculas") == 0):
		cant_peliculas = imdb.cantidad_peliculas() ''' lo mismo que con la funcion de los actores'''
		print "El dataset contiene" + str(cant_peliculas) + "peliculas"
	if(cmp(comando[0],"camino_hasta_KB") == 0):
	if(cmp(comando[0],"bacon_number") == 0):
	if(cmp(comando[0],"bacon_number_mayor_a_6") == 0):
	if(cmp(comando[0],"bacon_number_infinito") == 0):
	if(cmp(comando[0],"popularidad_contra_KB") == 0):
		kb = popularidad(imdb,'Bacon Kevin')
		otro = popularidad(imdb, comando[1])
		contra_kb = (otro*100)/kb
		print comando[1] + "es un" + str(contra_kb) + "%" + "de lo popular que es Kevin Bacon"
	if(cmp(comando[0],"KBN_promedio") == 0):		
	if(cmp(comando[0],"similares_a_KB") == 0):
		cant_similares = comando[1]
		similares = similares(imdb,'Bacon Kevin', parametro)
		print "Los" + parametro + "mas similares a KB son" + similares
	linea = raw_input("Ingrese comando:")



