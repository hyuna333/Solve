import sys
N = int(sys.stdin.readline())

lst = []
for _ in range(N):
    a, b = sys.stdin.readline().split()
    lst.append((int(a), b))

ans = sorted(lst, key=lambda x : x[0])

for member in ans:
    print(member[0], member[1])