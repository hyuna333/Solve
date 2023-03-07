import sys

arr = [[0]*101 for _ in range(101)]
cnt = 0

for _ in range(4):
    si, sj, ei, ej = map(int, sys.stdin.readline().split())
    for i in range(si, ei):
        for j in range(sj, ej):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1

print(cnt)