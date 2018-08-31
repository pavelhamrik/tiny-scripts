import sys
import argparse

GOLDEN_RATIO = 1.6180339887


def ratio(base, ratio_type, count, direction, decimals):
    ratios = [base]
    for c in range(count):
        ratio = ratios[c] * (ratio_type ** direction)
        ratio = round(ratio, decimals)
        ratios.append(ratio)
    return ratios


# arguments parsing

parser = argparse.ArgumentParser()

parser.add_argument("base", type=float, help="the value to base the ratios on; a number is expected")
parser.add_argument("-a", "--ascending", help="the ratios grow from the base number rather than divide it", action="store_true")
parser.add_argument("-d", "--decimals", type=int, help="the number of decimal places to show", default=2)
parser.add_argument("-c", "--count", type=int, help="how many ratios to calculate", default=8)

args = parser.parse_args()

arg_direction = -1
if args.ascending:
    arg_direction = 1

arg_ratio = GOLDEN_RATIO


# initialize the calculations

golden_ratios = ratio(args.base, arg_ratio, args.count, arg_direction, args.decimals)
print(golden_ratios)