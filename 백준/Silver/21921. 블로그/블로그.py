import sys
input = sys.stdin.readline
from collections import defaultdict

N, X = map(int, input().split())
vi = list(map(int, input().split()))
sm = defaultdict(int)
ans = 0

if X == N:
    ans = sum(vi)
else:
    pp = [0] * (N+1)
    pp[1] = vi[0]

    for i in range(2, N+1):
        pp[i] = pp[i-1] + vi[i-1]

    for j in range(X, N+1):
        tmp = pp[j] - pp[j-X]
        ans = max(ans, tmp)
        sm[tmp] += 1


if ans == 0:
    print("SAD")
else:
    print(ans)
    print(sm[ans])