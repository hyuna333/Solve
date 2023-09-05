N = int(input())
lst = list(map(int, input().split()))

ans = 0

def prime(num):
    global ans
    if num <= 1:
        return
    else:
        end = int(num**(1/2))
        for i in range(2, end+1):
            if not num % i:
              return
        ans += 1
        return

for n in lst:
    prime(n)

print(ans)