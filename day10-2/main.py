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
    completers = ""
    while i < len(remaining):
        if remaining[i] == closer:
            return "", i, ""
        else:
            completer, localI, illegal = findCloser(
                remaining[i], remaining[i+1::])
            if illegal != "":
                return "", -1, illegal
            i += localI+2
            completers += completer

    # print("did not find end: incomplete")
    return completers+closer, -1, ""


def solveLine(line: str) -> str:
    indicesToClose: list[int] = [0]
    for i in range(1, len(line)):
        char = line[i]
        if len(indicesToClose) > 0:
            toClose = line[indicesToClose[-1]]
            closer, illegal = getCloser(toClose)
        else:
            closer = ""

        if illegal != "":
            return "corrupted"

        if char == closer:
            indicesToClose = indicesToClose[0:-1]
        else:
            indicesToClose.append(i)

    res = ""
    for i in reversed(indicesToClose):
        closer, _ = getCloser(line[i])
        res += closer
    return res


def getPoints(char: str) -> int:
    if char == ")":
        return 1
    elif char == "]":
        return 2
    elif char == "}":
        return 3
    elif char == ">":
        return 4
    return None


scores = []
for line in lines:
    res = solveLine(line)
    if res == "corrupted":
        continue

    total = 0
    for char in res:
        total = total * 5 + getPoints(char)
    print(f'{res} -> {total}')
    scores.append(total)
scores = sorted(scores)
print(scores[int(len(scores)/2)])
