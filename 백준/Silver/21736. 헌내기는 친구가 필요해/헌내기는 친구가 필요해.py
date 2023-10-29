import sys
input = sys.stdin.readline

def start(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'I':
                return i, j

def move(si, sj):
    global ans
    q = [(si, sj)]
    vi = [[0] * M for _ in range(N)]
    vi[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if arr[ci][cj] == 'P':
            ans += 1

        for di, dj in ((1, 0), (0, -1), (-1, 0), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 캠퍼스 내이고 벽이 아니고 안 가본 곳이라면 진행
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 'X' and not vi[ni][nj]:
                q.append((ni, nj))
                vi[ni][nj] = 1


N, M = map(int, input().split())
arr = []
for _ in range(N):
    lst = list(input().strip())
    arr.append(lst)

# 도연이 위치
si, sj = start(arr)
ans = 0
move(si, sj)

if ans:
    print(ans)
else:
    print('TT')