import sys

N = int(sys.stdin.readline())

lst = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    lst[num] += 1

for i in range(len(lst)):
    if lst[i]:
        for _ in range(lst[i]):
            print(i)