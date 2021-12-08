import os
import functools

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))


def diff(str1, str2):
    res = ""
    for char in str1:
        if char not in str2:
            res += char
    for char in str2:
        if char not in str1:
            res += char
    return res


def intersection(str1, str2):
    res = ""
    for char in str1:
        if char in str2:
            res += char
    return res


def subtract(str1, str2):
    res = ""
    for char in str1:
        if char not in str2:
            res += char
    return res


digitToSegments = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}

sum = 0

for line in lines:
    parts = line.split(" | ")
    inputs = parts[0].split()
    outputs = parts[1].split()
    inputsByLen = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for input in inputs:
        inputsByLen[len(input)].append(input)

    one = inputsByLen[2][0]
    seven = inputsByLen[3][0]
    four = inputsByLen[4][0]
    eight = inputsByLen[7][0]
    twoThreeFive = inputsByLen[5]
    zeroSixNine = inputsByLen[6]

    all = "abcdefg"
    # store possibilities
    segmentMap = {
        "a": all,
        "b": all,
        "c": all,
        "d": all,
        "e": all,
        "f": all,
        "g": all,
    }
    segmentMap["a"] = diff(one, seven)
    # segments that variate between 0, 6 and 9 (d, c, e)
    zeroSixNineVariants = ''.join(list(filter(
        lambda x: x not in zeroSixNine[0] or x not in zeroSixNine[1] or x not in zeroSixNine[2],
        all,
    )))
    segmentMap["d"] = diff(one, four)
    segmentMap["d"] = intersection(
        segmentMap["d"], zeroSixNineVariants)

    segmentMap["b"] = diff(diff(one, four), segmentMap["d"])

    segmentMap["c"] = intersection(zeroSixNineVariants, one)
    segmentMap["f"] = diff(one, segmentMap["c"])

    segmentMap["e"] = subtract(
        zeroSixNineVariants, segmentMap["c"]+segmentMap["d"])
    segmentMap["g"] = subtract(
        all, segmentMap["a"]+segmentMap["b"]+segmentMap["c"]+segmentMap["d"]+segmentMap["e"]+segmentMap["f"])

    print(segmentMap)

    translator = {}
    for k in segmentMap:
        translator[segmentMap[k]] = k

    translatedOutput = ""
    for output in outputs:
        translation = ""
        for char in output:
            translation += translator[char]
        translation = "".join(sorted(translation))
        translatedOutput += digitToSegments[translation]
    print(translatedOutput)

    sum += int(translatedOutput)

print(sum)
