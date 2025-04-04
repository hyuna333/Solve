import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
two = []
zero = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zero.append((i, j))
        elif lab[i][j] == 2:
            two.append((i, j))

# 바이러스 퍼트리는 거
def bfs(si, sj):
    q = deque([(si, sj)])
    vi[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not tmp[ni][nj] and not vi[ni][nj]:
                tmp[ni][nj] = 2
                q.append((ni,nj))
                vi[ni][nj] = 1

# 안전지대 세는거
def safe(arr):
    zone = 0
    for lst in arr:
        zone += lst.count(0)
    return zone

ans = 0
for walls in combinations(zero, 3):
    tmp = [row[:] for row in lab]
    for bi, bj in walls:
        tmp[bi][bj] = 1

    vi = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2 and not vi[i][j]:
                bfs(i,j)

    num = safe(tmp)
    ans = max(ans, num)

print(ans)