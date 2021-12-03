import os

print('day3-2')

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/input.txt') as f:
    lines = [line.rstrip("\n") for line in f]

nbBits = len(lines[0])

oRatingLines = lines
for i in range(0, nbBits):
    nbOnes = sum(map(lambda line: line[i] == "1", oRatingLines))
    mostUsedBit = "1" if nbOnes >= len(oRatingLines) / 2 else "0"
    oRatingLines = list(
        filter(
            lambda line: line[i] == mostUsedBit,
            oRatingLines
        )
    )
    if len(oRatingLines) == 1:
        break
print(oRatingLines)

co2ratingLines = lines
for i in range(0, nbBits):
    nbOnes = sum(map(lambda line: line[i] == "1", co2ratingLines))
    mostUsedBit = "1" if nbOnes >= len(co2ratingLines) / 2 else "0"
    co2ratingLines = list(
        filter(
            lambda line: line[i] != mostUsedBit,
            co2ratingLines
        )
    )
    if len(co2ratingLines) == 1:
        break
print(co2ratingLines)

oRating = int(oRatingLines[0], 2)
co2rating = int(co2ratingLines[0], 2)
print(f'oRating: {oRating}')
print(f'co2rating: {co2rating}')
print(f'product: {oRating*co2rating}')
