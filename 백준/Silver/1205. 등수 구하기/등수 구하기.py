import sys
input = sys.stdin.readline

N, ns, P = map(int, input().split())

rank = list(map(int, input().split()))
ans = 1

if N == P and rank[-1] >= ns:
    ans = -1
else:
    rank.append(ns)
    rank.sort(reverse=True)
    ans = rank.index(ns) + 1

print(ans)