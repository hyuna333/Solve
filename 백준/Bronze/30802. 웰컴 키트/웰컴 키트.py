import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

T, P = map(int, input().split())
ts = 0
sm = sum(nums)
for num in nums:
    ts += ((num-1) // T) + 1
print(ts)
print(sm//P, sm%P)