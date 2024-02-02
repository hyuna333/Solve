import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dct = {n:0 for n in range(N)}
co = [[] for _ in range(N+1)]
for _ in range(N):
    c, *lst = map(int, input().split())
    co[c] = lst

ans = 1
for i in range(1, N+1):
    if i == K:
        continue
    g, s, b = co[K]
    if co[i][0] > g:
        ans += 1
    elif co[i][0] == g and co[i][1] > s:
        ans += 1
    elif co[i][0] == g and co[i][1] == s and co[i][2] > b:
        ans += 1

print(ans)