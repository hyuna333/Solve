import sys
from collections import deque

N = int(sys.stdin.readline())

lst = deque(n for n in range(1, N+1))

while len(lst) > 1:
    lst.popleft()
    lst.append(lst.popleft())

print(lst[0])