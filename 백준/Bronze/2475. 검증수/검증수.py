lst = list(map(int, input().split()))

nums = list(x**2 for x in lst)

print(sum(nums)%10)