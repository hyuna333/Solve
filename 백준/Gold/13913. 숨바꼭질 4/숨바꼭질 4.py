import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
MAX = 100001
vi = [False] * MAX
bef = [-1] * MAX

q = deque()
q.append(N)
vi[N] = True
t = [0] * MAX

while q:
    c = q.popleft()

    if c == K:
        print(t[c])
        break

    for n in (c-1, c+1, c*2):
        if 0 <= n < MAX and not vi[n]:
            vi[n] = True
            bef[n] = c
            t[n] = t[c] + 1
            q.append(n)

path = [K]
s = K
while True:
    if bef[s] == -1:
        break
    path.append(bef[s])
    s = bef[s]

print(*path[::-1])