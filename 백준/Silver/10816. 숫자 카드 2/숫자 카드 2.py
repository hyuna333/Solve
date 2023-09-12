import sys
from collections import Counter

N = int(sys.stdin.readline())
own = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

dct = Counter(own)

for num in check:
    if num in dct:
        print(dct[num], end=" ")
    else:
        print(0, end=" ")