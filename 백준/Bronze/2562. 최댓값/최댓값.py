lst = [int(input()) for _ in range(9)]

mx = max(lst)

for i in range(9):
    if lst[i] == mx:
        print(mx)
        print(i+1)
        break