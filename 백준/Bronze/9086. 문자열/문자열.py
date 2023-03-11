import sys

T = int(sys.stdin.readline())

for _ in range(T):
    lst = list(sys.stdin.readline())
    ans = ''
    ans = lst[0] + lst[-2]
    print(ans)