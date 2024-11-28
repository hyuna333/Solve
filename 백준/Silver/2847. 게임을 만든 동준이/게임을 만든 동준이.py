import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    n = int(input())
    lst.append(n)

ans = 0

for i in range(N-2, -1, -1):
    std = lst[i+1]
    while lst[i] >= std:
        ans += 1
        lst[i] -= 1

print(ans)