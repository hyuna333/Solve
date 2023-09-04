N = int(input())

def fac(n):
    if n == 1:
        return n

    return n*fac(n-1)

if N != 0:
    num = fac(N)
    lst = list(str(num))
    
    ans = 0
    for i in range(len(lst)-1, -1 ,-1):
            if lst[i] != '0':
                break
            ans += 1
else:
    ans = 0
    
print(ans)

