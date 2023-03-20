import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in lst:
    check = 0
    if i == 1:
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                check += 1
                break
        if not check:
            cnt += 1

print(cnt)
