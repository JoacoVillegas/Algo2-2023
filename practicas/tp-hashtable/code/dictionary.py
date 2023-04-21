from math import *
from algo1 import *
import linkedlist


class DictionaryNode:
  key = None
  value = None


class Dictionary:
  head = None


# def insert(D, key, value):
#   slot = key % 9
#   if D[slot] == None:
#     aList = linkedlist.LinkedList()
#     D[slot] = aList
#     dicNode = DictionaryNode()
#     dicNode.key = key
#     dicNode.value = value
#     linkedlist.add(aList, dicNode)
#   else:
#     slotList = D[slot]
#     dicNode = DictionaryNode()
#     dicNode.key = key
#     dicNode.value = value
#     linkedlist.add(slotList, dicNode)
#   return D

# def search(D, key):
#   slot = key % 9
#   if D[slot] == None:
#     return None
#   else:
#     currentNode = D[slot].head
#     while currentNode != None:
#       if currentNode.value.key == key:
#         return currentNode.value.value
#       currentNode = currentNode.nextNode
#     return None

# def delete(D, key):
#   slot = key % 9
#   if D[slot] == None:
#     return None
#   else:
#     currentNode = D[slot].head

#     while currentNode != None:
#       if currentNode.value.key == key:
#         linkedlist.delete(D[slot], currentNode.value)
#         if linkedlist.length(D[slot]) == 0:
#           D[slot] = None
#         return D
#       currentNode = currentNode.nextNode


def insert(D, key, value):
  slot = key % len(D)
  if D[slot] == None:
    aList = linkedlist.LinkedList()
    D[slot] = aList
    dicNode = DictionaryNode()
    dicNode.key = key
    dicNode.value = value
    linkedlist.add(aList, dicNode)
  else:
    slotList = D[slot]
    dicNode = DictionaryNode()
    dicNode.key = key
    dicNode.value = value
    linkedlist.add(slotList, dicNode)
  return D


def search(D, key):
  slot = key % len(D)
  if D[slot] == None:
    return None
  else:
    currentNode = D[slot].head
    while currentNode != None:
      if currentNode.value.key == key:
        return currentNode.value.value
      currentNode = currentNode.nextNode
    return None


def delete(D, key):
  slot = key % 9
  if D[slot] == None:
    return None
  else:
    currentNode = D[slot].head

    while currentNode != None:
      if currentNode.value.key == key:
        linkedlist.delete(D[slot], currentNode.value)
        if linkedlist.length(D[slot]) == 0:
          D[slot] = None
        return D
      currentNode = currentNode.nextNode


#FALTA MEJORAR, HAY ERRORES.
def checkPermutation(S, P):
  myHash = []

  if len(S) != len(P):
    return False

  for i in range(0, len(S)):
    myHash[i] = None

  for i in range(0, len(S)):
    insert(myHash, ord(S[i]), S[i])

  for i in range(0, len(P)):
    if search(myHash, P[i]) == None:
      return False

  return True


def areUniqueElements(L):
  myHash = []
  for i in range(0, linkedlist.length(L)):
    myHash.append(None)
  currentNode = L.head
  for i in range(0, linkedlist.length(L)):
    if search(myHash, currentNode.value) != None:
      return False
    insert(myHash, currentNode.value, currentNode.value)
    currentNode = currentNode.nextNode
  return True


#REVISAR
def checkInside(S, P):
  myHash = []
  for i in range(0, 149):
    myHash.append(None)

  lengthWords = len(P)
  i = 0
  while i + lengthWords <= len(P):
    #Tomar letras de a 4 en la palabra mas larga
    #uso k y j para lo que seria formar mi key, i es con quien recorro toda la palabra.
    k = i
    subString = S[i:i + lengthWords]
    j = lengthWords - 1
    aKey = 0
    while j != -1:
      aKey = (ord(subString[k]) * (10**j)) + aKey
      k += 1
      j -= 1
    insert(myHash, aKey, i)
    i += 1

  #Al terminar con todas las palabras que podia conformar con la mas larga, busco la palabra pequeña
  aKeyAux = 0
  j = lengthWords - 1
  l = 0
  while j != -1:
    aKeyAux = (ord(P[l]) * (10**j)) + aKeyAux
    l += 1
    j -= 1
  return search(myHash, aKeyAux)
