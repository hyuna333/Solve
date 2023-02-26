N = int(input())
repeat = N//4

ans = ''
for _ in range(repeat):
    ans += 'long '

ans += 'int'

print(ans)