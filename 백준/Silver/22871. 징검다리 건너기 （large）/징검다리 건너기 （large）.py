import sys
input = sys.stdin.readline

N = int(input())
stone = list(map(int, input().split()))

dp = [float("inf")]*N
dp[0] = 0

for i in range(1, N):
    for j in range(i):
        tmp = (i-j) * (1+abs(stone[j]-stone[i]))
        dp[i] = min(dp[i], max(dp[j], tmp))

print(dp[-1])