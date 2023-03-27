import sys

x, y, w, h = map(int, sys.stdin.readline().split())
lst = [x, y, w-x, h-y]

mn = lst[0]

for num in lst:
    if mn > num:
        mn = num

print(mn)