import os
import math
from collections import namedtuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))


Point = namedtuple('Point', 'x y z')

inputs: list[list[Point]] = []
i = 0
while i < len(lines) and True:
    scannerPoints = []
    i += 1  # skip header
    while i < len(lines) and lines[i] != "":
        splits = lines[i].split(",")
        scannerPoints.append(
            Point(int(splits[0]), int(splits[1]), int(splits[2])))
        i += 1
    i += 1  # skip blank line
    inputs.append(scannerPoints)

# for scannerPoints in inputs:
#     print(len(scannerPoints))
#     print(scannerPoints)


def rotatePoints(i: int, points: list[Point]) -> list[Point]:
    newPoints = []
    for p in points:
        newPoints.append(rotatePoint(i, p))
    return newPoints


def rotatePoint(i: int, p: Point) -> Point:
    if i == 0:
        p = Point(p.x, p.y, p.z)  # ensure copy

    mod4 = i % 4
    if mod4 == 1:
        p = Point(-p.x, -p.y, p.z)
    elif mod4 == 2:
        p = Point(p.x, -p.y, -p.z)
    elif mod4 == 3:
        p = Point(-p.x, p.y, -p.z)

    mod3 = int(i/4) % 3
    if mod3 == 1:
        p = Point(p.z, p.x, p.y)
    elif mod3 == 2:
        p = Point(p.y, p.z, p.x)

    if i > 11:
        p = Point(-p.x, p.z, p.y)

    return p


def offsetPoints(points: list[Point], offset: Point) -> list[Point]:
    newPoints = []
    for p in points:
        newPoints.append(addPoints(p, offset))
    return newPoints


def addPoints(p1: Point, p2: Point) -> Point:
    return Point(p1.x + p2.x, p1.y + p2.y, p1.z + p2.z)


def subPoints(p1: Point, p2: Point) -> Point:
    return Point(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z)


def getVector(p1: Point, p2: Point) -> Point:
    return Point(p1.x-p2.x, p1.y-p2.y, p1.z-p2.z)


def getVectors(points=list[Point]) -> list[Point]:
    vecs = []
    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            vecs.append(getVector(points[i], points[j]))
    return vecs


def revertPoint(p: Point) -> Point:
    return Point(-p.x, -p.y, -p.z)


def getEdgesIntersection(list1, list2):
    return [value for value in list1 if value in list2 or revertPoint(value) in list2]


def getPointsIntersection(list1, list2):
    return [value for value in list1 if value in list2]


def getNbEdges(nbVertex: int):
    return int(nbVertex * (nbVertex - 1) / 2)


def getHash(p: Point) -> str:
    return f'{p.x},{p.y},{p.z}'


rotations = {0: 0}
offsets = {0: Point(0, 0, 0)}
refQueues = [0]
for refIndex in refQueues:
    refPoints = rotatePoints(rotations[refIndex], inputs[refIndex])
    refPoints = offsetPoints(refPoints, offsets[refIndex])
    refVectors = getVectors(refPoints)
    for i in range(1, len(inputs)):
        if i in rotations:  # skip if rotation already known
            continue

        for r in range(0, 24):
            # print(f'looking at {i}/{r} through {refIndex}')

            rotatedPoints = rotatePoints(r, inputs[i])
            commonEdges = getEdgesIntersection(
                refVectors, getVectors(rotatedPoints))
            if(len(commonEdges) >= getNbEdges(12)):
                print(
                    f'found rotation for scanner {i} from scanner {refIndex}: {r} (len: {len(commonEdges)})')

                for refPoint in refPoints:
                    for targetPoint in rotatedPoints:
                        offset = addPoints(refPoint, revertPoint(targetPoint))
                        offsetedPoints = offsetPoints(rotatedPoints, offset)
                        if len(getPointsIntersection(refPoints, offsetedPoints)) >= 12:
                            print(
                                f'found offset for scanner {i} from scanner {refIndex}: {offset}')
                            rotations[i] = r
                            offsets[i] = offset
                            refQueues.append(i)
                            break
                    if i in offsets:
                        break

                break

print(len(rotations))
print(rotations)
print(len(offsets))
print(offsets)

allPoints = inputs[0].copy()
for i in range(1, len(inputs)):
    rotated = rotatePoints(rotations[i], inputs[i])
    offseted = offsetPoints(rotated, offsets[i])
    for point in offseted:
        if point not in allPoints:
            allPoints.append(point)

print(len(allPoints))
