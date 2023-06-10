import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

lst.sort()

def func(x):
    s = 0
    e = N-1
    while s <= e:
        mid = (s+e)//2
        if lst[mid] == x:
            return 1
        elif lst[mid] < x:
            s = mid+1
        else:
            e = mid-1
    return 0


for num in find:
    print(func(num))

