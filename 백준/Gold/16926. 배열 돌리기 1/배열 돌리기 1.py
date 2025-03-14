import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

half = min(N,M)//2

for h in range(half):
    layer = deque()
    for i in range(h, M-h):
        layer.append(arr[h][i])
    for i in range(h+1, N-h):
        layer.append(arr[i][M-h-1])
    for i in range(M-2-h, h-1, -1):
        layer.append(arr[N-h-1][i])
    for i in range(N-2-h, h, -1):
        layer.append(arr[i][h])

    layer.rotate(-(R%len(layer)))

    for i in range(h, M-h):
        arr[h][i] = layer.popleft()
    for i in range(h+1, N-h):
        arr[i][M-h-1] = layer.popleft()
    for i in range(M-2-h, h-1, -1):
        arr[N-h-1][i] = layer.popleft()
    for i in range(N-2-h, h, -1):
        arr[i][h] = layer.popleft()

for j in range(N):
    print(*arr[j])