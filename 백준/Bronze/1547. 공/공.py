import sys
input = sys.stdin.readline

M = int(input())

ans = 1
for _ in range(M):
    X, Y = map(int, input().split())
    if X == Y:
        pass
    elif X == ans:
        ans = Y
    elif Y == ans:
        ans = X

print(ans)