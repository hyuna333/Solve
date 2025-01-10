import sys
input = sys.stdin.readline
from collections import deque


def st():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return i, j

def feed(si, sj):
    q = deque([(si, sj, 0)])
    vi = [[0]*N for _ in range(N)]
    vi[si][sj] = 1
    fishes = []

    while q:
        ci, cj, t = q.popleft()
        # 먹을 수 있는 물고기
        if 0 < arr[ci][cj] < size:
            fishes.append((t, ci, cj))

        # 순서 위, 왼, 오, 아
        for di, dj in ((-1,0), (0,-1), (0,1), (1,0)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni <N and 0 <= nj <N and not vi[ni][nj] and arr[ni][nj] <= size:
                vi[ni][nj] = 1
                q.append((ni, nj, t+1))
                
    if fishes:
        # 가장 위, 왼쪽 물고기 선택
        fishes.sort()  
        return fishes[0][1], fishes[0][2], fishes[0][0]
    return si, sj, -1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
size = 2
eat = 0
ans = 0

si, sj = st()
arr[si][sj] = 0
while True:
    si, sj, tmp = feed(si, sj)
    if tmp == -1:
        break
    ans += tmp
    arr[si][sj] = 0
    eat += 1
    if eat == size:
        eat = 0
        size += 1

print(ans)