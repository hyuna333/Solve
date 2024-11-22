import sys
from collections import deque
input = sys.stdin.readline

def mount():
    q = deque([(0, 0)])
    vi[(0,0)] = 0

    while q:
        cx, cy = q.popleft()
        if cy == T:
            return vi[(cx,cy)]

        for i in range(-2, 3):
            for j in range(-2, 3):
                nx, ny = cx + i, cy + j
                if (nx, ny) in lst and (nx, ny) not in vi:
                    vi[(nx,ny)] = vi[(cx,cy)] + 1
                    q.append((nx, ny))
                    lst.remove((nx,ny))
    return -1


n, T = map(int, input().split())
lst = set(tuple(map(int, input().split())) for _ in range(n)) 

vi = {}
ans = mount()
print(ans)