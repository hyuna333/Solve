import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * N for _ in range(N)]
X = int(input())

now = N ** 2
di = 0
dr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ci = cj = 0
ai = aj = 0

while now >= 1:
    if now == X:
        ai, aj = ci, cj
    arr[ci][cj] = now
    ni, nj = ci + dr[di][0], cj + dr[di][1]
    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
        ci, cj = ni, nj
    else:
        di = (di + 1) % 4
        ci, cj = ci + dr[di][0], cj + dr[di][1]
    now -= 1

for lst in arr:
    print(*lst)
print(ai+1, aj+1)