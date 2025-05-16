import sys
input = sys.stdin.readline
from collections import deque

S = int(input())
vi = [[False] * (S + 1) for _ in range(S + 1)]

q = deque()
q.append((1, 0, 0))
vi[1][0] = True


while q:
    l, c, t = q.popleft()

    if l == S:
        print(t)
        break

    # 복사
    if not vi[l][l]:
        vi[l][l] = True
        q.append((l, l, t + 1))

    # 붙여넣기
    if c > 0 and l + c <= S and not vi[l + c][c]:
        vi[l + c][c] = True
        q.append((l + c, c, t + 1))

    # 삭제
    if l > 1 and not vi[l - 1][c]:
        vi[l - 1][c] = True
        q.append((l - 1, c, t + 1))