import sys
input = sys.stdin.readline

def find(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return i, j

def distance(si, sj):
    q = [(si, sj)]

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj+ dj
            # 범위 내이고, 원래 갈 수 있는 땅이고, 간 적이 없는 곳이라면 진행
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] and not vi[ni][nj]:
                vi[ni][nj] = vi[ci][cj] + 1
                q.append((ni, nj))



n, m = map(int, input().split())
arr = []
for _ in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)

si, sj = find(arr)

vi = [[0] * m for _ in range(n)]
distance(si, sj)

for i in range(n):
    for j in range(m):
        if (i, j) == (si, sj):
            print(0, end=' ')
        elif not vi[i][j] and arr[i][j]:
            print(-1, end=' ')
        else:
            print(vi[i][j], end=' ')
    print()