import sys
input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)
else:
    lst = []
    for _ in range(N):
        num = int(input())
        lst.append(num)

    lst.sort()
    noin = int(N * 0.15 + 0.5)

    newlst = lst[noin:N-noin]

    avg = int(sum(newlst) / len(newlst) + 0.5)

    print(avg)