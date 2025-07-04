import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
ans = 0

dp = [0] * N

for i in range(N):
    mx = scores[i]
    mn = scores[i]

    for k in range(i, -1, -1):
        mx = max(mx, scores[k])
        mn = min(mn, scores[k])
        val = mx - mn
        if k == 0:
            dp[i] = max(dp[i], val)
        else:
            dp[i] = max(dp[i], dp[k - 1] + val)

print(dp[N - 1])