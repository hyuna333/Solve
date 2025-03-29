import sys
input = sys.stdin.readline
import heapq

V, E, P = map(int, input().split())
graph = [[] for _ in range(V+1)]
INF = float('inf')

def dijkstra(start):
    d = [INF] * (V+1)
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if d[now] < dist:
            continue

        for next, weight in graph[now]:
            new_dist = dist + weight
            if new_dist < d[next]:
                d[next] = new_dist
                heapq.heappush(q, (new_dist, next))

    return d

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 1 > V
d1 = dijkstra(1)
# P > V
dP = dijkstra(P)

if d1[V] == d1[P] + dP[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")