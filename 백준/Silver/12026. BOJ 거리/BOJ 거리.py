import sys
input = sys.stdin.readline

N = int(input())
block = list(input().strip())
INF = float('inf')
dp = [INF] * N

st = ["B", "O", "J"]
dp[0] = 0

for i in range(N):
    now = block[i]
    idx = st.index(now)
    for j in range(i+1, N):
        if st[(idx+1) % 3] == block[j] and dp[j] > dp[i] + (j-i)**2:
            dp[j] = dp[i] + (j-i)**2

if dp[-1] != INF:
    print(dp[-1])
else:
    print(-1)