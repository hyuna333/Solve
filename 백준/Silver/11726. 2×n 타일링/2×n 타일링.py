import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    ans = 1
elif n == 2:
    ans = 2
else:
    tile = [0] * n
    tile[0] = 1
    tile[1] = 2

    for i in range(2, n):
        tile[i] = tile[i-2] + tile[i-1]

    ans = tile[n-1]

print(ans % 10007)

