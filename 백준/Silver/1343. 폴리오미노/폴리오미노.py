import sys
input = sys.stdin.readline

lst = list(input().strip())
tmp = 0
ans = ''

def check(tmp):
    global ans
    if tmp % 2:
        ans = -1
        return
    else:
        if tmp // 4 > 0:
            ans += 'AAAA' * (tmp // 4)
            if tmp % 4:
                ans += 'BB'
        else:
            ans += 'BB'

for i in range(len(lst)):
    if lst[i] == "X":
        tmp += 1
    else:
        if tmp > 0:
            check(tmp)
        if ans == -1:
            tmp = 0
            break
        ans += '.'
        tmp = 0

if ans != -1 and tmp:
    check(tmp)
print(ans)