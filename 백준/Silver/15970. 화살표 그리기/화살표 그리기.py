import sys
input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(N+1)]
ans = 0

for _ in range(N):
    num, col = map(int, input().split())
    lst[col].append(num)

for nums in lst:
    nums.sort()
    if len(nums) > 1:
        ans += nums[1] - nums[0]
        ans += nums[-1] - nums[-2]
        for i in range(1, len(nums)-1):
            ans += min(nums[i]-nums[i-1], nums[i+1]-nums[i])

print(ans)
