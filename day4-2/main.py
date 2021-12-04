import os

print('day4-2')

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]


def toInt(x): return int(x)


firstLine = lines[0].split(",")
draws = list(map(toInt, firstLine))
print(f'draws: {draws}')


class BingoNumber:
    def __init__(self, value):
        self.value: int = value
        self.marked: bool = False

    def __repr__(self):
        return f'{ "x" if self.marked else "" }{self.value}'


def toBingoNumber(x): return BingoNumber(int(x))


grids = []
for lineNb in range(2, len(lines), 6):
    grid = [[] for i in range(0, 5)]
    for i in range(0, 5):
        splits = lines[lineNb+i].split()
        intSplits = list(map(toBingoNumber, splits))
        grid[i] = intSplits
    grids.append(grid)

for i, grid in enumerate(grids):
    print(f'grid #{i}: {grid}')


def isWinner(grid):
    for i in range(0, 5):
        line = list(map(lambda x: grid[i][x], range(0, 5)))
        if len(list(filter(lambda x: x.marked, line))) == 5:
            return True
        column = list(map(lambda x: grid[x][i], range(0, 5)))
        if len(list(filter(lambda x: x.marked, column))) == 5:
            return True


lastDraw = None
for draw in draws:
    for grid in grids:
        for line in grid:
            for nb in line:
                if nb.value == draw:
                    nb.marked = True

    if len(grids) == 1 and isWinner(grids[0]):
        lastDraw = draw
        break
    else:
        grids = list(filter(lambda grid: not isWinner(grid), grids))

loser = grids[0]
print(f'lastDraw: {lastDraw}')
print(f'loser: {loser}')

sum = 0
for line in loser:
    for nb in line:
        if not nb.marked:
            sum += nb.value
print(f'sum: {sum}')
print(f'product: {sum * lastDraw}')
