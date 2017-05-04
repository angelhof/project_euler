from collections import deque
from itertools import combinations

def compute_pentagon(i):
    return i*(3*i-1)/2

def is_pentagon(i):
    n = ((24*i+1) ** 0.5 + 1) / 6.0
    return n.is_integer()


pairs = combinations(map(compute_pentagon, range(1,5000)), 2)
pairs = sorted(pairs, key=lambda x: x[1] -x[0])
for pair in pairs:
    print pair
    if(is_pentagon(pair[1]-pair[0]) and is_pentagon(pair[1] + pair[0])):
        print "Great!!!", pair, pair[1] - pair[0]
        exit(0)

