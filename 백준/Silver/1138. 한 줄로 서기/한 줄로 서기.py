import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
ki = {n:lst[n-1] for n in range(1, N+1)}

ans = [N]
for i in range(N-1, 0, -1):
    ans.insert(ki[i], i)

print(*ans)