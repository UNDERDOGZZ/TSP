import csv
import copy
import random as r
import heapq as hq

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
    return dictionary

def calcularDistancia(x,y,x2,y2):
        dx = x - x2
        dx2 = dx*dx
        dy = y - y2
        dy2 = dy*dy
        distancia = (dx2+dy2)**0.5
        return distancia

def convertirAGrafito(dic):
        arr = []
        n = len(dic)
        for i in dic:
                arr.append([])
        for i in range(1,n):
                for j in range(1,n):
                        if not i == j:
                                distancia = calcularDistancia(dic[i]["x"], dic[i]["y"],dic[j]["x"], dic[j]["y"])
                                arr[i].append((j,distancia))
        return arr

def find(s, a):
    if s[a] < 0:
        return a
    else:
        granpa = find(s, s[a])
        s[a] = granpa
        return granpa

def union(s, a, b):
    pa = find(s, a)
    pb = find(s, b)
    if pa == pb: return
    
    if s[pa] <= s[pb]:
        s[pa] += s[pb]
        s[pb] = pa
    elif s[pb] < s[pa]:
        s[pb] += s[pa]
        s[pa] = pb

def kruskal(G):
        total = 0
        il = makeIL(G)
        q = []
        n = len(G)
        for edge in il:
                hq.heappush(q, edge)
                roots = [-1]*n
                T = []
        while len(q) > 0:
                w, u, v = hq.heappop(q)
                if find(roots, u) != find(roots, v):
                        union(roots, u, v)
                        T.append((u, v, w))
                        total = total + w
        return roots, T,total,n

def makeIL(G):
    il = []
    n = len(G)
    for u in range(n):
        for v, w in G[u]:
            il.append((w, u, v))
    return il

def hallarDosMinimo(dic):
        arr = []
        n = len(dic)
        for i in range(1):
                for j in range(n):
                        if not i == j:
                                distancia = calcularDistancia(dic[i]["x"], dic[i]["y"],dic[j]["x"], dic[j]["y"])
                                arr.append((j,distancia))
        min = arr[0][1]

        for i in range(n-1):
                if min > arr[i][1]:
                        min = arr[i][1]
        
        min2 = arr[0][1]

        for i in range(n-1):
                        if min2 > arr[i][1] and min != arr[i][1]:
                                min2 = arr[i][1]

        return min, min2

print("¿A que tipo de capital quiere hallar el lowerbound? (1 = Departamental, 2 = Provincial, 3 = Distrital): ", end="")
num = input()
roots, T, total, n = kruskal(convertirAGrafito(readFile("CP_P_20180726.csv", int(num))))
min, min2 = hallarDosMinimo(readFile("CP_P_20180726.csv", int(num)))
total = total + min + min2
print(f"Numero de captiales: {n}")
print(f"Lowerbound: {total}")