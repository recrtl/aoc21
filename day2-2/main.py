import os

print('day2-2')

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = open(dir_path+'/input.txt').readlines()

depth = 0
horizontal = 0
aim = 0
for line in lines:
    splits = line.rstrip("\n").split(" ")
    verb = splits[0]
    nb = int(splits[1])

    if verb == 'forward':
        horizontal += nb
        depth += nb * aim
    elif verb == 'down':
        aim += nb
    elif verb == 'up':
        aim -= nb
    else:
        print(f'{verb} not handled !')

print(f'depth: {depth}')
print(f'horizontal: {horizontal}')
print(f'result: {depth*horizontal}')
