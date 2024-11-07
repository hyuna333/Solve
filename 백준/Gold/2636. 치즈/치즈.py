import sys
input = sys.stdin.readline

def cheese(vi):
    q = [(0,0)]
    vi[0][0] = 1
    cnt = 0

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<n and 0<=nj<m and not vi[ni][nj]:
                if not arr[ni][nj]:
                    q.append((ni,nj))
                else:
                    arr[ni][nj] = 0
                    cnt += 1
                vi[ni][nj] = 1

    return cnt

n, m = map(int, input().split())
arr = []
arr = [list(map(int, input().split())) for _ in range(n)]

ans = []
while True:
    vi = [[0] * m for _ in range(n)]
    ch = cheese(vi)

    if ch == 0:
        print(len(ans))
        print(ans[-1])
        break
    ans.append(ch)
