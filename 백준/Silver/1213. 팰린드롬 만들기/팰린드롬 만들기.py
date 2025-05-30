import sys
input = sys.stdin.readline
from collections import defaultdict

hansoo = input().strip()

l = len(hansoo)
dct = defaultdict(int)
for st in hansoo:
    dct[st] += 1
ans = ""

if l % 2 == 0:
    for i in dct.values():
        if i % 2:
            ans = "I'm Sorry Hansoo"
            break
else:
    tmp = 0
    for i in dct.values():
        if i % 2:
            tmp += 1

        if tmp > 1:
            ans = "I'm Sorry Hansoo"
            break

if ans != "I'm Sorry Hansoo":
    half = ''
    middle = ''

    for i in sorted(dct.keys()):
        if dct[i] % 2 == 1:
            middle = i
        half += i * (dct[i] // 2)

    ans = half + middle + half[::-1]

print(ans)