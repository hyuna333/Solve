import sys

N = 9
sm = 0
lst = []

for _ in range(N):
    hi = int(sys.stdin.readline())
    sm += hi
    lst.append(hi)

for i in range(N-1):
    for j in range(i+1, N):
        ans = sm - lst[i] - lst[j]
        if ans == 100:
            lst.remove(lst[j])
            lst.remove(lst[i])
            break
    if len(lst) == 7:
        break

lst.sort()

for i in range(7):
    print(lst[i])