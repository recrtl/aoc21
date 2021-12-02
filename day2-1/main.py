import os

print('day2-1')

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = open(dir_path+'/input.txt').readlines()

depth = 0
horizontal = 0
for line in lines:
    splits = line.rstrip("\n").split(" ")
    verb = splits[0]
    nb = int(splits[1])

    if verb == 'forward':
        horizontal += nb
    elif verb == 'down':
        depth += nb
    elif verb == 'up':
        depth -= nb
    else:
        print(f'{verb} not handled !')

print(f'depth: {depth}')
print(f'horizontal: {horizontal}')
print(f'result: {depth*horizontal}')
