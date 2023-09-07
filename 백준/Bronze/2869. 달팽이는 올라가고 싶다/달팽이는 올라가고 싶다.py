import sys, math
A, B, V = map(int, sys.stdin.readline().split())

ans = 0
if A == V:
    ans = 1
else:
    ans = math.ceil((V - B) / (A - B))

print(ans)