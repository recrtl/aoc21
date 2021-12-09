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


def findNeighbours(i, j):
    res = []
    if i > 0:
        res.append([i-1, j])
    if i < nbRows-1:
        res.append([i+1, j])
    if j > 0:
        res.append([i, j-1])
    if j < nbCols-1:
        res.append([i, j+1])
    return res


lowPoints = []
for i in range(0, nbRows):
    for j in range(0, nbCols):
        value = heightmap[i][j]
        neighbours = findNeighbours(i, j)
        isLowPoint = all(heightmap[n[0]][n[1]] > value for n in neighbours)
        if isLowPoint:
            print(f'low point {i},{j}: {value}')
            lowPoints.append([i, j])

basins = []
for lowPoint in lowPoints:
    basin = [lowPoint]
    basinSum = 0
    for point in basin:
        i = point[0]
        j = point[1]
        value = heightmap[i][j]
        basinSum += value
        for neighbour in findNeighbours(i, j):
            if neighbour in basin:
                continue
            ni, nj = neighbour[0], neighbour[1]
            nValue = heightmap[ni][nj]
            if nValue > value and nValue < 9:
                basin.append(neighbour)
    print(basin)
    basins.append([len(basin), basinSum])

basins = sorted(basins, key=lambda x: x[1], reverse=True)
print(f'sorted basins: {basins}')
print(f'res: {basins[0][0] * basins[1][0] * basins[2][0]}')
