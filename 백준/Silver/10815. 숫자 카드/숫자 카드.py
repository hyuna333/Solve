import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    s = 0
    e = N-1
    while s<=e:
        m = (s+e)//2
        if A[m] == B[i]:
            print(1, end= ' ')
            break
        elif A[m] > B[i]:
            e = m-1
        elif A[m] < B[i]:
            s = m+1
    else:
        print(0, end=' ')
