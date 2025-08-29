import sys
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
mo = ["a", "e", "i", "o", "u"]

for case in combinations(lst, L):
    m = 0
    z = 0
    for st in case:
        if st in mo:
            m += 1
        else:
            z += 1
    if m >= 1 and z >= 2:
        print(''.join(case))