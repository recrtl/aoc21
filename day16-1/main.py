import os
import functools
from typing import Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

print(lines[0])
bits = ""
for char in lines[0]:
    dec = int(char, 16)
    bits += str(bin(dec))[2:].zfill(4)
print(bits)

versionSum = 0


def readPacket(bits: str):
    version = int(bits[0:3], 2)
    global versionSum
    versionSum += version
    type = int(bits[3:6], 2)
    if type != 4:  # operator
        if bits[6] == "0":  # length indicated by 15 next bits
            length = int(bits[7:22], 2)
            offset = 22
            while offset < 22+length:
                offset += readPacket(bits[offset:])
        elif bits[6] == "1":  # nb of packets is indicated by 11 next bits
            nb = int(bits[7:18], 2)
            offset = 18
            for _ in range(0, nb):
                offset += readPacket(bits[offset:])
        else:
            exit(42)
        return offset

    else:  # literal
        offset = 6
        while bits[offset] != "0":
            offset += 5  # don't care about the value for now
        offset += 5
        return offset


readPacket(bits)
print(versionSum)
