import sys

mx = 0
mx_idx = 0
for i in range(1, 10):
    N = int(sys.stdin.readline())
    if mx < N:
        mx = N
        mx_idx = i

print(mx)
print(mx_idx)
