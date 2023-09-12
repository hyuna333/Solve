import sys

N, K = map(int, sys.stdin.readline().split())

lst = [i for i in range(1, N+1)]

idx = K - 1
ans = []

print('<', end="")
while lst:
    if idx >= len(lst):
        idx %= len(lst)
    else:
        ans.append(lst.pop(idx))
        idx += K - 1

print(*ans, sep=", ", end="")
print('>')