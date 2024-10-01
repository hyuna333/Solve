import sys
input = sys.stdin.readline

def consult(n, sm):
    global ans
    # 마지막날 패스
    if n == N:
        ans = max(ans, sm)
        return

    consult(n+1, sm)

    if n + date[n] <= N:
        consult(n+date[n], sm+cost[n])



N = int(input())
date = []
cost = []

for _ in range(N):
    T, P = map(int, input().split())
    date.append(T)
    cost.append(P)

ans = 0

consult(0, 0)

print(ans)

