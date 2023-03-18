import sys

N, M = map(int, sys.stdin.readline().split())

ans = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        ans[i][j] += lst[j]
    print(*ans[i])