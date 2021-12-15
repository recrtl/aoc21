import os
import functools
from typing import Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

map = []
nbRows = len(lines)
nbCols = len(lines[0])
for y, line in enumerate(lines):
    map.append([])
    for char in line:
        map[y].append(int(char))


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
    queue = []
    for x in range(0, nbCols):
        for y in range(0, nbRows):
            vertex = [x, y]
            dist[getKey(vertex)] = 9999999999
            prev[getKey(vertex)] = None
            queue.append(vertex)
    dist[getKey(source)] = 0

    queueNotInfinity = {getKey(source): source}
    while len(queue) > 0:
        if len(queueNotInfinity) > 0:
            k = min(queueNotInfinity, key=(lambda v: dist[v]))
            u = queueNotInfinity.pop(k)
        else:
            u = queue[0]
        queue.remove(u)

        print(len(queue))

        if u == target:
            return dist, prev

        for neighbor in getNeighbors(u):
            if neighbor not in queue:
                continue

            alt = dist[getKey(u)] + map[neighbor[1]][neighbor[0]]
            neighborKey = getKey(neighbor)
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
