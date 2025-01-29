import sys
input = sys.stdin.readline
import heapq

N = int(input())
h = []

for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        heapq.heappush(h, num)
        if len(h) > N:
            heapq.heappop(h)

print(h[0])