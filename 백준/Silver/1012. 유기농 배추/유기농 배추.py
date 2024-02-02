import sys
input = sys.stdin.readline

def bug(ci, cj):
    q = [(ci, cj)]

    while q:
        ci, cj = q.pop()
        arr[ci][cj] = 0

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj]:
                q.append((ni, nj))



T = int(input())
for _ in range(T):
    ans = 0
    M, N, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if arr[i][j]:
                bug(i, j)
                ans += 1

    print(ans)
