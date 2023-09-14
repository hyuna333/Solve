import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())

    sm = 0

    for _ in range(N):
        num = int(input())
        sm += num

    if sm == 0:
        print(0)
    elif sm > 0 :
        print('+')
    else:
        print('-')