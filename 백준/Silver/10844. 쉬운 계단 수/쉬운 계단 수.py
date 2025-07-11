import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000000
dp = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for n in range(2, N + 1):
    dp[n][0] = dp[n - 1][1] % MOD
    for j in range(1, 9):
        dp[n][j] = (dp[n - 1][j - 1] + dp[n - 1][j + 1]) % MOD
    dp[n][9] = dp[n - 1][8] % MOD

print(sum(dp[N]) % 1000000000)