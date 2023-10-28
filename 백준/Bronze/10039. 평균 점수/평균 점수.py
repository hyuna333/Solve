import sys
input = sys.stdin.readline

sm = 0
for _ in range(5):
    num = int(input())
    if num < 40:
        sm += 40
    else:
        sm += num

print(sm // 5)