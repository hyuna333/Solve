import sys
T = int(sys.stdin.readline())

for _ in range(T):
    lst = list(sys.stdin.readline())
    cnt = sm = 0
    for st in lst:
        if st == 'O':
            cnt += 1
            sm += cnt
        else:
            cnt = 0

    print(sm)