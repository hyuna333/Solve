import sys
input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
ans = 1
mn = 5

if N == 1:
    print(1, min(G[0]))
else:
    for grade in range(1, 6):
        s = e = 0
        while e < N:
            if grade in G[e]:
                e += 1
            else:
                s = e = e + 1

            tmp = e - s
            if tmp > ans:
                ans = tmp
                mn = int(grade)
            elif tmp == ans:
                mn = min(mn, int(grade))

    print(ans, mn)