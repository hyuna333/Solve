import sys
input = sys.stdin.readline

H, M, S = map(int, input().split())
N = int(input())

hour = N // 3600
minute = (N - 3600 * hour) // 60
second = N - (3600 * hour) - (60 * minute)

H += hour
M += minute
S += second

if S >= 60:
    M += S // 60
    S %= 60

if M >= 60:
    H += M // 60
    M %= 60

if H >= 24:
    H %= 24


print(H, M, S)