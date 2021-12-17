import os
import functools
from typing import Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

print(lines[0])
splits = lines[0].split(" ")
xsplits = splits[-2].split(",")[0].split("=")[1].split("..")
ysplits = splits[-1].split("=")[1].split("..")
targetMin = [int(xsplits[0]), int(ysplits[0])]
targetMax = [int(xsplits[1]), int(ysplits[1])]
print(targetMin, targetMax)


def getTrajectory(vel, cond):
    pos = [0, 0]
    traj = [pos.copy()]
    while True:
        pos[0] += vel[0]
        pos[1] += vel[1]
        if vel[0] > 0:  # ignore negative x
            vel[0] -= 1
        vel[1] -= 1
        traj.append(pos.copy())

        if cond(traj):
            break
    return traj


def condAfterTarget(traj):
    return traj[-1][0] > targetMax[0] or traj[-1][1] < targetMin[1]


def renderTraj(traj):
    # return
    print()
    maxX = max(traj, key=lambda pos: pos[0])[0]
    minY = min(traj, key=lambda pos: pos[1])[1]-1
    maxY = max(traj, key=lambda pos: pos[1])[1]
    minY = min(minY, targetMin[1])
    maxX = max(maxX, targetMax[0]+1)
    for y in range(maxY, minY, -1):
        row = ""
        for x in range(0, maxX):
            if x == 0 and y == 0:
                row += "S"
            elif [x, y] in traj:
                row += "#"
            elif x >= targetMin[0] and y >= targetMin[1] and x <= targetMax[0] and y <= targetMax[1]:
                row += "T"
            else:
                row += "."
        print(row)


def condXStaticOrInTarget(traj):
    if len(traj) >= 2 and traj[-1][0] == traj[-2][0]:
        return True
    if traj[-1][0] > targetMin[0]:
        return True
    return False


# solve x:
xMin = 0
while True:
    traj = getTrajectory([xMin, 0], condXStaticOrInTarget)
    print(traj)
    # renderTraj(traj)
    if traj[-1][0] > targetMin[0]:
        break
    xMin += 1

xMax = targetMax[0]+1

print(f'xMin={xMin}, xMax={xMax}')


def isInTarget(pos):
    return pos[0] >= targetMin[0] and pos[1] >= targetMin[1] and pos[0] <= targetMax[0] and pos[1] <= targetMax[1]


yMin = targetMin[1]
nbTraj = 0
for x in range(xMin, xMax+1):
    print(x)
    for y in range(yMin, 300):
        traj = getTrajectory([x, y], condAfterTarget)
        if isInTarget(traj[-2]):
            # print([x, y])
            nbTraj += 1

print(nbTraj)
