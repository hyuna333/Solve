import sys

N = int(sys.stdin.readline())
arr = [[0]*1001 for _ in range(1001)]

si = sj = 1001
ei = ej = 0
for num in range(1, N+1):
    y, x, ga, se = map(int, sys.stdin.readline().split())
    for i in range(x, x+se):
        for j in range(y, y+ga):
            arr[i][j] = num
            if si > i: si = i
            if sj > j: sj = j
            if ei < i: ei = i
            if ej < j: ej = j

ans = [0]*(N+1)
for n in range(1,N+1):
    for i in range(si, ei+1):
        ans[n] += arr[i].count(n)
        
for i in range(1, len(ans)):
    print(ans[i])
