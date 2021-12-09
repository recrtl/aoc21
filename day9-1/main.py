import os
import functools

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))


heightmap = []
for i, line in enumerate(lines):
    heightmap.append(list(map(lambda x: int(x), line)))

for line in heightmap:
    print(line)

nbRows = len(heightmap)
nbCols = len(heightmap[0])
sum = 0
for i in range(0, nbRows):
    for j in range(0, nbCols):
        value = heightmap[i][j]
        isLowPoint = ((i == 0 or heightmap[i-1][j] > value)
                      and (i == nbRows-1 or heightmap[i+1][j] > value)
                      and (j == 0 or heightmap[i][j-1] > value)
                      and (j == nbCols-1 or heightmap[i][j+1] > value))
        if isLowPoint:
            print(f'low point {i},{j}: {value}')
            sum += value+1

print(sum)
