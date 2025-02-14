import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

s, e = 0, N-1
ans = float('inf')

while s < e:
    tmp = lst[s] + lst[e]

    if abs(ans) > abs(tmp):
        ans = tmp
    if tmp == 0:
        break

    if tmp < 0:
        s += 1
    else:
        e -= 1

print(ans)