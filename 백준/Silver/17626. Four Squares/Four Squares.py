import sys
input = sys.stdin.readline

num = int(input())

def fs(n):
  dp = [float('inf')] * (n + 1)
  dp[0] = 0  # 0은 제곱수의 합이 아무것도 없으므로 0으로 초기화

  for i in range(1, n + 1):
    j = 1
    while j * j <= i:
      dp[i] = min(dp[i], dp[i - j * j] + 1)
      j += 1

  return dp[n]

print(fs(num))