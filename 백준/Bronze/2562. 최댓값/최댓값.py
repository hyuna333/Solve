lst = [int(input()) for _ in range(9)]

mx = max(lst)
ans = 0

for i in range(9):
    if lst[i] == mx:
        ans = i+1
        break

print(mx)
print(ans)