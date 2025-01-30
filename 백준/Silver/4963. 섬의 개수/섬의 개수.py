import sys
input = sys.stdin.readline

def visit(si, sj):
    q = [(si, sj)]

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<h and 0<=nj<w and arr[ni][nj] and not vi[ni][nj]:
                vi[ni][nj] = 1
                q.append((ni,nj))
    return

while True:
    w, h = map(int, input().split())
    if w == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    vi = [[0]*w for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] and not vi[i][j]:
                vi[i][j] = 1
                visit(i,j)
                ans += 1

    print(ans)