import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())

str = input().strip()
dct = defaultdict(int)
s = 0
ans = 0
cnt = 0

for e in range(len(str)):
    dct[str[e]] += 1
    if dct[str[e]] == 1:
        cnt += 1

    while cnt > N:
        dct[str[s]] -= 1
        if dct[str[s]] == 0:
            cnt -= 1
        s += 1

    ans = max(ans, e - s + 1)

print(ans)