import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

s = 1
e = max(lst)
ans = 0

while s <= e:
    m = (s+e)//2
    tmp = 0

    for lan in lst:
        tmp += lan // m
        if tmp >= N:
            break

    if tmp >= N:
        s = m+1
        ans = m
    else:
        e = m-1

print(ans)