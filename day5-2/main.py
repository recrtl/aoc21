import os
from typing import NamedTuple

print('day5-1')

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    inputs = [line.rstrip("\n") for line in f]


class Line:
    def __init__(self, start, end):
        self.start: Point = start
        self.end: Point = end

    def __repr__(self):
        return f'{self.start.x},{self.start.y} -> {self.end.x},{self.end.y}'


class Point:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


maxPoint = Point(0, 0)
lines: list[Line] = []
for input in inputs:
    splits = input.split(" -> ")
    startValues = splits[0].split(",")
    endValues = splits[1].split(",")
    start = Point(int(startValues[0]), int(startValues[1]))
    end = Point(int(endValues[0]), int(endValues[1]))
    lines.append(Line(start, end))

    maxPoint.x = max(maxPoint.x, start.x, end.x)
    maxPoint.y = max(maxPoint.y, start.y, end.y)

for line in lines:
    print(line)

matrix = [[0 for i in range(0, maxPoint.x+1)] for j in range(0, maxPoint.y+1)]

for line in lines:
    current = line.start
    matrix[current.y][current.x] += 1
    while current != line.end:
        current.x += 1 if current.x < line.end.x else -1 if current.x > line.end.x else 0
        current.y += 1 if current.y < line.end.y else -1 if current.y > line.end.y else 0
        matrix[current.y][current.x] += 1

for line in matrix:
    print(line)

count = 0
for line in matrix:
    for value in line:
        if value > 1:
            count += 1
print(count)
