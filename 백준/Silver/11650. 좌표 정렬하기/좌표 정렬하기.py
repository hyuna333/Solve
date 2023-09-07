import sys
N = int(sys.stdin.readline())

lst = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    lst.append((a, b))

ans = sorted(lst)

for spot in ans:
    print(spot[0], spot[1])