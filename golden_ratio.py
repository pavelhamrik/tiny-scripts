# ---------------------------------------------- #
# superseded by the ratio.py script in this repo #
# ---------------------------------------------- #

import sys

def golden_ratio(dim, orig, direction):
    ratio = dim * (1.618 ** direction)
    print(round(ratio, 2))
    if (ratio / orig) ** direction < 100:
        return golden_ratio(ratio, orig, direction)
    return ratio

if len(sys.argv[1:]) < 1:
    print("Error: Please include at least one argument: dimension (float), direction (optional, 1 or -1).")
    quit()

direction = 1
if len(sys.argv[1:]) >= 2:
    if sys.argv[2] != "1" and sys.argv[2] != "-1":
        print("Error: Second argument (direction) can only be 1 (ascending numbers) or -1 (descending numbers).")
        quit()
    direction = int(sys.argv[2])

dim = float(sys.argv[1])

golden_ratio(dim, dim, direction)
