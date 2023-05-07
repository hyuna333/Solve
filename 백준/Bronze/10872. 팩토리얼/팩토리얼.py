import sys

def fac(n):
    if n <= 1:
        return 1
    return fac(n-1)*n

N = int(sys.stdin.readline())

ans = fac(N)

print(ans)