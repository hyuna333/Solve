import sys
input = sys.stdin.readline

N = int(input())

que = []
for _ in range(N):
    st = list(input().split())
    if st[0] == "push":
        que.append(int(st[1]))
    elif st[0] == "pop":
        if que:
            print(que.pop(0))
        else:
            print(-1)
    elif st[0] == "size":
        print(len(que))
    elif st[0] == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif st[0] == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)