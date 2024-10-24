import heapq
import sys
input = sys.stdin.readline

INF = float('inf')
N, E = map(int, input().split())
lst = [[] for _ in range(N+1)]

def da(s, distance):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, c = heapq.heappop(q)

        if distance[c] < dist:
            continue

        for next, next_dis in lst[c]:
            cost = dist + next_dis
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))


for _ in range(E):
    a, b, c = map(int, input().split())
    lst[a].append((b,c))
    lst[b].append((a, c))

v1, v2 = map(int, input().split())

dist_1 = [INF] * (N + 1)
dist_v1 = [INF] * (N + 1)
dist_v2 = [INF] * (N + 1)

da(1, dist_1)
da(v1, dist_v1)
da(v2, dist_v2)

# 1 > v1 > v2 > N
path_1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
# 1 > v2 > v1 > N
path_2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]

result = min(path_1, path_2)
if result >= INF:
    print(-1)
else:
    print(result)