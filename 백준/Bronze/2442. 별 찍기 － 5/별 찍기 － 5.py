import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    print(' ' * (N-1-i), end='')
    print('*' * (2*i+1), end='')
    print()
