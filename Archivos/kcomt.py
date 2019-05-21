import csv
import copy
import random as r

def readFile(filename):
    dictionary = {}

    with open(filename, encoding='utf-8-sig') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        contador=0
        for row in file:
                elem = {}
                elem["id"]=row[0]
                elem["departamento"] = row[1]
                elem["provincia"] = row[2]
                elem["distrito"] = row[3]
                elem["codigo"] = row[4]
                elem["x"] = float(row[15])
                elem["y"] = float(row[16])
                dictionary[contador] = elem
                contador+=1
                del elem
    print(dictionary)

readFile("CPPRUEBA.csv")