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

class vertice(object):
	def __init__(self,id):
		self.id = id
		self.adyacentes = {}

class Grafo(object):
    
    def __init__(self):
        self.cant_vertices = 0
        self.vertices = {}
    
    def vertice_pertenece(self,vertice):
        if self.vertices.has_key(vertice):
        	return True
        else:
        	return False
            
    def agregar_vertice(self,identificador):
    	if not self.vertice_pertenece(identificador):	
    		self.cant_vertices += 1
        	self.vertices[identificador] = vertice(identificador)

    def quitar_vertice(self,identificador):
    	self.cant_vertices -= 1
    	self.vertices.pop(identificador)
    	for v in self.vertices:
    		self.vertices[v].adyacentes.pop(identificador)

    def identificadores(self):
    	return self.vertices.keys()

    def son_adyacente(self,identificador,adyacente):
        if self.vertice_pertenece(identificador):
        	aux = self.vertices[identificador]
        	if aux.adyacentes.has_key(adyacente):
        		return True
        	else:
        		return False
        else:
        	return False

    def cantidad_vertices(self):
    	return self.cant_vertices

    def agregar_arista(self,id1,id2):
    	aux = self.vertices.get(id2)
    	dic = {id2:aux}
    	self.vertices[id1].adyacentes.update(dic)
    	aux = self.vertices.get(id1)
    	dic = {id1:aux}
    	self.vertices[id2].adyacentes.update(dic)

    def quitar_arista(self,id1,id2):
    	self.vertices[id1].adyacentes.pop(id2, None)
    	self.vertices[id2].adyacentes.pop(id1, None)

    def adyacentes_vertice(self,id):
    	return self.vertices[id].adyacentes      


    def __iter__(self):
        return iter(self.vertices)  


