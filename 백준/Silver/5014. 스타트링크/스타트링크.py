import sys
input = sys.stdin.readline
from collections import deque


def ele(s):
    q = deque([s])
    vi[s] = 1

    while q:
        c = q.popleft()

        if c == G:
            return

        if c+U <= F and not vi[c+U]:
            q.append(c+U)
            vi[c+U] = vi[c] + 1

        if c-D > 0 and not vi[c-D]:
            q.append(c-D)
            vi[c-D] = vi[c] + 1


F, S, G, U, D = map(int, input().split())

q = deque([S])
vi = [0]*(F+1)
ele(S)

if vi[G]:
    print(vi[G]-1)
else:
    print("use the stairs")