import sys
input = sys.stdin.readline

N = int(input())
rope = [int(input()) for _ in range(N)]
ans = 0

rope.sort(reverse=True)

for i in range(N):
    ans = max(ans, rope[i]*(i+1))

print(ans)