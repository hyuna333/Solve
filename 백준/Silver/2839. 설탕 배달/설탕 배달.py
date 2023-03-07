import sys

N = int(sys.stdin.readline())

A = C = N//5
B = (N-A*5)//3
ans = -1

if A*5 + B*3 == N:
    ans = A+B
else:
    for i in range(1, C+1):
        A -= 1
        B = (N-A*5)//3
        if A * 5 + B * 3 == N:
            ans = A + B
            break

print(ans)