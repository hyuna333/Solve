lst = list(map(int, input().split()))

ans = 'mixed'

if lst == sorted(lst):
    ans = 'ascending'
elif lst == sorted(lst, reverse=True):
    ans = 'descending'

print(ans)