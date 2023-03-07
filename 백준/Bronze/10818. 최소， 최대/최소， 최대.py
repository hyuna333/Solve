import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

mx = mn = lst[0]
for i in lst:
    if mx < i: mx = i
    if mn > i: mn = i

print(mn, mx)