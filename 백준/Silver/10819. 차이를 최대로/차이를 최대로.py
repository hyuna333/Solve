import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
ans = 0

for perm in permutations(nums):
    sm = 0
    for i in range(N-1):
        sm += abs(perm[i] - perm[i+1])
    ans = max(ans, sm)

print(ans)