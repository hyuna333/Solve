import sys
input = sys.stdin.readline

import heapq
heap = []
N = int(input())

for _ in range(N):
    num = int(input())
    if not num:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)
