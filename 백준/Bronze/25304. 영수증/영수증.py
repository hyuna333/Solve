X = int(input())
N = int(input())
sm = 0

for _ in range(N):
    a, b = map(int, input().split())
    sm += a*b

ans = 'No'
if sm == X: ans = 'Yes'

print(ans)