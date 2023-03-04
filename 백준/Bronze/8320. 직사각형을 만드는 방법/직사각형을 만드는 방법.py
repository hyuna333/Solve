import sys
T = int(sys.stdin.readline())
N = int(T**(1/2))

sm = 0
for i in range(1, N+1):
    sm += T//i-(i-1)

print(sm)