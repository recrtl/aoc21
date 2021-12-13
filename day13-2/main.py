import os
import functools
from typing import Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

dots = []
folds = []
readingDots = True
for line in lines:
    if line == "":
        readingDots = False
        continue

    if readingDots:
        splits = line.split(",")
        x = int(splits[0])
        y = int(splits[1])
        dots.append([x, y])
    else:
        folds.append(line.split()[2].split("="))

for fold in folds:
    foldValue = int(fold[1])
    if fold[0] == "x":
        for dot in dots:
            if dot[0] > foldValue:
                dot[0] = foldValue - (dot[0] - foldValue)
    else:
        for dot in dots:
            if dot[1] > foldValue:
                dot[1] = foldValue - (dot[1] - foldValue)

uniqueDots = []
for dot in dots:
    if dot not in uniqueDots:
        uniqueDots.append(dot)

print(uniqueDots)
print(len(uniqueDots))

maxX = 0
maxY = 0
for dot in uniqueDots:
    maxX = max(maxX, dot[0])
    maxY = max(maxY, dot[1])

for y in range(0, maxY+1):
    str = ""
    for x in range(0, maxX+1):
        if [x, y] in uniqueDots:
            str += "#"
        else:
            str += "."
    print(str)
