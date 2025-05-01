import sys
input = sys.stdin.readline
from collections import defaultdict, deque

city = defaultdict(list)

for line in sys.stdin:
    if line.strip() == '':
        break
    a, b, d = map(int, line.strip().split())
    city[a].append((b,d))
    city[b].append((a,d))

def br(s):
    vi = {}
    q = deque()
    q.append((s, 0))
    vi[s] = 0
    mxn = s
    mx = 0

    while q:
        c, d = q.popleft()
        if d > mx:
            mxn = c
            mx = d

        for n, nd in city[c]:
            if n not in vi:
                vi[n] = d + nd
                q.append((n, d + nd))

    return mxn, mx

nx, _ = br(1)
_, ans = br(nx)
print(ans)