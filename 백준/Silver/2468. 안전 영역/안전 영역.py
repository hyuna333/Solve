import sys
input = sys.stdin.readline

def rain(si, sj, h, vi):
    q = [(si, sj)]
    vi[si][sj] = 1

    while q:
        ci, cj = q.pop()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not vi[ni][nj] and arr[ni][nj] > h:
                vi[ni][nj] = 1
                q.append((ni, nj))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = 0

for w in range(max(map(max, arr))):
    vi = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > w and not vi[i][j]:
                rain(i, j, w, vi)
                ans += 1
    mx = max(mx, ans)

print(mx)