class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

def rotateLeft(Tree, avlnode):
    if Tree.root == avlnode:
        newRoot = avlnode.rightnode
        leftSon = newRoot.leftnode
        newRoot.parent = None
        avlnode.rightnode = None
        avlnode.parent = newRoot
        Tree.root = newRoot
        newRoot.leftnode = avlnode
        avlnode.rightnode = leftSon
        if leftSon != None:
          leftSon.parent = avlnode
    else:
        newRoot = avlnode.rightnode
        leftSon = newRoot.leftnode
        newRoot.parent = avlnode.parent
        if avlnode.parent.leftnode == avlnode:
            avlnode.parent.leftnode = newRoot
        else:
            avlnode.parent.rightnode = newRoot
        avlnode.parent = newRoot
        avlnode.rightnode = leftSon
        newRoot.leftnode = avlnode 
        if leftSon != None:
            leftSon.parent = avlnode
    return newRoot

def rotateRight(Tree, avlnode):
    if Tree.root == avlnode:
        newRoot = avlnode.leftnode
        rightSon = newRoot.rightnode
        newRoot.parent = None
        Tree.root = newRoot
        avlnode.parent = newRoot
        newRoot.rightnode = avlnode
        avlnode.leftnode = rightSon
        if rightSon != None:
            rightSon.parent = avlnode
    else:
        newRoot = avlnode.leftnode
        rightSon = newRoot.rightnode
        newRoot.parent = avlnode.parent
        if avlnode.parent.leftnode == avlnode:
            avlnode.parent.leftnode = newRoot
        else:
            avlnode.parent.rightnode = newRoot
        avlnode.parent = newRoot
        avlnode.leftnode = rightSon
        newRoot.rightnode = avlnode
        if rightSon != None:
            rightSon.parent = avlnode
    return newRoot

def calculateBalance(AVLTree):
    return calculateBalanceR(AVLTree, AVLTree.root)

def heightTree(currentNode):
  if currentNode == None:
    return 0 

  hLeft = heightTree(currentNode.leftnode)
  hRight = heightTree(currentNode.rightnode)

  if hLeft >= hRight:
    hTree = hLeft + 1
  else:
    hTree = hRight + 1

  return hTree

def calculateBalanceR(AVLTree, currentNode):
  bfValue = heightTree(currentNode.leftnode) - heightTree(currentNode.rightnode)
  currentNode.bf = bfValue
  
  if currentNode.leftnode != None:
    calculateBalanceR(AVLTree, currentNode.leftnode)
  if currentNode.rightnode != None:
    calculateBalanceR(AVLTree, currentNode.rightnode)

  if AVLTree.root == currentNode:
    return AVLTree
  

def reBalance(AVLTree, currentNode):
   if currentNode.bf < 0:
      if currentNode.rightnode.bf > 0:
         rotateRight(AVLTree, currentNode.rightnode)
         rotateLeft(AVLTree, currentNode)
      else:
         rotateLeft(AVLTree, currentNode)
   elif currentNode.bf > 0:
      if currentNode.leftnode.bf < 0:
         rotateLeft(AVLTree, currentNode.leftnode)
         rotateRight(AVLTree, currentNode)
      else:
         rotateRight(AVLTree, currentNode)
   calculateBalance(AVLTree)
   return AVLTree
# def reBalance(AVLTree):
#    calculateBalance(AVLTree)
   
#    while searchDesbalance(AVLTree, AVLTree.root) == False:
#       searchDesbalance(AVLTree, AVLTree.root)

def update_bf(AVLTree, currentNode):
   auxNode = currentNode
   while auxNode != None:
      bfValue = heightTree(auxNode.leftnode) - heightTree(auxNode.rightnode)
      auxNode.bf = bfValue
      # print("/////")
      # print(auxNode.key)
      # print(auxNode.bf)
      # print("/////")
      auxNode = auxNode.parent
    
   while currentNode != None:
      if currentNode.bf > 1 or currentNode.bf < -1:
         
         reBalance(AVLTree, currentNode)
      currentNode = currentNode.parent
   return
#///////////////////////////////////////////////////
def crearNodo(element, key, currentNode):
  nodoAInsertar = AVLNode()
  nodoAInsertar.key = key
  nodoAInsertar.value = element
  nodoAInsertar.parent = currentNode
  return nodoAInsertar

def buscarPosicion(B, element, key, currentNode):
  if key == currentNode.key:
    return None

  if key > currentNode.key:
    if currentNode.rightnode != None:
      nodoInsert = buscarPosicion(B, element, key, currentNode.rightnode)
    else:
      nodoInsert = crearNodo(element, key, currentNode)
      currentNode.rightnode = nodoInsert
  else:
    if currentNode.leftnode != None:
      nodoInsert = buscarPosicion(B, element, key, currentNode.leftnode)
    else:
      nodoInsert = crearNodo(element, key, currentNode)
      currentNode.leftnode = nodoInsert

  return nodoInsert
      

def insert(B, element, key):
  if B.root == None:
    nodoRaiz = AVLNode()
    nodoRaiz.key = key
    nodoRaiz.value = element
    nodoRaiz.parent = None
    nodoRaiz.bf = 0
    B.root = nodoRaiz
    return nodoRaiz.key
  else:
    nodo = buscarPosicion(B, element, key, B.root)
    update_bf(B, nodo)
    return  nodo.key
#////////////////////////////////////////////////////////  
def DeleteElement(currentNode):
  #Primera situacion: el nodo a eliminar es una hoja.
  if currentNode.rightnode == None and currentNode.leftnode == None:
    if currentNode.parent.leftnode == currentNode:
      currentNode.parent.leftnode = None
    else:
      currentNode.parent.rightnode = None
    currentNode.parent = None
    return currentNode.key

  #Tercera Situacion: el nodo a eliminar tiene dos hijos.
  if currentNode.rightnode != None and currentNode.leftnode != None:
    #Buscamos el mayor elemento de los menores SI ES QUE TIENE, En el caso contrario, deberemos buscar el menor elemento de los mayores.
    nodeAux = currentNode.leftnode
  
    while nodeAux.rightnode != None:
      nodeAux = nodeAux.rightnode
    valueAux = nodeAux.value
    keyAux = nodeAux.key
    keyEliminada = currentNode.key
    DeleteElement(nodeAux)
    currentNode.value = valueAux
    currentNode.key = keyAux
    return keyEliminada

  #Segunda Situacion: el nodo a eliminar tiene un hijo.
  #¿Debo decir que su parent sea None?
  if currentNode.rightnode == None and currentNode.leftnode != None:
    if currentNode.parent.leftnode == currentNode:
      currentNode.leftnode.parent = currentNode.parent
      currentNode.parent.leftnode = currentNode.leftnode
    else:
      currentNode.leftnode.parent = currentNode.parent
      currentNode.parent.rightnode = currentNode.leftnode
    currentNode.parent = None
    return currentNode.key
  else:
    if currentNode.rightnode != None and currentNode.leftnode == None:
      if currentNode.parent.leftnode == currentNode:
        currentNode.rightnode.parent = currentNode.parent
        currentNode.parent.leftnode = currentNode.rightnode
      else:
        currentNode.rightnode.parent = currentNode.parent
        currentNode.parent.rightnode = currentNode.rightnode
    currentNode.parent = None
    return currentNode.key
  

def busquedaDeleteKey(B, key, currentNode):
  keyEliminated = None
  if currentNode.key == key:
    keyEliminated = DeleteElement(currentNode)
  else:
    if currentNode.leftnode != None and keyEliminated == None:
      keyEliminated = busquedaDeleteKey(B, key, currentNode.leftnode)
    if currentNode.rightnode != None and keyEliminated == None:
      keyEliminated = busquedaDeleteKey(B, key, currentNode.rightnode)

  if keyEliminated != None:
    return keyEliminated
  else:
    return None

def deleteKey(B, key):
  if B.root == None:
    return None
  else:
    keyEliminated = busquedaDeleteKey(B, key, B.root)
    
    calculateBalance(B)
    while searchDesbalance(B, B.root) == False:
       searchDesbalance(B, B.root)

def searchDesbalance(AVLTree, currentNode):
   boolDesbalance = True
   if currentNode.bf > 1 or currentNode.bf < -1:
      reBalance(AVLTree, currentNode)
      boolDesbalance = False
   else:
      if currentNode.leftnode != None:
         searchDesbalance(AVLTree, currentNode.leftnode)
      if currentNode.rightnode != None:
         searchDesbalance(AVLTree, currentNode.rightnode)  
   return boolDesbalance