import sys

N, M = map(int, sys.stdin.readline().split())
lst = [n for n in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    L = (j-i)//2

    for k in range(L+1):
        lst[i+k], lst[j-k] = lst[j-k], lst[i+k]

ans = lst[1:]
print(*ans)