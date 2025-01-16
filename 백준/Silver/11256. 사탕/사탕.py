import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    J, N = map(int, input().split())
    box = []
    for i in range(N):
        R, C = map(int, input().split())
        box.append(R*C)

    box.sort(reverse=True)

    for j in range(N):
        if sum(box[:j+1]) >= J:
            print(j+1)
            break