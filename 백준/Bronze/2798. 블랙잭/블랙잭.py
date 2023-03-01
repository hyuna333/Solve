import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

mx = 0
sm = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sm += lst[i]+lst[j]+lst[k]
            if mx < sm <= M:
                mx = sm
            sm = 0
            
print(mx)