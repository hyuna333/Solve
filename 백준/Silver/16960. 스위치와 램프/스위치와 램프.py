import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dct = {n:0 for n in range(1, M+1)}
swt = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    tmp = set()
    for j in range(N):
        if i == j:
            continue
        tmp.update(swt[j][1:])
    if len(tmp) == M:
        ans = 1
        break

print(ans)