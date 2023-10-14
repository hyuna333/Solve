import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
mx = 0
for i in range(N):
    money = int(input())
    if money > K:
        break

    lst.append(money)

ans = 0
for i in range(len(lst)-1, -1, -1):
    if K == 0:
        break
    num = K // lst[i]
    ans += num
    K -= num * lst[i]

print(ans)