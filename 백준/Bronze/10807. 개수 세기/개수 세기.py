import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
V = int(sys.stdin.readline())

cnt = 0
for i in lst:
    if i == V:
        cnt += 1

print(cnt)