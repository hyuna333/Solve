import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
lst = list(map(int, input().split()))
X = int(input())

def compare(a, b):
    while b:
        a, b = b, a % b

    if a == 1:
        return True
    else:
        return False

sm = 0
cnt = 0
for num in lst:
    a, b = max(num, X), min(num, X)
    if compare(a, b):
        sm += num
        cnt += 1

print(sm / cnt)
