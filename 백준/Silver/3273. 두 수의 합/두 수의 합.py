import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
X = int(input())

lst.sort()
ans = 0

s = 0
e = N - 1

while s < e:
    sm = lst[s] + lst[e]

    if sm == X:
        ans += 1
        s += 1
        e -= 1
    elif sm < X:
        s += 1
    else:
        e -= 1
        
print(ans)