import sys
input = sys.stdin.readline
from collections import deque

# 굴 D
# 고슴도치 S
# 물 *
# 돌 X

def mool():
    size = len(water)
    for _ in range(size):
        ci, cj = water.popleft()
        for di, dj in ((0,1), (-1,0), (0,-1), (1,0)):
            ni, nj = ci+di, cj+dj
            # 범위 내이고 아무 것도 없다면 물로 채우기
            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == ".":
                water.append((ni,nj))
                arr[ni][nj] = "*"


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

ei = ej = si = sj = -1
water = deque([])
vi = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == "D":
            ei, ej = i, j
        elif arr[i][j] == "S":
            si, sj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == "*":
            water.append((i, j))

q = deque([(si, sj)])
vi[si][sj] = 1

while q:
    mool()
    l = len(q)

    for _ in range(l):
        ci, cj = q.popleft()

        # 비버굴인지 파악
        if (ci, cj) == (ei, ej):
            print(vi[ci][cj] - 1)
            sys.exit(0)
        # 비버굴 아니면 주변 파악
        for di, dj in ((0, 1), (-1, 0), (0, -1), (1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < R and 0 <= nj < C and (arr[ni][nj] == "." or arr[ni][nj] == "D") and not vi[ni][nj]:
                vi[ni][nj] = vi[ci][cj] + 1
                q.append((ni,nj))

print("KAKTUS")