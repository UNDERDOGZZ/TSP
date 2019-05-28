import csv
import copy
import random as r

def readFile(filename, numCapital):
    dictionary = {}
    with open(filename, encoding='utf-8-sig') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        contador=-1
        for row in file:
                if contador > -1:
                        if int(row[7]) == numCapital:
                                elem = {}
                                elem["id"]=row[0]
                                elem["departamento"] = row[1]
                                elem["provincia"] = row[2]
                                elem["distrito"] = row[3]
                                elem["codigo"] = row[4]
                                elem["capital"] = int(row[7])
                                elem["x"] = float(row[15])
                                elem["y"] = float(row[16])
                                dictionary[contador] = elem
                                contador+=1
                                del elem
                else:
                        contador+=1
    print(dictionary)

readFile("CP_P_20180726.csv", 1)
