import sys
input = sys.stdin.readline

def Z(n, r, c):
    if n == 0:
        return 0

    ban = 2 ** (n-1)

    if r < ban and c < ban:
        return Z(n-1, r, c)
    elif r < ban and c >= ban:
        return ban**2 + Z(n-1, r, c-ban)
    elif r >= ban and c < ban:
        return 2 * ban**2 + Z(n-1, r-ban, c)
    else:
        return 3 * ban**2 + Z(n-1, r-ban, c-ban)

N, r, c = map(int, input().split())
print(Z(N, r, c))