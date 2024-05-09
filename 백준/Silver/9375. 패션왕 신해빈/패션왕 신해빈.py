import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    dct = {}
    n = int(input())
    for _ in range(n):
        name, where = input().split()
        if where in dct:
            dct[where] += 1
        else:
            dct[where] = 1

    ans = 1
    for num in dct.values():
        ans *= num + 1

    ans -= 1

    print(ans)


