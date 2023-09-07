import sys
N = int(sys.stdin.readline())

a, b = map(int, sys.stdin.readline().split())

ans = [1 for _ in range(N)]
lst = [[a, b]]
for _ in range(N-1):
    W, H = map(int, sys.stdin.readline().split())
    lst.append([W, H])

    for i in range(len(lst)-1):
        if lst[i][0] > W and lst[i][1] > H:
            ans[len(lst) - 1] += 1
        elif lst[i][0] < W and lst[i][1] < H:
            ans[i] += 1

print(*ans)