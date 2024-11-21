import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []


for _ in range(K):
    I, T = map(int, input().split())
    lst.append((T, I))

dp = [0]*(N+1)

for t, i in lst:
    for j in range(N, t-1, -1):  # 큰 시간부터
        dp[j] = max(dp[j], dp[j-t] + i)

print(dp[N])