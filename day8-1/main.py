import os
from typing import NamedTuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

nbOfUniques = 0
for line in lines:
    parts = line.split(" | ")
    inputs = parts[0].split()
    outputs = parts[1].split()
    for output in outputs:
        l = len(output)
        if l == 2:
            nbOfUniques += 1
        elif l == 3:
            nbOfUniques += 1
        elif l == 4:
            nbOfUniques += 1
        elif l == 7:
            nbOfUniques += 1

print(nbOfUniques)
