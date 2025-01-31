import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
l = 0
r = max(lst) - min(lst)

while l <= r:
    m = (l+r)//2
    ci = 0
    asi = 0
    pa = 1
    cmx = cmn = lst[0]

    while ci < N:
        cmx = max(cmx, lst[ci])
        cmn = min(cmn, lst[ci])

        if cmx - cmn > m:
            pa += 1
            asi = ci
            cmx = lst[ci]
            cmn = lst[ci]
        else:
            ci += 1

    if pa > M:
        l = m + 1
    else:
        r = m - 1
        ans = m

print(ans)