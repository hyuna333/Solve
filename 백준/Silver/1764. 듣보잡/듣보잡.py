import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nohear = {}
both = []

for _ in range(N):
    name = input().strip()
    nohear[name] = 1

for _ in range(M):
    name = input().strip()
    if nohear.get(name):
        both.append(name)

both.sort()

print(len(both))
for pp in both:
    print(pp)