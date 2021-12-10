import os
import functools
from typing import Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))


def getCloser(char: str) -> Tuple[str, str]:
    if char == "(":
        return ")", ""
    elif char == "[":
        return "]", ""
    elif char == "{":
        return "}", ""
    elif char == "<":
        return ">", ""
    return "", char


def findCloser(char: str, remaining: str) -> Tuple[str, int, str]:
    closer, illegal = getCloser(char)
    if illegal != "":
        return "", -1, illegal

    i = 0
    while i < len(remaining):
        if remaining[i] == closer:
            return closer, i, ""
        else:
            _, localI, illegal = findCloser(remaining[i], remaining[i+1::])
            if illegal != "":
                return "", -1, illegal
            i += localI+2
    # print("did not find end: incomplete")
    return "", -1, ""


def getPoints(char: str) -> int:
    if char == ")":
        return 3
    elif char == "]":
        return 57
    elif char == "}":
        return 1197
    elif char == ">":
        return 25137
    return None


sum = 0
for line in lines:
    closer, _, illegal = findCloser(line[0], line[1::])
    print(f'{line} -> {closer} / {illegal}')
    if illegal != "":
        sum += getPoints(illegal)

print(sum)
