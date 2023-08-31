nums = [int(input()) for _ in range(10)]

lst = []

for num in nums:
    lst.append(num%42)

lst = set(lst)
print(len(lst))