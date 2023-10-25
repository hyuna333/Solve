import sys
input = sys.stdin.readline

sm = 0
mn = 100
for _ in range(7):
    num = int(input())
    if num % 2:
        sm += num
        mn = min(mn, num)

if sm == 0:
    print(-1)
else:
    print(sm)
    print(mn)