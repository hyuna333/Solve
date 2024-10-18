import sys
input = sys.stdin.readline

def start(n, alst, blst, N):
    global ans

    if n == N:
        if len(alst) == N // 2:
            asm = bsm = 0
            for i in range(len(alst)):
                for j in range(len(alst)):
                    asm += arr[alst[i]][alst[j]]
                    bsm += arr[blst[i]][blst[j]]
            ans = min(ans, abs(asm-bsm))
        return

    start(n+1, alst + [n], blst, N)
    start(n+1, alst, blst + [n], N)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 9 * N * N
start(0, [], [], N)

print(ans)
