import sys
import math
input = sys.stdin.readline

def find(pa, x):
    if pa[x] != x:
        pa[x] = find(pa, pa[x])
    return pa[x]

def union(pa, rank, x, y):
    rx = find(pa, x)
    ry = find(pa, y)

    if rx != ry:
        if rank[rx] > rank[ry]:
            pa[ry] = rx
        elif rank[rx] < rank[ry]:
            pa[rx] = ry
        else:
            pa[ry] = rx
            rank[rx] += 1

N, M = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(N)]

# 간선들
edges = []
for i in range(N):
    for j in range(i+1, N):
        dis = math.sqrt((dots[i][0] - dots[j][0])**2 + (dots[i][1] - dots[j][1])**2)
        edges.append((dis, i, j))

pa = [i for i in range(N)]
rank = [0] * N

# 연결되어 있는 애들은 같은 그룹으로 만들기
for _ in range(M):
    u, v = map(int, input().split())
    union(pa, rank, u - 1, v - 1)

edges.sort()
ans = 0

for dist, u, v in edges:
    # 다른 그룹이라면 길이 추가하고 같은 그룹으로 만들기
    if find(pa, u) != find(pa, v):
        union(pa, rank, u, v)
        ans += dist

print(f"{ans:.2f}")