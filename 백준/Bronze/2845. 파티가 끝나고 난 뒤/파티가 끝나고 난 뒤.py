import sys
input = sys.stdin.readline

L, P = map(int, input().split())

nums = list(map(int, input().split()))

pp = L * P

for num in nums:
    print(num - pp, end=' ')