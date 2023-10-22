import sys
input = sys.stdin.readline

def dfs(a):
    ans_dfs.append(a)
    vi[a] = 1

    for i in lst[a]:
        if not vi[i]:
            dfs(i)

def bfs(a):
    q = []

    q.append(a)
    ans_bfs.append(a)
    vi[a] = 1

    while q:
        n = q.pop(0)
        for i in lst[n]:
            if not vi[i]:
                q.append(i)
                ans_bfs.append(i)
                vi[i] = 1



N, M, V = map(int, input().split())

lst = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for n in lst:
    n.sort()

ans_dfs = []
vi = [0] * (N+1)
dfs(V)

ans_bfs = []
vi = [0] * (N+1)
bfs(V)

print(*ans_dfs)
print(*ans_bfs)