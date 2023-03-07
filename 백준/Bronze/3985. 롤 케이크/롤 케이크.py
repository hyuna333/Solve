import sys

L = int(sys.stdin.readline())
N = int(sys.stdin.readline())
cake = [0]*(L+1)
cnt = [0]*(N+1)
mx = 0

for i in range(1, N+1):
    s, e = map(int, sys.stdin.readline().split())
    ex = e-s
    if mx < ex:
        mx = ex
        mx_idx = i

    for j in range(s, e+1):
        if cake[j] == 0:
            cake[j] = i
            cnt[i] += 1

real = 0
for k in range(N+1):
    if real < cnt[k]:
        real = cnt[k]
        real_idx = k

print(mx_idx)
print(real_idx)