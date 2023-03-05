import sys

N, M = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
dr = 0
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
arr = [[0]*M for _ in range(N)]

if K > N*M:
    print(0)
else:
    num = 1
    ci = cj = 0
    while num < K:
        arr[ci][cj] = num
        ni, nj = ci+di[dr], cj+dj[dr]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
            ci, cj = ni, nj
        else:
            dr = (dr+1)%4
            ci, cj = ci+di[dr], cj+dj[dr]
        num += 1
    print(ci+1, cj+1)