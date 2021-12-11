import os
import functools
from typing import Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

energyLevels: list[list[int]] = []
for i, line in enumerate(lines):
    energyLevels.append(list(map(lambda x: int(x), line)))

print()
for line in energyLevels:
    print(line)

nbRows = len(energyLevels)
nbCols = len(energyLevels[0])

totalFlashes = 0
for step in range(1, 100 + 1):
    for i in range(0, nbRows):
        for j in range(0, nbCols):
            energyLevels[i][j] += 1

    while True:
        previousFlashes = totalFlashes
        for i in range(0, nbRows):
            for j in range(0, nbCols):
                if energyLevels[i][j] > 9:
                    energyLevels[i][j] = -1
                    totalFlashes += 1
                    for i2 in range(max(0, i-1), min(nbRows, i+2)):
                        for j2 in range(max(0, j-1), min(nbCols, j+2)):
                            # ignore those who already flashed during this step
                            if energyLevels[i2][j2] >= 0:
                                energyLevels[i2][j2] += 1
        if totalFlashes == previousFlashes:
            break

    for i in range(0, nbRows):
        for j in range(0, nbCols):
            if energyLevels[i][j] < 0:
                energyLevels[i][j] = 0

    print()
    for line in energyLevels:
        print(line)

print(totalFlashes)
