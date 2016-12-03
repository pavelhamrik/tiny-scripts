import sys

def golden_ratio(dim, orig):
    ratio = dim / 1.618
    print round(ratio, 2)
    if ratio / orig > 0.01:
        return golden_ratio(ratio, orig)
    return ratio


if len(sys.argv[1:]) != 1:
    print "Error: Please include exactly one argument (dimension)"
    quit()

dim = float(sys.argv[1])
golden_ratio(dim, dim)
