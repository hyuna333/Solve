import sys

T = int(sys.stdin.readline())

for case in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{case}: {A} + {B} = {A+B}')

