import os
from typing import NamedTuple

print('day6-2')

input = [1,4,1,1,1,1,5,1,1,5,1,4,2,5,1,2,3,1,1,1,1,5,4,2,1,1,3,1,1,1,1,1,1,1,2,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,4,1,1,1,1,4,1,1,5,5,1,1,1,4,1,1,1,1,1,3,2,1,1,1,1,1,2,3,1,1,2,1,1,1,3,1,1,1,2,1,2,1,1,2,1,1,3,1,1,1,3,3,5,1,4,1,1,5,1,1,4,1,5,3,3,5,1,1,1,4,1,1,1,1,1,1,5,5,1,1,4,1,2,1,1,1,1,2,2,2,1,1,2,2,4,1,1,1,1,3,1,2,3,4,1,1,1,4,4,1,1,1,1,1,1,1,4,2,5,2,1,1,4,1,1,5,1,1,5,1,5,5,1,3,5,1,1,5,1,1,2,2,1,1,1,1,1,1,1,4,3,1,1,4,1,4,1,1,1,1,4,1,4,4,4,3,1,1,3,2,1,1,1,1,1,1,1,4,1,3,1,1,1,1,1,1,1,5,2,4,2,1,4,4,1,5,1,1,3,1,3,1,1,1,1,1,4,2,3,2,1,1,2,1,5,2,1,1,4,1,4,1,1,1,4,4,1,1,1,1,1,1,4,1,1,1,2,1,1,2]
print(f'Initial state: {input}')


def initFishesPerAge():
    fishesPerAge = {}
    for value in range(0, 9):
        fishesPerAge[value] = 0
    return fishesPerAge


fishesPerAge = initFishesPerAge()
for value in input:
    fishesPerAge[value] += 1

print(fishesPerAge)

maxDay = 256
for day in range(1, maxDay+1):
    newFishesPerAge = initFishesPerAge()
    for age in fishesPerAge:
        nbOfFish = fishesPerAge[age]
        if age == 0:
            newFishesPerAge[6] += nbOfFish
            newFishesPerAge[8] += nbOfFish
        else:
            newFishesPerAge[age-1] += nbOfFish
    fishesPerAge = newFishesPerAge
    print(f'After {day} day: {fishesPerAge}')

nbOfFish = 0
for age in fishesPerAge:
    nbOfFish += fishesPerAge[age]
print(f'After {maxDay} day, the would be {nbOfFish} fish')
