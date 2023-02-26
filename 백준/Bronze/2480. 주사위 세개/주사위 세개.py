dice = list(map(int, input().split()))

lst = [0]*7

for i in dice:
    lst[i] += 1

mx = mx_idx = 0
for i in range(7):
    if mx <= lst[i]:
        mx = lst[i]
        mx_idx = i

ans = 0
if mx == 3:
    ans = 10000+1000*mx_idx
elif mx == 2:
    ans = 1000+100*mx_idx
else:
    ans = 100*mx_idx

print(ans)

