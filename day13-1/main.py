import os
import functools
from typing import Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

dots = []
maxX = 0
maxY = 0
for line in lines:
    if line == "":
        break
    splits = line.split(",")
    x = int(splits[0])
    y = int(splits[1])
    maxX = max(maxX, x)
    maxY = max(maxY, y)
    dots.append([x, y])

# yFold = 7
# for dot in dots:
#     if dot[1] > yFold:
#         dot[1] = yFold - (dot[1] - yFold)

xFold = 655
for dot in dots:
    if dot[0] > xFold:
        dot[0] = xFold - (dot[0] - xFold)

uniqueDots = []
for dot in dots:
    if dot not in uniqueDots:
        uniqueDots.append(dot)

print(uniqueDots)
print(len(uniqueDots))
