import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

sm = [0] * (N+1)
for i in range(1, N+1):
    sm[i] = sm[i-1] + nums[i-1]

for _ in range(M):
    s, e = map(int, input().split())
    ans = sm[e] - sm[s-1]
    print(ans)