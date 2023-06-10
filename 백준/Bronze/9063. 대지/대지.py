import sys

N = int(sys.stdin.readline())

si = sj = 10000
ei = ej = -10000

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a < si:
        si = a
    if a > ei:
        ei = a
    if b < sj:
        sj = b
    if b > ej:
        ej = b

print((ei-si)*(ej-sj))