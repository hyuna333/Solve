import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
pa = [-1] * N
nodes = list(map(int, input().split()))
adj = [[] for _ in range(N)]
de = int(input())
ans = 0

for i in range(len(nodes)):
    p = nodes[i]
    if p != -1:
        pa[i] = p
        if i != de:
            adj[p].append(i)

q = deque([de])
pa[de] = 100

while q:
    c = q.popleft()
    for n in adj[c]:
        pa[n] = 100
        q.append(n)

for i in range(N):
    if pa[i] != 100 and len(adj[i]) == 0:
        ans += 1

print(ans)