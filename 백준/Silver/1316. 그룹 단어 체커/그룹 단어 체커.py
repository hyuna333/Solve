import sys

M = int(sys.stdin.readline())
ans = M

for _ in range(M):
    N = sys.stdin.readline()
    stk = []

    for st in N:
        if st not in stk:
            stk.append(st)
        else:
            if st != stk[-1]:
                ans -= 1
                break

print(ans)