import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    M = int(sys.stdin.readline())
    if not lst:
        lst.append(M)
    else:
        for i in range(len(lst)):
            if lst[i] >= M:
                lst.insert(i, M)
                break
        else:
            lst.append(M)

for num in lst:
    print(num)