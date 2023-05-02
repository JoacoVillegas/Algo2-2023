"""Ejercicio 1
Implementar la función crear grafo que dada una lista de vértices y una lista de aristas cree un grafo con la representación por Lista de Adyacencia.

def createGraph(List, List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una conexión entre dos vértices.
Salida: retorna el nuevo grafo"""

class GraphNode:
  vertex = None
  conectList = None
  #aca esta el cambio que decia: ¿Y si solo lo guardara en la primera posicion?
  EdgesListofGraph = None

  #Para BFSTree y DFSTree:
  color = None
  distance = None
  parent = None

  #especiales para DFSTree:
  timeD = None
  timeF = None
  
  
def createGraph(LV,LA):
  listAdyacencia = []
  for i in range(len(LV)):
    Node = GraphNode()
    Node.vertex = LV[i]
    #Node.conectList = []
    listAdyacencia.append(Node)
    
  for i in range(len(LV)):
    listAdyacencia[i].conectList = []
    for j in range(len(LA)):
      if LV[i] == LA[j][0]:
        listAdyacencia[i].conectList.append(LA[j][1])
      elif LV[i] == LA[j][1]:
        listAdyacencia[i].conectList.append(LA[j][0])
  listAdyacencia[0].EdgesListofGraph = LA
  return listAdyacencia
        
listVertice = [1,2,3,4,5,6,7]
listAristas = [(2,7),(1,5),(3,4),(4,6),(5,7),(2,6),(6,5),(3,7)]
graph = createGraph(listVertice,listAristas)
print("Grafo: ",graph[3].conectList)
print("¿Cuantos vertices tiene?: ", len(graph))
"""Ejercicio 2
Implementar la función que responde a la siguiente especificación.

def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario."""

#Cada dia se aprende algo nuevo, voy a hacer uso del bloque try-except, veamos si funciona. Tengo entendido que no puedo realizar comparaciones con valueError, pero si crear una funcion que con try except (funciona como un if- else) y asi poder retornar lo que yo necesite.

def busquedaElemento(lista, elemento):
  try:
    indice = lista.index(elemento)
    return indice
  except ValueError:
    return None
    
#La idea de esta funcion es recibe un Nodo (primero seguramente que es el que tiene a v1),vamos a agregarlo a la lista de los vertices pasados (para asi no formar un bucle), me fijo si en su lista de conexiones ESTA el v2. Si no es asi, recorro toda la lista de conexiones de la siguiente forma, voy comprobando si esos vertices estan en la lista de vertices pasados, si no estan, voy a buscarlos en mi lista Grafo para asi realizar recursividad. si en el Search me devuelve un true, es porque lo encontro. 
def existPathR(verticesPasados, Grafo, Nodo, v2):
  verticesPasados.append(Nodo.vertex)
  if busquedaElemento(Nodo.conectList,v2) != None:
    return True
  for verticesConectados in Nodo.conectList:
    if busquedaElemento(verticesPasados, verticesConectados) == None:
      siguienteVertice = verticesConectados
      for nuevoVertice in Grafo:
        if nuevoVertice.vertex == siguienteVertice:
          search = existPathR(verticesPasados, Grafo, nuevoVertice, v2)
          
          if search == True:
            return True
  return False
    
def existPath(Grafo, v1, v2):
  myNode = None
  #aca al principio unos casos base, si el grafo no tiene vertices o si v1 y v2 son el mismo vertice.
  if Grafo == None or len(Grafo) == 0:
    return False

  if v1 == v2:
    return True
  #aca lo que hacemos es buscar el v1 en Grafo, si lo encontro defino una variable llamada myNode para asi luego, si es None retorna falso(porque nunca encontro a v1), y si no es asi sigue.
  for recorridoVertices in Grafo:
    if recorridoVertices.vertex == v1:
      myNode = recorridoVertices
      break
  if myNode == None:
    return False
  #aca tambien, podemos decir un caso base. si Justo en la lista de vertices conectados a v1 llega a estar v2, se retorna true.
  if busquedaElemento(myNode.conectList,v2) != None:
    return True

  listaVerticesPasados = []
  return existPathR(listaVerticesPasados, Grafo, myNode, v2)

print(existPath(graph, 1, 6))

def isConnected(Grafo):
  if Grafo == None or len(Grafo) == 0:
    return False

  for vertices in Grafo:
    for vertices2 in Grafo:
      if existPath(Grafo, vertices.vertex, vertices2.vertex) == False:
        return False
  return True

print(isConnected(graph))

#Voy a realizar un cambio en la clase GraphNode, de modo tal que se queden guardadas las listas con las que se creo en createGraph (Para simplificar la implementacion, pero en el caso de que no tuviera que hacer esto, deberia recorrer la lista de adyacencia, formando duplas de vuelta y agregarlas a una lista que me muestre cuales estan siendo contadas. Al ir recorriendo, voy a encontrarme con las mismas duplas, por eso en caso de que cuando haga un search y no esten en la lista mencionada, cuento una mas y la agrego.)
def isTree(Grafo):
  if Grafo == None or len(Grafo) == 0:
    return False

  if len(Grafo[0].EdgesListofGraph) == len(Grafo)-1 and isConnected(Grafo) == True:
    return True
  else:
    return False
print(isTree(graph))

def convertTree(Grafo):
  Lista = []
  #voy a recorrer lo que seria mi Grafo con doble bucle, es decir que por ejemplo, para v1 voy a pasar por v2, v3, v4, v5 y comparar sus conexiones. Luego el siguiente seria comparar las conexiones de v2 con v1, v3, v4, v5, y asi sucesivamente.
  for vertice1 in Grafo:
    for vertice2 in Grafo:
      cont = 0
      subLista = []
      if vertice1 != vertice2:
        for conexionesv1 in vertice1.conectList:
          #el caso de donde justo es el vertice2.vertex y no dentro de su lista de conexiones
          if conexionesv1 == vertice2.vertex:
            cont += 1 
            subLista.append((vertice1.vertex, conexionesv1))
          #el caso donde aca si hay que entrar a la lista de conexiones, aca debo de agregar dos duplas, uno con vertice1.vertex y el vertice2.vertex
          if busquedaElemento(vertice2.conectList, conexionesv1) != None:
            cont += 1 
            subLista.append((vertice2.vertex, conexionesv1))
            subLista.append((vertice1.vertex, conexionesv1))
        #si el contador es mayor o igual a 2, es que estamos en caso de un ciclo
        if cont >= 2:
          Lista.append(subLista)
  return Lista    

print(convertTree(graph))

def countConnections(Grafo):
  #un caso base, si el grafo es conexo entonces solamente hay 1 componente
  if isConnected(Grafo) == True:
    return 1
  listaCC = []
  #bucles anidados para formar listas de componentes conexas
  for vertice1 in Grafo:
    subLista = []
    subLista.append(vertice1.vertex)
    for vertice2 in Grafo:
      if vertice1 != vertice2:
        if existPath(Grafo, vertice1.vertex, vertice2.vertex) == True:
          subLista.append(vertice2.vertex)
    #Ordeno la lista, para asi luego evitar repeticiones y tener bien contadas las componentes conexas
    subListaOrdenada = sorted(subLista)
    if busquedaElemento(listaCC, subListaOrdenada) == None:
      listaCC.append(subListaOrdenada)
      
  return len(listaCC)
  
print(countConnections(graph))

def convertToBFSTree(Grafo, v):
  for vertice in Grafo:
    vertice.color = "Blanco"
    vertice.distance = -1
    vertice.parent = None
    
  v.color = "Gris"
  v.distance = 0
  v.parent = None
  colaVertices = []
  #para simular una cola, uso append y pop(0)
  colaVertices.append(v)
  while len(colaVertices) != 0:
    #RESOLVER ESTE PROBLEMA: Yo solamente en mi conectlist tengo guardados los vertices, pero no clase graphnode donde tengo los atributos a dar.
    verticeaUsar = colaVertices.pop(0)
    for vertice in verticeaUsar.conectList:
      for verticeConexo in Grafo:
        if verticeConexo.vertex == vertice:
          break 
        
      if verticeConexo.color == "Blanco":
        verticeConexo.color = "Gris"
        verticeConexo.distance = verticeaUsar.distance + 1
        verticeConexo.parent = verticeaUsar
        colaVertices.append(verticeConexo)
    verticeaUsar.color = "Negro"

convertToBFSTree(graph, graph[0])


#Modificaciones que realice es que DFSVisit me retorna un int, que es el tiempo. 
def convertToDFSTree(Grafo, v):
  for vertice in Grafo:
    vertice.color = "Blanco"
    vertice.parent = None

  tiempo = 0
  DFSVisit(Grafo, v, tiempo)
  #En caso de que hayan quedado Vertices en blanco, CREO que es por esta razon la que hace un bucle en las siguientes lineas
  for vertice in Grafo:
    if vertice.color == "Blanco":
      DFSVisit(Grafo, vertice, tiempo)
#Funcion Recursiva      
def DFSVisit(Grafo, v, tiempo):
  tiempo += 1
  v.timeD = tiempo
  v.color = "Gris"
  for vertice in v.conectList:
    flag = False
    for vertice2 in Grafo:
      if (vertice2.vertex == vertice) and (vertice2.color == "Blanco"):
        flag = True
        break
    if vertice2.color == "Blanco" and flag == True:
      vertice2.parent = v
      tiempo = DFSVisit(Grafo, vertice2, tiempo)
  v.color = "Negro"
  tiempo += 1 
  v.timeF = tiempo
  return tiempo

convertToDFSTree(graph, graph[3])
print(graph[0].parent.parent.vertex)

def bestRoad(Grafo, v1, v2):
  #Caso base, nos aseguramos si existe un camino entre v1 y v2
  if existPath(Grafo,v1, v2) == False:
    return []

  Lista = []
  for vertice in Grafo:
    if vertice.vertex == v1:
      verticeaUsar = vertice
  #Otro caso base, donde justo en los vertices adyacentes a v1, se encuentra el v2
  if busquedaElemento(verticeaUsar.conectList, v2) != None:
    Lista.append(v1)
    Lista.append(v2)
    return Lista

  #Hago la recursividad por la cantidad de vertices que son adyacentes a v1(?
  for vertices in verticeaUsar.conectList:
    listaFinal = bestRoadR(Grafo, verticeaUsar, v2, [], Lista,[])

  #Aca de todas los caminos posibles, tomo el mas pequeño:
  menor = 100000
  for posibleCamino in listaFinal:
    if len(posibleCamino) < menor:
      menor = len(posibleCamino)
      caminoMasCorto = posibleCamino
  return caminoMasCorto
  
def bestRoadR(Grafo, verticeEnUso, v2, subLista, Lista, listaVerticesPasados):
  listaVerticesPasados.append(verticeEnUso.vertex)
  subLista.append(verticeEnUso.vertex)
  if busquedaElemento(verticeEnUso.conectList, v2) != None:
    subLista.append(v2)
    Lista.append(subLista)
    return Lista

  for numVertice in verticeEnUso.conectList:
    for verticeNodo in Grafo:
      if verticeNodo.vertex == numVertice and busquedaElemento(listaVerticesPasados, verticeNodo.vertex) == None:
        bestRoadR(Grafo, verticeNodo, v2, list(subLista), Lista, list(listaVerticesPasados))

  return Lista

print(bestRoad(graph, 5, 4))
  
  
