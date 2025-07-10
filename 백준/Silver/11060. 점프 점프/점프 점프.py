import sys
input = sys.stdin.readline

N = int(input())
miro = list(map(int, input().split()))
jump = [float("INF")]*N
jump[0] = 0

for i in range(N):
    for j in range(miro[i]):
        if i+j+1 >= N:
            break
        if jump[i+j+1] > jump[i] + 1:
            jump[i+j+1] = jump[i] + 1

if jump[-1] == float("INF"):
    print(-1)
else:
    print(jump[-1])