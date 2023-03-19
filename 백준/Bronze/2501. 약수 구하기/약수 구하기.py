import sys

N, M = map(int, sys.stdin.readline().split())

lst = []
for i in range(1, N+1):
    if N%i == 0:
        lst.append(i)

if len(lst) < M:
    print(0)
else:
    print(lst[M-1])