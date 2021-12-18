import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

print(os.path.basename(dir_path))

inputs = []
for line in lines:
    exec(f'inputs.append({line})')
print(inputs)


def carry(value, carries):  # takes int or pair and returns updated value and remaining carries
    if isinstance(value, int):
        value += carries[0]+carries[1]
        return value, [0, 0]

    if isinstance(value[0], int):
        value[0] += carries[1]
        carries[1] = 0
    else:
        value[0], tmpCarries = carry(value[0], [0, carries[1]])
        carries[1] = tmpCarries[1]

    if isinstance(value[1], int):
        value[1] += carries[0]
        carries[0] = 0
    else:
        value[1], tmpCarries = carry(value[1], [carries[0], 0])
        carries[0] = tmpCarries[0]

    return value, carries


def explode(pair, depth):  # returns exploded, resulting pair, carries
    if isinstance(pair[0], int) and isinstance(pair[1], int):
        if depth > 4:
            return True, 0, pair
        else:
            return False, pair, [0, 0]

    exploded = False
    carries = [0, 0]
    if isinstance(pair[0], list):
        exploded, pair[0], carries = explode(pair[0], depth+1)
        if exploded and carries[1] > 0:
            pair[1], tmpCarries = carry(pair[1], [0, carries[1]])
            carries[1] = tmpCarries[1]

    if not exploded and isinstance(pair[1], list):
        exploded, pair[1], carries = explode(pair[1], depth+1)
        if exploded and carries[0] > 0:
            pair[0], tmpCarries = carry(pair[0], [carries[0], 0])
            carries[0] = tmpCarries[0]

    if not exploded:
        return False, pair, None
    else:
        return True, pair, carries


def split(value):
    if isinstance(value, int):
        if value < 10:
            return False, value
        else:
            half = value/2
            return True, [math.floor(half), math.ceil(half)]
    else:
        splitted, value[0] = split(value[0])
        if not splitted:
            splitted, value[1] = split(value[1])
        return splitted, value


def reduce(pair):
    reducing = True
    while reducing:
        reducing, pair, _ = explode(pair, 1)
        if reducing:
            # print(f'exploded: {pair}')
            continue
        reducing, pair = split(pair)
        # if reducing:
        #     print(f'splitted: {pair}')


def add(v1, v2):
    return [v1, v2]


def magnitude(value):
    if isinstance(value, int):
        return value
    else:
        return 3*magnitude(value[0]) + 2*magnitude(value[1])


sum = inputs[0]
for i in range(1, len(inputs)):
    sum = add(sum, inputs[i])
    reduce(sum)
    print(sum)

print(magnitude(sum))
