import sys

P = int(sys.stdin.readline())
for _ in range(P):
    case, *lst = map(int, sys.stdin.readline().split())
    stk = []
    ans = 0
    for i in range(len(lst)):
        if not stk:
            stk.append(lst[i])
        else:
            if stk[-1] <= lst[i]:
                stk.append(lst[i])
            else:
                for j in range(i):
                    if stk[j] > lst[i]:
                        ans += i-j
                        stk.insert(j, lst[i])
                        break
                        
    print(f'{case} {ans}')