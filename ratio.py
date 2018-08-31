import argparse
import math

GOLDEN_RATIO = (1 + math.sqrt(5)) / 2
KEPLER_TRIANGLE = math.sqrt(GOLDEN_RATIO)
TYPOGRAPHIC_SCALE = 2 ** (1 / 5)
SQRT_2 = math.sqrt(2)
HALF_EULER = math.exp(1) / 2
JUST_MINOR_SIXTH = 8 / 5
PERFECT_FOURTH = 4 / 3
PERFECT_FIFTH = 3 / 2


# calculation function reused for all the various ratios

def calc_ratio(base, ratio_type, count, direction, decimals):
    ratios = [base]
    for c in range(count):
        ratio = ratios[c] * (ratio_type ** direction)
        ratio = round(ratio, decimals)
        ratios.append(ratio)
    return ratios


# arguments parsing

parser = argparse.ArgumentParser()

parser.add_argument("base", type=float, help="the value to base the ratios on; a number is expected")
parser.add_argument("-c", "--count", type=int, help="how many ratios to calculate", default=11)
parser.add_argument("-d", "--decimals", type=int, help="the number of decimal places to show; a whole number is expected", default=2)
parser.add_argument("-a", "--ascending", help="the ratios grow from the base number rather than divide it", action="store_true")
parser.add_argument("-r", "--ratio", type=float, help="a custom ratio; a number is expected", default=GOLDEN_RATIO)

parser.add_argument("--golden", help="use golden ratio (" + str(round(GOLDEN_RATIO, 3)) + "); default", action="store_true")
parser.add_argument("--kepler", help="use kepler triangle ratio (" + str(round(KEPLER_TRIANGLE, 3)) + "); default", action="store_true")
parser.add_argument("--typographic", help="use typographic scale ratio (" + str(round(TYPOGRAPHIC_SCALE, 3)) + "); default", action="store_true")
parser.add_argument("--sqrt-2", help="use the square root of 2 ratio (" + str(round(SQRT_2, 3)) + ")", action="store_true")
parser.add_argument("--half-euler", help="use the euler number / 2 ratio (" + str(round(HALF_EULER, 3)) + ")", action="store_true")
parser.add_argument("--minor-sixth", help="use the just minor sixth ratio (" + str(round(JUST_MINOR_SIXTH, 3)) + ")", action="store_true")
parser.add_argument("--perfect-fourth", help="use the perfect fourth ratio (" + str(round(PERFECT_FOURTH, 3)) + ")", action="store_true")
parser.add_argument("--perfect-fifth", help="use the perfect fifth ratio (" + str(round(PERFECT_FIFTH, 3)) + ")", action="store_true")

args = parser.parse_args()

# determine ascending or descending succession of ratios

arg_direction = -1
if args.ascending:
    arg_direction = 1

# determine which ratio to use

arg_ratio = args.ratio

if args.kepler:
    arg_ratio = KEPLER_TRIANGLE

if args.typographic:
    arg_ratio = TYPOGRAPHIC_SCALE

if args.sqrt_2:
    arg_ratio = SQRT_2

if args.half_euler:
    arg_ratio = HALF_EULER

if args.minor_sixth:
    arg_ratio = JUST_MINOR_SIXTH

if args.perfect_fourth:
    arg_ratio = PERFECT_FOURTH

if args.perfect_fifth:
    arg_ratio = PERFECT_FIFTH

# quick fix of a negative number of decimal places

arg_decimals = abs(args.decimals)


# initialize the calculation

output_ratios = calc_ratio(args.base, arg_ratio, args.count, arg_direction, arg_decimals)
print(output_ratios)
