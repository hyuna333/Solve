import sys

M, N = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
ga = [0]*(N+1)
se = [0]*(M+1)

for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    if a == 0:
        ga[b] = 1
    else:
        se[b] = 1

now_g = mx_g = 0
for i in range(N+1):
    if ga[i] == 1 or i == N:
        if mx_g < i-now_g:
            mx_g = i- now_g
        now_g = i

now_s = mx_s = 0
for i in range(M+1):
    if se[i] == 1 or i == M:
        if mx_s < i-now_s:
            mx_s = i- now_s
        now_s = i

print(mx_g*mx_s)