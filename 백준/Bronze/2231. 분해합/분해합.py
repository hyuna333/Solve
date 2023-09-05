N = int(input())

ans = 0
for num in range(1, N+1):
    sm = num + sum(map(int, str(num)))

    if sm == N:
        ans = num
        break

print(ans)