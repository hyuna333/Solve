import sys
input = sys.stdin.readline

N = int(input())
lose = list(map(int, input().split()))
gain = list(map(int, input().split()))

dp = [0] * 101

if sum(lose) < 100:
    print(sum(gain))
else:
    for i in range(N):
        for hp in range(100, lose[i], -1):
            dp[hp] = max(dp[hp], dp[hp - lose[i]] + gain[i])
    print(max(dp))