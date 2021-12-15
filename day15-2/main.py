import os
import functools
from typing import Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

map = []
nbRowsInput = len(lines)
nbColsInput = len(lines[0])
nbRows = nbRowsInput*5
nbCols = nbColsInput*5
map = [None] * nbRows
for y in range(0, nbRows):
    map[y] = [None] * nbCols

for y, line in enumerate(lines):
    map.append([])
    for x, char in enumerate(line):
        map[y][x] = int(char)


for i in range(1, 5):
    for x in range(nbColsInput*i, nbColsInput*(i+1)):
        for y in range(0, nbRowsInput):
            map[y][x] = (map[y][x-nbColsInput] % 9) + 1

for i in range(1, 5):
    for x in range(0, nbCols):
        for y in range(nbRowsInput*i, nbRowsInput*(i+1)):
            map[y][x] = (map[y-nbRowsInput][x] % 9)+1


def getKey(vertex):
    return str(vertex[0])+","+str(vertex[1])


def getNeighbors(vertex):
    res = []
    if vertex[0] > 0:
        res.append([vertex[0]-1, vertex[1]])
    if vertex[0] < nbCols:
        res.append([vertex[0]+1, vertex[1]])
    if vertex[1] > 0:
        res.append([vertex[0], vertex[1]-1])
    if vertex[1] < nbRows:
        res.append([vertex[0], vertex[1]+1])
    return res


def dijkstra(map, source):
    dist = {}
    prev = {}
    queue = {}
    for x in range(0, nbCols):
        for y in range(0, nbRows):
            vertex = [x, y]
            vertexKey = getKey(vertex)
            dist[vertexKey] = 9999999999
            prev[vertexKey] = None
            queue[vertexKey] = vertex
    dist[getKey(source)] = 0

    queueNotInfinity = {getKey(source): source}
    while len(queue) > 0:
        k = min(queueNotInfinity, key=(lambda v: dist[v]))
        u = queueNotInfinity.pop(k)
        queue.pop(getKey(u))

        if len(queue) % 1000 == 0:
            print(f'{len(queue)} {len(queueNotInfinity)}')

        if u == target:
            return dist, prev

        for neighbor in getNeighbors(u):
            neighborKey = getKey(neighbor)
            if neighborKey not in queue:
                continue

            alt = dist[getKey(u)] + map[neighbor[1]][neighbor[0]]
            if alt < dist[neighborKey]:
                dist[neighborKey] = alt
                prev[neighborKey] = u
                queueNotInfinity[neighborKey] = neighbor
    return dist, prev


start = [0, 0]
target = [nbCols-1, nbRows-1]

dist, prev = dijkstra(map, start)

path = []
current = target
while current != start:
    path.append(current)
    current = prev[getKey(current)]
print(list(reversed(path)))

print()
for y in range(0, nbRows):
    row = ""
    for x in range(0, nbCols):
        if [x, y] in path:
            row += '\033[1m\033[92m' + str(map[y][x]) + '\033[0m'
        else:
            row += str(map[y][x])
    print(row)

print()
print(dist[getKey(target)])
