import sys

lst = list(map(int, sys.stdin.readline().split()))
N = len(lst)

for i in range(N-1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            print(*lst)