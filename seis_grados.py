from grafo import Grafo



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
    padre = {}
    for v in grafo:
    	if v not in visitados:
    		padre[v] = None
    		orden[v] = 0
    		bfs_visitar(grafo, origen, visitados, orden, padre)
    return orden,padre

def bfs_visitar(grafo, origen, visitados, orden, padre):
    q = deque()
    q.append(origen)
    visitados[origen] = True
    while len(q) > 0:
        v = q.popleft()
        for w in grafo.adyacentes_vertice(v):
            if w not in visitados:
                visitados[w] = True
                padre[w] = v
                orden[w] = orden[v] + 1
                q.append(w)

def grafo_crear(nombre_archivo):
    """
    Crea un grafo de conexiones de actores a partir de un archivo de datos.

    PRE: Recibe el nombre de un archivo separado por comas que contenga de lineas:
        actor,pelicula,pelicula,pelicula
        que equivalen a: vertice,arista,arista,arista
    POST: Devuelve un grafo creado a partir de estos datos.
    """
    with open(nombre_archivo, "r") as archivo:
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
    raise NotImplementedError


def camino(grafo, origen, llegada):
    """
    Devuelve el camino entre un actor de origen y uno de llegada.

    PRE: Recibe el grafo, un actor de origen y un actor de llegada.
    POST: Devuelve una lista ordenada de cadenas (películas) para llegar desde
        el origen hasta el final.
    """

    distancias,padres = bfs(grafo, origen)
    padre = padres[llegada]
    aux = llegada
    i = 0
    lista = []
    while (cmp(padre,origen) != 0):
    	peliculas = grafo.adyacentes_vertice(aux)
    	lista[i] = (padre,aux,pelicula[padre])
    	aux = padre
    	padre = padre[aux]
    	i += 1
    lista.reverse()
    return lista
    raise NotImplementedError


def actores_a_distancia(grafo, origen, n):
    """
    Devuelve los actores a distancia n del recibido.

    PRE: Recibe el grafo, el actor de origen y el número deseado.
    POST: Devuelve la lista de cadenas (actores) a n pasos del recibido.
    """
    distancias,padres = bfs(grafo, origen) #diccionario con todos los actores como claves y su distancia como valor
    actores_distancia = []
    i = 0
    for x in distancias:
    	if distancias[x] == n:
    		actores_distancia[i] = x
    		i+=1
    return actores_distancia

    raise NotImplementedError


def popularidad(grafo, actor):
    """
    Calcula la popularidad del actor recibido.

    PRE: Recibe el grafo y un actor de origen
    POST: Devuelve un entero que simboliza la popularidad: todos los adyacentes
        de los adyacentes del actor, multiplicado por su cantidad de peliculas
    """
    cant_actores_2 = 0
    distancias = bfs(grafo, origen)
    for x in distancias:
    	if distancias[x] == 2:
    		cant_actores_2 += 1
    adyacentes = grafo.adyacentes_vertice(actor)
    cant_adyacentes = len(adyacentes)
    return cant_actores_2 * cant_adyacentes

    raise NotImplementedError


def similares(grafo,origen, n):
    """
    Calcula los n actores más similares al actor de origen y los devuelve en una
    lista ordenada de mayor similitud a menor.

    PRE: Recibe el grafo, el actor de origen, y el n deseado
    POST: Devuelve una lista de los n actores no adyacentes más similares al
        pedido. La lista no debe contener al actor de origen.
    """
    visitados = {}
    similares = []
	random_walks(grafo,origen,500,visitados)
	heap = []
	for vertice in visitados:
		nodo = Nodo_heap(visitados[vertice], vertice)
		heapq.heappush(heap, nodo)
	i = 0
	h = n
	while i < h:
		nodo = heapq.heappop(heap)
		if (nodo.vertice != origen) and (nodo.vertice not in grafo.adyacentes_vertice(origen)):
			similares[i] = nodo.vertice
			i +=1
	return similares
    raise NotImplementedError
