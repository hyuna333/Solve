import sys
input = sys.stdin.readline
from collections import deque


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


T = int(input())
for _ in range(T):
    ans = 'sad'
    N = int(input())
    home = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(N)]
    festival = tuple(map(int, input().split()))

    q = deque()
    q.append(home)
    vi = [False] * N

    while q:
        c = q.popleft()
        if distance(c, festival) <= 1000:
            ans = "happy"
            break

        for i in range(N):
            if not vi[i] and distance(c, stores[i]) <= 1000:
                vi[i] = True
                q.append(stores[i])

    print(ans)