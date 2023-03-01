import sys

N = int(sys.stdin.readline())
arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    si, sj = map(int, sys.stdin.readline().split())
    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j] += 1
    
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] >= 1: cnt += 1

print(cnt)
