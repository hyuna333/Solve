import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

mx = cmx = lst[0]

for num in lst[1:]:
    cmx = max(num, cmx + num)
    mx = max(mx, cmx)

print(mx)
