import sys
input = sys.stdin.readline

def fac(n):
    if n <= 1:
        return 1
    else:
        return fac(n-1) * n

N, K = map(int, input().split())

ans = fac(N) // (fac(K) * fac(N - K))
print(ans)