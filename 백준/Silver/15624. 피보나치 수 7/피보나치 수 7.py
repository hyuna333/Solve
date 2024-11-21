import sys
input = sys.stdin.readline

n = int(input())

a, b = 0, 1  

for _ in range(2, n + 1):
    a, b = b, (a + b) % 1000000007

print(b)