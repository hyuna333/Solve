import sys
input = sys.stdin.readline
from collections import deque

def link(si, sj, n):
    q = deque([(si, sj)])
    size = 1
    arr[si][sj] = n

    while q:
        ci, cj = q.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                q.append((ni, nj))
                arr[ni][nj] = n
                size += 1
    return size

def change(ci, cj):
    st = set()
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni, nj = ci + di, cj + dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]:
            st.add(arr[ni][nj])

    sm = 1
    for li in st:
        sm += dct[li]
    return sm

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 연결된 요소 미리 계산하기
dct = {}
num = 2
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            dct[num] = link(i, j, num)
            num += 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            ans = max(ans, change(i, j))

print(ans)