#!/usr/bin/env python
# coding: utf-8

# In[ ]:


conda install gdal -c conda-forge


# In[ ]:



import matplotlib.pyplot as plt
import matplotlib.cm
import pandas as pd
import numpy as np
import seaborn as sns

from matplotlib.colors import Normalize
import matplotlib.colors as colors
from numpy import array
from numpy import max

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


# In[3]:


plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
m.bluemarble(scale=0.5);


# In[10]:


conda install basemap-data-hires


# In[83]:


fig = plt.figure(figsize=(15, 15))
m = Basemap(projection='mill', resolution='h', 
            lat_0=-9.1899672, lon_0=-75.015152,llcrnrlat = -18.384377,
            llcrnrlon = -84.342834,
            urcrnrlat = 0.936457,
            urcrnrlon = -68.225205)
m.etopo(scale=4, alpha=0.6)

# Map (long, lat) to (x, y) for plotting
x, y = m(-72.531266212, -13.992029757)

#plt.plot(x, y, 'ok', markersize=1)
m.drawcoastlines(linewidth=2)
m.drawcountries(linewidth=2)
#plt.text(x, y, ' Seattle', fontsize=9);

pD, pla, c = readCPxDto('test1008.csv')
for i in range(len(pla)):
    d = pla[i]
    for j in range(len(c[d])):
        x, y = m(pD[d][j]['x'], pD[d][j]['y'])
        plt.plot(x, y,'ok',markersize=1,color='purple')
        plt.text(x, y, pD[d][j]['name'], fontsize=7)
        del x
        del y


# In[43]:


import heapq as hq
import math
import csv

def readCPxDto(fileName):
    dictionary = {}
    cp = {}
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
                    cp[row[1]] = []
                    cp[row[1]].append(elem['name'])
                    places.append(row[1])
                else:
                    dictionary[row[1]].append(elem)
                    cp[row[1]].append(elem['name'])
                del elem
            
            idElem += 1
        
    return dictionary, places, cp


# In[44]:


def calculateDistance(x1,y1,x2,y2):        
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)


# In[85]:



def prim(distancia,nombre, dptos):
    pathDic = {}
    for a in range(len(dptos)):
        dpto = dptos[a]
        pathDic[dpto]=[]
        n = len(distancia[dpto])
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
                for v, w in distancia[dpto][u]:
                    if not visited[v] and w < dist[v] and w!=0 :
                        dist[v] = w
                        path[v] = nombre[dpto][v][u]
                        hq.heappush(q, (w, v))
        for i in range(len(path)):
            if nombre[dpto][v][i] not in path:
                path[0]=nombre[dpto][v][i]
        pathDic[dpto]=path
    print(pathDic)
    fig = plt.figure(figsize=(15, 15))
    m = Basemap(projection='mill', resolution='h', 
                lat_0=-9.1899672, lon_0=-75.015152,llcrnrlat = -18.384377,
                llcrnrlon = -84.342834,
                urcrnrlat = 0.936457,
                urcrnrlon = -68.225205)
    m.etopo(scale=4, alpha=0.6)

    # Map (long, lat) to (x, y) for plotting
    x, y = m(-72.531266212, -13.992029757)

    #plt.plot(x, y, 'ok', markersize=1)
    m.drawcoastlines(linewidth=2)
    m.drawcountries(linewidth=2)
    #plt.text(x, y, ' Seattle', fontsize=9);
    xs=[]
    ys=[]
    pD, pla, c = readCPxDto('test1008.csv')
    for i in range(len(pathDic)):
        d = pla[i]
        for j in range(len(pathDic[d])):
            x, y = m(pD[d][j]['x'], pD[d][j]['y'])
            xs.append(x)
            ys.append(y)
            plt.plot(x, y,'ok',markersize=1,color='purple')
            plt.text(x, y, pD[d][j]['name'], fontsize=7)
            del x
            del y
    m.plot(xs, ys, color='r', linewidth=3, label='Flight 98')
    


# In[89]:


def distPrimMap(filename):
    placesDictionary, places, cp = readCPxDto(filename)
    #print (placesDictionary['JUNIN'])
    dis = {}
    abc = {}
    for a in range(len(places)):
        dpto = places[a]
        dis[dpto] = []
        abc[dpto] = []
        for b in range (len(cp[dpto])):
            aux = []
            aux2 = []
            for c in range (len(cp[dpto])):
                aux.append((int(c), calculateDistance(float(placesDictionary[dpto][b]["x"]),float(placesDictionary[dpto][b]["y"]), float(placesDictionary[dpto][c]["x"]),float(placesDictionary[dpto][c]["y"]))))
                aux2.append(placesDictionary[dpto][c]["name"])
            dis[dpto].append(aux)
            abc[dpto].append(aux2)
            del aux
            del aux2
    #print(abc['AYACUCHO'])
    prim(dis, abc, places)
    


# In[90]:


distPrimMap('test1008.csv')


# In[ ]:




