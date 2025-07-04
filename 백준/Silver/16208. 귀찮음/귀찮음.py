import sys
input = sys.stdin.readline

N = int(input())
sticks = list(map(int, input().split()))
sticks.sort()
ans = 0

while len(sticks) > 1:
    a = sticks.pop(-1)
    b = sticks.pop(-1)
    ans += a * b
    sticks.append(a+b)

print(ans)