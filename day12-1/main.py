import os
import functools
from typing import Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

edgesByVertice = {}
for line in lines:
    vertices = line.split("-")
    start = vertices[0]
    end = vertices[1]
    if start in edgesByVertice:
        edgesByVertice[start].append(end)
    else:
        edgesByVertice[start] = [end]

    if end in edgesByVertice:
        edgesByVertice[end].append(start)
    else:
        edgesByVertice[end] = [start]

print(edgesByVertice)


def visit(current: str, currentPath: list[str]) -> list[list[str]]:
    if current == "end":
        return [currentPath]
    res = []
    for next in edgesByVertice[current]:
        if next.islower():
            if next in currentPath:
                continue
        newPath = currentPath.copy()
        newPath.append(next)
        newPathes = visit(next, newPath)
        res += newPathes
    return res


pathes = visit("start", ["start"])
print()
for path in pathes:
    print(path)

print()
print(len(pathes))
