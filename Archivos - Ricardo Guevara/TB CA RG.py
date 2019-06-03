#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
                
                


# In[2]:


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


# In[3]:


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


# In[4]:


def calculateDistancesDictionary(dictionary, departments):
    
    n = len(departments)
    distance_dictionary = {}

    for pos in range(n):
        dep = departments[pos]
        distance_dictionary[dep] = calculateDistances(dictionary, dep)

    return distance_dictionary




# In[8]:


placesDictionary, places = readCPxDto('test.csv')
distancesDictionary = calculateDistancesDictionary(palcesDictionary, places)


# In[6]:


print(distancesDictionary)


# In[9]:


print(placesDictionary)


# In[ ]:




