import sys

N = int(sys.stdin.readline())
for _ in range(N):
    lst = list(sys.stdin.readline().rstrip())
    stk = []
    ans = 'YES'
    for i in lst:
        if i == '(':
            stk.append(i)
        elif stk and i == ')':
            stk.pop()
        else:
            ans = 'NO'
            break

    if stk:
        ans = 'NO'

    print(ans)

