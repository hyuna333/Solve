import sys

N, M = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline() for _ in range(N)]
ans = [[0]*M for _ in range(N)]

for i in range(N):
    st = -1
    for j in range(M):
        if arr[i][j] == 'c':
            st = j
        else:
            if st == -1:
                ans[i][j] = st
            else:
                ans[i][j] = j-st
    print(*ans[i])