import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
ans = -1

if sum(lst) <= M:
    ans = max(lst)
else:
    s, e = 0, max(lst)

    while s <= e:
        mid = (s+e)//2
        tmp = 0

        for num in lst:
            tmp += min(num, mid)

        if tmp <= M:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1

print(ans)