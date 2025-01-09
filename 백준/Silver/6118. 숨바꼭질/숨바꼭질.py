import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
vi = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)

q = [1]
while q:
    c = q.pop(0)
    vi[1] = 1

    for n in adj[c]:
        if not vi[n]:
            vi[n] = vi[c] + 1
            q.append(n)

mx = max(vi)
idx = vi.index(mx)
cnt = vi.count(mx)
print(idx, mx-1, cnt)