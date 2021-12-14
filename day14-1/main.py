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

for step in range(0, 10):
    newPolymer = ""
    for i in range(0, len(polymer)-1):
        insert = rules[polymer[i]+polymer[i+1]]
        newPolymer += polymer[i]+insert
    newPolymer += polymer[-1]
    polymer = newPolymer
    print(f'After step #{step+1}:\t{polymer}')

elements = []
counts = []
for element in polymer:
    if element not in elements:
        elements.append(element)
        counts.append(polymer.count(element))
res = max(counts) - min(counts)
print(res)
