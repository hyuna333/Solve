import sys

T = int(sys.stdin.readline())

for case in range(1, T+1):
    print(' '*(T-case)+'*'*case)
