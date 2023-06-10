import sys

def func(N, n):
    global ans

    if n > ans:
        return
    if N == 1:
        ans = min(ans, n)
        return

    if N % 3 == 0:
        func(N//3, n+1)
    if N % 2 == 0:
        func(N//2, n+1)
    func(N-1, n+1)


N = int(sys.stdin.readline())

ans = 100000000
func(N, 0)

print(ans)
