import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

if N == 1:
    print(sum(nums) - max(nums))
else:
    three = min(nums[0] + nums[1] + nums[2],
                nums[0] + nums[1] + nums[3],
                nums[0] + nums[2] + nums[4],
                nums[0] + nums[3] + nums[4],
                nums[1] + nums[2] + nums[5],
                nums[1] + nums[3] + nums[5],
                nums[2] + nums[4] + nums[5],
                nums[3] + nums[4] + nums[5])

    two = min(nums[0] + nums[1], nums[0] + nums[2], nums[0] + nums[3],
              nums[0] + nums[4], nums[1] + nums[5], nums[2] + nums[5],
              nums[3] + nums[5], nums[4] + nums[5], nums[1] + nums[3],
              nums[1] + nums[2], nums[2] + nums[4], nums[3] + nums[4])

    one = min(nums)

    a = 4 * three
    b = (4 * (N-2) + 4 * (N-1)) * two
    c = ((N-2)**2 + 4 * (N-2) * (N-1)) * one
    ans = a + b + c

    print(ans)
