import os

print('day3-1')

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = open(dir_path+'/input.txt').readlines()

totals = [0 for i in range(len(lines[0].rstrip("\n")))]

for line in lines:
    for i, char in enumerate(line.rstrip("\n")):
        totals[i] += int(char)

gammaRateBinary = ""
epsilonRateBinary = ""
for value in totals:
    if value > len(lines) / 2:
        gammaRateBinary += "1"
        epsilonRateBinary += "0"
    else:
        gammaRateBinary += "0"
        epsilonRateBinary += "1"

print(f'totals: {totals}')
print(f'gammaRateBinary: {gammaRateBinary}')
print(f'epsilonRateBinary: {epsilonRateBinary}')

gammaRate = int(gammaRateBinary, 2)
epsilonRate = int(epsilonRateBinary, 2)
print(f'gammaRate: {gammaRate}')
print(f'epsilonRate: {epsilonRate}')
print(f'product: {gammaRate*epsilonRate}')
