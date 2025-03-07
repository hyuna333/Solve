import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
pa = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def tree():
    q = deque([1])
    while q:
        n = q.popleft()
        for ch in adj[n]:
            if pa[ch] == 0:
                pa[ch] = n
                q.append(ch)

tree()

for i in range(2, N+1):
    print(pa[i])