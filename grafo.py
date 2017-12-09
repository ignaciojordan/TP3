import random
import os
import sys


class Nodo_heap(object):
    def __init__(self,dato,vertice):
        self.dato = dato
        self.vertice = vertice
    
    def obtener_valor():
        return dato
    
    def __cmp__(self,other):
        if self.dato<other.dato: return 1
        if self.dato>other.dato: return -1
        return 0
    
    def __str__(self):
        return str(self.dato)
    
    def __repr__(self):
        return str(self.dato)    

'''class vertice(object):
	def __init__(self,id):
		self.id = id
		self.adyacentes = {}'''

class Grafo(object):
    
    def __init__(self):
        self.cant_vertices = 0
        self.cant_aristas = 0
        self.vertices = {}
    #funciones auxiliares
    def vertice_pertenece(self,vertice):
        return vertice in self.vertices

    def cantidad_vertices(self):
        return self.cant_vertices

    def cantidad_aristas(self):
        return self.cant_aristas
    #primitiva vertice        
    def agregar_vertice(self,vertice):
    	if not self.vertice_pertenece(vertice):	
    		self.cant_vertices += 1
        	self.vertices[vertice] = {}

    def quitar_vertice(self,vertice):
    	self.cant_vertices -= 1
    	self.vertices.pop(vertice)
    	

    def obtener_vertices(self):
    	return self.vertices

    def adyacentes_vertice(self,vertice):
        return self.vertices[vertice] 

    def son_adyacente(self,vertice,adyacente):
        if not self.vertice_pertenece(vertice):
            return false
        return adyacente in self.vertices[vertice]

    #primitivas arista
    def agregar_arista(self,arista,vertice1,vertice2):
    	if not self.son_adyacente(vertice1,vertice2):
            self.vertices[vertice1][vertice2] = [arista]
            self.vertices[vertice2][vertice1] = [arista]
            self.cant_aristas += 1
            return 
        self.vertices[vertice1][vertice2].append(arista)
        self.vertices[vertice2][vertice1].append(arista)
        return
        

    def quitar_arista(self,vertice1,vertice2):
    	del self.vertices[vertice1][vertice2]
    	del self.vertices[vertice2][vertice1]    


    def __iter__(self):
        return iter(self.vertices)  



