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


def readPacket(bits: str):
    version = int(bits[0:3], 2)
    type = int(bits[3:6], 2)
    if type != 4:  # operator
        values = []
        if bits[6] == "0":  # length indicated by 15 next bits
            length = int(bits[7:22], 2)
            offset = 22
            while offset < 22+length:
                packetValue, packetOffset = readPacket(bits[offset:])
                offset += packetOffset
                values.append(packetValue)
        elif bits[6] == "1":  # nb of packets is indicated by 11 next bits
            nb = int(bits[7:18], 2)
            offset = 18
            for _ in range(0, nb):
                packetValue, packetOffset = readPacket(bits[offset:])
                offset += packetOffset
                values.append(packetValue)
        else:
            exit(42)

        value = ""
        if type == 0:
            value = "+".join(values)
        elif type == 1:
            value = "*".join(values)
        elif type == 2:
            value = f'min([{",".join(values)}])'
        elif type == 3:
            value = f'max([{",".join(values)}])'
        elif type == 5:
            value = f'1 if {values[0]}>{values[1]} else 0'
        elif type == 6:
            value = f'1 if {values[0]}<{values[1]} else 0'
        elif type == 7:
            value = f'1 if {values[0]}=={values[1]} else 0'

        return "("+value+")", offset

    else:  # literal
        offset = 6
        value = ""
        while True:
            value += bits[offset+1:offset+5]
            offset += 5
            if bits[offset-5] == "0":
                break
        value = str(int(value, 2))
        return value, offset


value, _ = readPacket(bits)
print(value)
print("=")
exec(f'print({value})')
