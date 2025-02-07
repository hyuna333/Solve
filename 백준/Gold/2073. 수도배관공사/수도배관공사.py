import sys
input = sys.stdin.readline

D, P = map(int, input().split())
pipes = []
INF = float('inf')
dp = [0] * (D+1)
dp[0] = INF

for _ in range(P):
    L, C = map(int, input().split())
    pipes.append((L,C))

pipes.sort(key=lambda x: -x[1])

for L, C in pipes:
    for j in range(D, L-1, -1):
        if dp[j-L] > 0:
            dp[j] = max(dp[j], min(dp[j-L], C))

print(dp[D])