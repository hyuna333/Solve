import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

s = 0
e = max(A) * M
ans = 0

while s <= e:
    m = (s+e)//2
    sm = sum(m//i for i in A)
    if sm >= M:
        e = m-1
        ans = m
    else:
        s = m+1

print(ans)