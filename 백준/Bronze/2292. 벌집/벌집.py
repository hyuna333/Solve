N = int(input())

num = 1
ans = 1

while True:
    if N <= num:
        break
    num += 6 * ans
    ans += 1

print(ans)