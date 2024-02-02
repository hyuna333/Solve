import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
money = {0:0, 1:A, 2:B * 2, 3:C * 3}
time = [0] * 101
mn = 100
mx = 1

for i in range(3):
    s, e = map(int, input().split())
    for j in range(s, e):
        time[j] += 1
    mn = min(mn, s)
    mx = max(mx, e-1)

sm = 0
for m in range(mn, mx+1):
    sm += money[time[m]]

print(sm)