import sys

N, M = map(int, sys.stdin.readline().split())
box = [n for n in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    box[i], box[j] = box[j], box[i]

ans = box[1:]
print(*ans)