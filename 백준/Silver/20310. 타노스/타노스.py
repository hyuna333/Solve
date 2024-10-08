import sys
input = sys.stdin.readline

ze = one = 0
S = input()

for ch in S:
    if ch == '1':
        one += 1
    else:
        ze += 1

ans = '0' * (ze//2) + '1' * (one//2)
print(ans)

