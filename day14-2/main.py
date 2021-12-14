import os
import functools
from typing import Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

polymer = lines[0]
print(polymer)

rules = {}
for i in range(2, len(lines)):
    splits = lines[i].split(" -> ")
    rules[splits[0]] = splits[1]

solutions = {}


def addOccurences(occurences: dict[str, int], key: str, value: int):
    if key in occurences:
        occurences[key] += value
    else:
        occurences[key] = value


def merge(d1: dict[str, int], d2: dict[str, int]):
    for k in d2:
        if k in d1:
            d1[k] += d2[k]
        else:
            d1[k] = d2[k]


def solve(couple: str, iteration: int):
    key = couple+str(iteration)
    if key in solutions:
        return solutions[key]

    if iteration == 0:
        res = {couple[0]: 1}
        addOccurences(res, couple[1], 1)
        return res

    insert = rules[couple]
    res = {}
    res[insert] = -1
    merge(res, solve(couple[0]+insert, iteration-1))
    merge(res, solve(insert + couple[1], iteration-1))
    solutions[key] = res
    return res


res = {}
for i in range(0, len(polymer)-1):
    merge(res, {polymer[i+1]: -1})
    merge(res, solve(polymer[i]+polymer[i+1], 40))
merge(res, {polymer[-1]: 1})
print(res)

diff = max(res.values()) - min(res.values())
print(diff)
