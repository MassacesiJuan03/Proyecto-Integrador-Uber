#Verificar que los lugares ingresados sean los correctos.
def validar_lugares(lugar):
    """Verifica si es un Hospital,Almacen,Tienda,Supermercado,Escuela,Kiosco o Iglesia"""
    lugares_validos = ('H','A','T','S','E','K','I')
    if lugar[0] in lugares_validos:
        return True
    else:
        return False

#Cargar elementos fijos y moviles al mapa.
def updateMap(map, name, direction):
    """Crear una función para agregar lugares fijos y objetos moviles al mapa"""
    #Ingresar en el mapa si no se encuetra dentro el elemento.
    if name not in map:
        if type(direction) is not list: #Ingresar la dirección al mapa como lista en caso de que no lo sea.
            map[name] = list(direction)
        else:
            map[name] = direction
    for key in map:
        if key == direction[0][0]:
            map[key].append((name,direction[0][1]))
        elif key == direction[1][0]:
            map[key].append((name,direction[1][1]))
    return    
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Todo esto es para Dijktra(INICIO) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
class nodeVertex:
    value = None
    parent = None
    distance = 0
    
def DefinedVertexDijkstra(v,ListNode):
    #Definir cada vértice del grafo como un nodo con sus atributos.
    vertexNode = nodeVertex()
    vertexNode.value = v
    ListNode.append(vertexNode)
    return ListNode

def relax(u, tupleV, listNodes):
    #Obtener el vértice adyacente de u en forma de nodo. 
    for node in listNodes:
        if node.value == tupleV[0]:
            adjVertex = node        
            #Realizar relajo
            if adjVertex.distance > (u.distance + tupleV[1]):
                adjVertex.distance = u.distance + tupleV[1]
                adjVertex.parent = u    
            return

def initRelax(listNodes, v1):
    #Iniciar el relajamiento para cada vértice(nodo) del grafo.
    for node in listNodes:
        node.distance = 999999999
        node.parent = None
    v1.distance = 0
    return
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Todo esto es para Dijktra(FINAL) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#Dijkstra que sirve para buscar los autos más cercanos a la persona.
def dijkstra_allnodes(Graph, person, hash_movil_element):
    """Desde un nodo A el camino mas cerano a todos los nodos"""
    assert Graph != {}, f"El mapa está vacío"
    #Verificar que la persona existe dentro del mapa.
    assert person in Graph, f"La persona {person} no se encuentra en el mapa."
    #Crear la lista de nodos(pasar los vértices a class = Node()).
    listVertex = list(Graph.keys())
    listTypeNodes = []
    for vertex in listVertex:
        listTypeNodes = DefinedVertexDijkstra(vertex, listTypeNodes)
    #Init relax
    for vertexNode in listTypeNodes:
        if vertexNode.value == person: #Buscar persona e iniciar relajo.
            initRelax(listTypeNodes, vertexNode)
            break
    #Definir lista de nodos visitados.
    listVisited = []
    #Ordenar la cola de nodos por su distancia.
    Queue = sorted(listTypeNodes, key=lambda node:node.distance)
    #Definir una lista donde almacenamos el auto y la distancia del auto a la persona.
    list_Distance_And_Cars = []
    while Queue != []:
        #Obtener el primer vértice de la cola.
        u = Queue.pop(0)
        #Agregar el vértice a la lista de visitados.
        listVisited.append(u.value)
        #Obtener los vértices adyacentes de u. Ej: [('e1', 4), ('e2', 6)]
        adjacencyNodes = Graph[u.value]
        #Recorrer la lista de adyacencia de u.
        if adjacencyNodes != None:
            for tuple in adjacencyNodes:
                if tuple[0] not in listVisited:
                    relax(u, tuple, listTypeNodes)
        #Ordenar la cola de nodos por su distancia.
        sorted(listTypeNodes, key=lambda node:node.distance) 
        #Verificar quu el auto cercano pueda llegar a la persona.
        if u.value[0] == "C":
            if dijkstra(Graph, u.value, person) == True:
                #Agregamos a la lista los autos que la persona puede pagar.
                if hash_movil_element[person][1] >= ((u.distance + hash_movil_element[u.value][1]) / 4):  #Ej del hash: [[("e1",4),("e2",6)], 1500]
                    list_Distance_And_Cars.append((u.value,u.distance))
            if len(list_Distance_And_Cars) == 3: 
                return list_Distance_And_Cars  #Devolver la lista con el ranking de los 3 autos más cercanos que la persona puede pagar.  
    #En el peor de los casos es que no hayan al menos 3 autos, devolver error.
    assert list_Distance_And_Cars == 3, f"No sé pudieron devolver al menos tres autos."

#Dijktra que sirve para verificar que el auto pueda llegar a la posición de la persona.
def dijkstra(Graph, car, person):
    """Busca la distancia mas corta entre un nodo A y un nodo B"""
    assert Graph != {}, f"El mapa está vacío"
    #Verificar que los vértices v1 y v2 existen dentro del mapa.
    assert person in Graph, f"La persona {person} no sé encuentra en el mapa."
    assert car in Graph, f"El auto {car} no sé encuentra en el mapa."
    assert person in Graph and car in Graph, f"La persona {person} y el auto {car} no sé encuentran en el mapa."
    #Crear la lista de nodos(pasar los vértices a class = Node()).
    listVertex = list(Graph.keys())
    listTypeNodes = []
    for vertex in listVertex:
        listTypeNodes = DefinedVertexDijkstra(vertex, listTypeNodes)
    #Init relax
    for vertexNode in listTypeNodes:
        if vertexNode.value == car:
            initRelax(listTypeNodes, vertexNode)
            break
    #Definir lista de nodos visitados.
    listVisited = []
    #Ordenar la cola de nodos por su distancia.
    Queue = sorted(listTypeNodes, key=lambda node:node.distance)
    while Queue != []:
        #Obtener el vértice de la cola.
        u = Queue.pop(0)
        #Retorno True, si se cumple que puede llegar el auto a la persona.
        if u.value == person:
           return True
        #Agregar el vértice a la lista de visitados.
        listVisited.append(u.value)
        #Obtener los vértices adyacentes de u.
        adjacencyNodes = Graph[u.value]
        #Recorrer la lista de adyacencia de u.
        if adjacencyNodes != None:
            for vertex in adjacencyNodes:
                if vertex[0] not in listVisited:
                    relax(u,vertex, listTypeNodes)
        #Ordenar la cola de nodos por su distancia.
        sorted(listTypeNodes, key=lambda node:node.distance)
    #Retorno False ya que recorrí todo el mapa y nunca pude llegar a la persona.
    return False

#Obtener el camino más corto entre dos direcciones.
def camino_mas_corto(Graph, direction_1, direction_2): #¿Para direcciones de tipo {("e3",7),("e5",8)}?
    """retorna el camino mas corto entre las dos direcciones"""
    assert Graph != {}, f"El mapa está vacío"
    #Verificar que las esquinas de las direcciones existen dentro del mapa.
    direction_1 = list(direction_1)
    direction_2 = list(direction_2)
    assert direction_1[0][0] in Graph, f"La esquina {direction_1[0][0]} de la {direction_1} no sé encuentra en el mapa"
    assert direction_1[1][0] in Graph, f"La esquina {direction_1[1][0]} de la {direction_1} no sé encuentra en el mapa" 
    assert direction_2[0][0] in Graph, f"La esquina {direction_2[0][0]} de la {direction_2} no sé encuentra en el mapa"
    assert direction_2[1][0] in Graph, f"La esquina {direction_2[1][0]} de la {direction_2} no sé encuentra en el mapa" 
    #Obtener los nombres de la direcciones inicial y final.
    listVertex = list(Graph.keys())
    final_destination = "Destino Final" #Se actualiza a un lugar fijo en el caso de que la dirección esté asignada a este.
    for key in listVertex:
        if Graph[key] == direction_1:
            person = key
        elif Graph[key] == direction_2:
            final_destination = key
    #En el caso de que el destino no sé encuentre en el mapa lo ingreso.
    if final_destination == "Destino Final":
        updateMap(Graph, final_destination, direction_2)
    #Crear la lista de nodos(pasar los vértices a class = Node()).
    listTypeNodes = []
    for vertex in listVertex:
        listTypeNodes = DefinedVertexDijkstra(vertex, listTypeNodes)
    #Init relax
    for vertexNode in listTypeNodes:
        if vertexNode.value == person:
            initRelax(listTypeNodes, vertexNode)
            break
    #Definir lista de nodos visitados.
    listVisited = []
    #Ordenar la cola de nodos por su distancia.
    Queue = sorted(listTypeNodes, key=lambda node:node.distance)
    while Queue != []:
        #Obtener el vértice de la cola.
        u = Queue.pop(0)
        #Si se cumple es que llegue a la dirección de destino.
        if u.value == final_destination:
           #Obtener el camino más corto de "D1" a "D2".
                listShortestPath = []
                while u.parent != None:
                    listShortestPath.insert(0, u.value)
                    u = u.parent
                listShortestPath.insert(0, u.value)
                return listShortestPath
        #Agregar el vértice a la lista de visitados.
        listVisited.append(u.value)
        #Obtener los vértices adyacentes de u.
        adjacencyNodes = Graph[u.value]
        #Recorrer la lista de adyacencia de u.
        if adjacencyNodes != None:
            for vertex in adjacencyNodes:
                if vertex[0] not in listVisited:
                    relax(u,vertex, listTypeNodes)
        #Ordenar la cola de nodos por su distancia.
        sorted(listTypeNodes, key=lambda node:node.distance)
    #Retorno False ya que recorrí todo el mapa y nunca pude llegar a la dirección de destino.
    return False


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Funciones importantes(INICIO)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
#1. Crear el mapa
def create_map(listV, listE):
    """Retorna un hash con el grafo mapa"""
    map = {}
    for vertex in listV:
        map[vertex] = []
    for edge in listE:
        #Extraemos desde la arista v1 = vertice_1 , v2 = vertice_2 , c = costo
        v1 , v2 , c = edge 
        map[v1].append((v2,c))    
    return map
    
E = ["e1","e2","e3","e4","e5","e6","e7","e8","e9","e10","e11","e12"]
C = [("e1","e2",10),("e2","e1",10),("e1","e3",8),("e3","e1",8),("e2","e4",8),("e4","e2",8),("e3","e5",15),("e5","e3",15),("e4","e6",15),("e6","e4",15),("e5","e6",5),("e5","e7",10),("e7","e5",10),("e7","e8",10),("e8","e7",10),("e8","e9",10),("e9","e8",10),("e8","e10",10),("e10","e8",10),("e9","e11",10),("e11","e9",10),("e10","e5",10),("e11","e10",10),("e10","e11",10),("e12","e10",10),("e10","e12",10)]
map = create_map(E, C)
print(map)
print("")

#2. Crear los hash de elementos fijos y moviles. 
hash_fixed_element = {}
hash_movil_element = {}

#2.1. Cargar elementos fijos 
def load_fix_element(map, name, direction, hash_fixed):
    #Validar entradas.
    if name == "" or direction == []:
        return "Datos no validos"
    #Validar elemento fijo.
    assert validar_lugares(name) == True, f" Incorrecto, no es posible cargar esté lugar"
    #Validar que la dirección exista dentro del mapa.
    direction = list(direction)
    assert direction[0][0] in map, f"La esquina {direction[0][0]} de la {direction} no sé encuentra en el mapa"
    assert direction[1][0] in map, f"La esquina {direction[1][0]} de la {direction} no sé encuentra en el mapa" 
    #Agregar al hash en caso de que no exista.
    assert name not in hash_fixed, f"Elemento repetido, el lugar {name} ya se encuentra cargado en el mapa"
    hash_fixed[name] = direction
    updateMap(map, name, direction)
    return hash_fixed
      
load_fix_element(map, "H1", {("e3",7),("e5",8)}, hash_fixed_element)
load_fix_element(map, "A1", {("e1",6),("e2",4)}, hash_fixed_element)
load_fix_element(map, "T1", {("e10",5),("e11",5)}, hash_fixed_element)  
diccFix = load_fix_element(map, "S1", {("e5",1),("e6",4)}, hash_fixed_element)
print("Hash de elementos fijos:")
print(diccFix)
print()

#2.2. Cargar elementos moviles.
def load_movil_element(map ,name, direction, amount, hash_movil):
    #Validar entradas.
    if name == "" or direction == []:
        return "Datos no validos"
    #Validar elemento movil.
    if name[0] != "P" or name[0] != "C":
        assert f"Elemento móvil incorrecto, no es posible cargar {name}"
    #Validar que la dirección exista dentro del mapa.
    direction = list(direction)
    assert direction[0][0] in map, f"La esquina {direction[0][0]} de la {direction} no sé encuentra en el mapa"
    assert direction[1][0] in map, f"La esquina {direction[1][0]} de la {direction} no sé encuentra en el mapa" 
    #Agregar al hash en caso de que no exista.
    assert name not in hash_movil or name[0] == "C", f"Elemento repetido, la persona {name} ya se encuentra cargado en el mapa"
    assert name not in hash_movil or name[0] == "P", f"Elemento repetido, el auto {name} ya se encuentra cargado en el mapa"
    hash_movil[name] = [direction,amount]
    #Agregar los autos al mapa(las personas serán ingresadas luego cuando se validen los viajes).
    if name[0] == "C":
        updateMap(map, name, direction)
    return hash_movil

load_movil_element(map ,"P1", {("e1",4),("e2",6)}, 1200, hash_movil_element)
load_movil_element(map, "P2", {("e3",4),("e1",4)}, 500, hash_movil_element)
load_movil_element(map, "C1", {("e5",3),("e7",7)}, 2500, hash_movil_element)
load_movil_element(map, "C2", {("e12",1),("e10",9)}, 2500, hash_movil_element)
load_movil_element(map, "C3", {("e8",5),("e9",5)}, 2500, hash_movil_element)
diccMovil = load_movil_element(map, "C4", {("e2",3.5),("e4",4.5)}, 2500, hash_movil_element)
print("Hash de elementos moviles:")
print(diccMovil)
print()

#3. Buscar los tres autos más cercanos a la persona.
def encontrar_autos_cercanos(map, persona, hash_movil_element):
    """retorna una tupla de los 3 autos mas cercanos"""
    assert persona[0] == "P", f"Incorrecto, {persona} no es una persona"
    direction = hash_movil_element[persona][0] 
    #Se ingresa la persona al mapa.
    updateMap(map, persona, direction)
    #Se buscan los tres autos que puede pagar más cercanos a la persona.
    listNearbyCars = dijkstra_allnodes(map, persona, hash_movil_element)
    return listNearbyCars

lista_autos_cercanos = encontrar_autos_cercanos(map, "P1", diccMovil)   
print(lista_autos_cercanos)

a = camino_mas_corto(map, {("e1",4),("e2",6)}, {("e7",5),("e8",5)})
print(a)
#4- Crear viaje
def create_trip(map, person, direction, hash_movil_element, hash_fix_element):
    """Crea el viaje de uber"""
    print(f'------ Bienvenido {person} ------')
    #Validar la dirección.
    direction = eval("direction")
    if type(direction) is str: #Dirección de lugar fijo, por ej: "S1", "A5", "H2".
        assert validar_lugares(direction) is True, f"Dirección Inválida"
        direction = hash_fix_element[direction] #Obtener la dirección de un lugar fijo.
    else: #Dirección de lugar fijo, por ej: {("e3",7),("e5",8)}.
        direction = list(direction)
        assert direction[0][0] in map, f"La esquina {direction[0][0]} de la {direction} no sé encuentra en el mapa"
        assert direction[1][0] in map, f"La esquina {direction[1][0]} de la {direction} no sé encuentra en el mapa" 
    #Buscar los tres autos que la persona puede pagar más cercanos.
    autos_cercanos = encontrar_autos_cercanos(map, person, hash_movil_element)
    #Casos 1 -> No hay autos cercanos
    if not autos_cercanos:
        print('-- No hay autos cercanos que puedan realizar el viaje --')
        return
    #Caso 2 -> Muestra una lista de autos cercanos
    print('####Estos son los autos mas cercanos####')
    print('Elegir entre:')
    indice = 0
    for auto in autos_cercanos:
        if indice == 0:
            print('|Autos|Costo|')
        print(auto)
        indice += 1
    #Elije el auto
    auto = str(input('Elija un auto: '))
    auto = auto.upper()
    #Validación del auto
    while (auto[0] != "C") or (int(auto[1]) > indice):
        print('// Auto Invalido, vuelva a ingresar //')
        auto = str(input('Elija un auto: '))
        auto = auto.upper()
    #Crea el camino hacia destino.
    direction_person = hash_movil_element[person][0]
    camino_destino = camino_mas_corto(map, direction_person, direction)
    #Actualizar direcciones en el mapa de la persona y el auto.
    map[auto] = direction
    map[person] = direction
    #Actualizar direcciones en el hash de la persona y el auto.
    hash_movil_element[auto][0] = direction
    hash_movil_element[person][0] = direction 
    #Actualizar monto de la persona en el hash.
    for car in autos_cercanos:
        if car[0] == auto:
            distance = car[1] #Obtengo la distancia (auto --> persona)
    hash_movil_element[person][1] = (hash_movil_element[person][1] - ((distance +  hash_movil_element[auto][1]) / 4))
    #Validar que el camino de destino exista.
    if camino_destino != False:
        return camino_destino
    else:
        return
b = create_trip(map, "P1", {("e7",5),("e8",5)}, diccMovil, diccFix)
print(b)
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Funciones importantes(FINAL)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

