#1. Crear el mapa
def createMap(listV,listE):
    #Verificar que el grafo tenga vértices.
    if listV == []:
        return "El mapa no presenta esquinas." 
    else:
        #Definir el diccionario donde irá el grafo.
        dictionaryGraph = {}
        #Recorrer la lista de vértices del grafo.
        for vertex in listV:
            #Definir lista de adyacencia para cada vértice.
            adjacencyList = []
            #Recorrer la lista de aristas del grafo.
            for edge in listE:
                #Verificar que el vértice sea igual al primer componente de la arista(grafo dirigido).
                if vertex == edge[0]:
                    adjacencyList.append((edge[1],edge[2]))
            dictionaryGraph[vertex] = adjacencyList 
            #Si la lista de adyacencia está vacía es porque el vértice no tiene vértices adyacentes.
            if adjacencyList == []:
                dictionaryGraph[vertex] = None                         
    return dictionaryGraph
    
E = [1,2,3,4,5,6,7,8,9,10,11,12]
C = [(1,2,10),(2,1,10),(1,3,8),(3,1,8),(2,4,8),(4,2,8),(3,5,15),(5,3,15),(4,6,15),(6,4,15),(5,6,5),(5,7,10),(7,5,10),(7,8,10),(8,7,10),(8,9,10),(9,8,10),(8,10,10),(10,8,10),(9,11,10),(11,9,10),(10,5,10),(11,10,10),(10,11,10),(12,10,10),(10,12,10)]
Graph = createMap(E,C)
print(Graph)
print("")

#2. Crear los hash de elementos fijos y moviles. 
class fixed_element():
    name = None
    direction = None 
hash_fixed_element = {}

class movil_element():
    name = None
    direction = None
    amount = 0
hash_movil_element = {}

#2.1. Cargar elementos fijos 
def load_fix_element(name, direction, hash_fixed):
    #Validar entradas.
    if name == "" or direction == []:
        return "Datos no validos"
    #Contemplar solo en minúsculas.
    name = name.upper()
    #Guardar nombre y dirección en una clase(podría no ser necesario -_-).
    elementFix = fixed_element()
    elementFix.name = name
    elementFix.direction = direction
    #Agregar al hash en caso de que no exista.
    if name not in hash_fixed:
        hash_fixed[name] = elementFix
    else:
        return "El elemento se ha ingresado con anterioridad"
    return hash_fixed

load_fix_element("H1", [(3,7),(5,8)], hash_fixed_element)
load_fix_element("A1", [(1,6),(2,4)], hash_fixed_element)
load_fix_element("T1", [(10,5),(11,5)], hash_fixed_element)  
diccFixed = load_fix_element("S1", [(5,1),(6,4)], hash_fixed_element)
#print("Hash de elementos fijos:")
#print(diccFixed)
#print("")
#2.2. Cargar elementos moviles.
def load_movil_element(name, direction, amount, hash_movil):
    #Validar entradas.
    if name == "" or direction == []:
        return "Datos no validos"
    #Contemplar solo en minúsculas.
    name = name.upper()
    #Guardar nombre y dirección en una clase(podría no ser necesario -_-).
    elementMovil = movil_element()
    elementMovil.name = name
    elementMovil.direction = direction
    elementMovil.amount = amount
    #Agregar al hash en caso de que no exista.    
    if name not in hash_movil:
        hash_movil[name] = elementMovil
    else:
        return "El elemento se ha ingresado con anterioridad"
    return hash_movil

load_movil_element("P1", [(1,4),(2,6)], 1500, hash_movil_element)
load_movil_element("P2", [(3,4),(1,4)], 6550, hash_movil_element)
load_movil_element("C1", [(5,3),(7,7)], 2500, hash_movil_element)
load_movil_element("C2", [(12,1),(10,9)], 2500, hash_movil_element)
load_movil_element("C3", [(8,5),(9,5)], 2500, hash_movil_element)
diccMovil = load_movil_element("C4", [(2,3.5),(4,4.5)], 2500, hash_movil_element)
#print("Hash de elementos moviles:")
#print(diccMovil)

#3. Crear el viaje 
#def create_trip(person, element):
    