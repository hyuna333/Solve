import sys
input = sys.stdin.readline

N = int(input())

sm = 0
for _ in range(N):
    num = int(input())
    sm += num

print(sm - N + 1)