import sys
input = sys.stdin.readline

s = input().strip()

if s != s[::-1]:
    print(len(s))
elif len(set(s)) == 1:
    print(-1)
else:
    print(len(s) - 1)