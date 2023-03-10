import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

mx = max(score)
sm = 0

for i in score:
    i = i/mx*100
    sm += i

avg = sm/N

print(avg)

