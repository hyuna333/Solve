import sys
input = sys.stdin.readline

N = int(input())

sm = 0
for i in range(1, N+1):
    sm += i

sqsm = sm ** 2

tsqsm = 0
for j in range(1, N+1):
    tsqsm += j ** 3


print(sm)
print(sqsm)
print(tsqsm)