lst = [int(input()) for _ in range(3)]

num = lst[0]*lst[1]*lst[2]

num = str(num)

dct = {str(i):0 for i in range(10)}

for i in num:
    dct[i] += 1

for j in dct.values():
    print(j)