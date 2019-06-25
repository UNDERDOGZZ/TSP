#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv

def read(fileName):
    array = []
    with open(fileName) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        idElem = -1
        for row in file:
            if idElem != -1:
                elem = {}
                elem["name"] = row[5]
                elem["x"] = float(row[15])
                elem["y"] = float(row[16])
                array.append(elem)
            
            idElem += 1
        
    return array
                
                


# In[ ]:


def readCPxDto(fileName):
    dictionary = {}
    places = []
    with open(fileName) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        idElem = -1
        for row in file:
            if idElem != -1:
                elem = {}
                elem["name"] = row[5]
                elem["x"] = float(row[15])
                elem["y"] = float(row[16])
                if row[1] not in dictionary:
                    dictionary[row[1]] = []
                    dictionary[row[1]].append(elem)
                    places.append(row[1])
                else:
                    dictionary[row[1]].append(elem)
                del elem
            
            idElem += 1
        
    return dictionary, places


# In[ ]:


def calculateDistances(dictionary, department):
    
    distance_matrix = []
    row = []
    n = len(dictionary[department])
    for fil in range(n):
        for col in range(n):
            if fil == col:
                row.append(0)
            else:
                operation = ((dictionary[department][col]["x"]) - (dictionary[department][fil]["x"]))**2 + ((dictionary[department][col]["y"] - dictionary[department][fil]["y"]))**2
                distance = operation**0.5
                row.append(distance)
        distance_matrix.append(row)
        row = []
    return distance_matrix


# In[ ]:


def calculateDistancesDictionary(dictionary, departments):
    
    n = len(departments)
    distance_dictionary = {}

    for pos in range(n):
        dep = departments[pos]
        distance_dictionary[dep] = calculateDistances(dictionary, dep)

    return distance_dictionary




# In[ ]:


placesDictionary, places = readCPxDto('test.csv')
distancesDictionary = calculateDistancesDictionary(placesDictionary, places)


# In[ ]:


print(distancesDictionary)


# In[ ]:


print(placesDictionary)


# In[1]:


import csv
import math
import heapq as hq
def readFile(filename):
    dictionary = {}
    with open(filename,encoding='utf-8-sig') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        contador=1
        for row in file:
                elem = {}
                elem["id"]=row[0]
                elem["name"] = row[1]
                elem["x"] = float(row[2])
                elem["y"] = float(row[3])
                dictionary[contador] = elem
                contador+=1
                del elem
    return dictionary



# In[2]:


def calculateDistance(x1,y1,x2,y2):        
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)
    


# In[3]:


def prim(distancia,nombre):
    n = len(distancia)
    dist = [math.inf]*n
    path = [None]*n
    visited = [False]*n
    q = []
    hq.heappush(q, (0, 0))
    contador=0
    while len(q) > 0:
        #print(contador)
        contador+=1
        _, u = hq.heappop(q)
        if not visited[u]:
            visited[u] = True
            for v, w in distancia[u]:
                if not visited[v] and w < dist[v] and w!=0 :
                    dist[v] = w
                    path[v] = nombre[v][u]
                    hq.heappush(q, (w, v))
    print(path)


# In[6]:


def makingDictonarys(filename):
    dictionary = readFile(filename)
    distancia=[]
    nombre=[]
    for i in range(1,len(dictionary)+1):
        aux=[]
        aux2=[]
        for j in range(1,len(dictionary)+1):
            aux.append((int(dictionary[j]["id"]),calculateDistance(float(dictionary[i]["x"]),float(dictionary[i]["y"]), float(dictionary[j]["x"]),float(dictionary[j]["y"]))))
            aux2.append(dictionary[j]["name"])
            #aux.append((j,calculateDistance(float(dictionary[i]["x"]),float(dictionary[i]["y"]), float(dictionary[j]["x"]),float(dictionary[j]["y"]))))
        distancia.append(aux)
        nombre.append(aux2)
        del aux
        del aux2
    print(distancia)
    #prim(distancia,nombre)


# In[7]:


makingDictonarys('cincuenta.csv')


# In[ ]:


print(placesDictionary['AYACUCHO'])


# In[ ]:


print(distancesDictionary['AYACUCHO'])


# In[ ]:


def prim1(placesD, distancesD, places):
    cont=len(distancesD)
    for i in range(cont):
        n = len(placesD[places[i]])
        visited = [False]*n
        dist = [math.inf]*n
        path = [None]*n
        q = []
        hq.heappush(q, (0, 0))
        while len(q) > 0:
            _, u = hq.heappop(q)
            if not visited[u]:
                visited[u] = True
                for v, w in distancesD[places[i]][u]:
                    if not visited[v] and w < dist[v] and w!=0 :
                        dist[v] = w
                        path[v].append(places[v][u])
                        hq.heappush(q, (w, v))
    print(path)


# In[ ]:


prim1(placesDictionary, distancesDictionary, places)


# In[ ]:


print(distancesDictionary['AYACUCHO'][1])


# In[ ]:




