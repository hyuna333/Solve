import sys
input = sys.stdin.readline

td, N = map(int, input().split())
dp = [float('inf')] * (td+100)
dp[0] = 0

for i in range(N):
    cost, num = map(int, input().split())

    for j in range(num, td+100):
        dp[j] = min(dp[j], dp[j-num]+cost)

print(min(dp[td:]))