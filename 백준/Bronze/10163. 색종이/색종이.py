import sys

N = int(sys.stdin.readline())
arr = [[0]*1001 for _ in range(1001)]

for num in range(1, N+1):
    sj, si, ga, se = map(int, sys.stdin.readline().split())
    for i in range(si, si+se):
        for j in range(sj, sj+ga):
            arr[i][j] = num

ans = [0]*(N+1)
for i in range(1001):
    for j in range(1001):
        if arr[i][j] == 0: pass
        else:
            ans[arr[i][j]] += 1
cnt = ans[1:]

for i in range(len(cnt)):
    print(cnt[i])
