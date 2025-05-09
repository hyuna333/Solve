import sys

input = sys.stdin.readline

N, T = map(int, input().split())
L, R = [], []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)


low = max(L)
high = max(R)
answer = -1

while low <= high:
    mid = (low + high) // 2
    min_total = sum(L[i] for i in range(N))
    max_total = sum(min(R[i], mid) for i in range(N))

    if min_total <= T <= max_total:
        answer = mid
        high = mid - 1
    elif T < min_total:
        high = mid - 1
    else:
        low = mid + 1

print(answer)