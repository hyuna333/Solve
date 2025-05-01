import sys
input = sys.stdin.readline
from collections import deque

def ant(si, sj):
    q = deque([(si, sj)])
    vi[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<M and 0<=nj<N and arr[ni][nj] == 1 and not vi[ni][nj]:
                q.append((ni,nj))
                vi[ni][nj] = 1


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
vi = [[0]*N for _ in range(M)]
ans = 0

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 and not vi[i][j]:
            ans += 1
            ant(i, j)

print(ans)