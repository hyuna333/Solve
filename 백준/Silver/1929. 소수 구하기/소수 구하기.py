import math
import sys
input = sys.stdin.readline

def primeNum(num):
    lst = [True] * (num + 1)
    lst[0] = lst[1] = False

    for i in range(2, int(math.sqrt(num))+1):
        if lst[i] == True:
            j = 2
            while i * j <= num:
                lst[i * j] = False
                j += 1
    
    return [i for i in range(2, num + 1) if lst[i]]

M, N = map(int, input().split())

ans = primeNum(N)
for num in ans:
    if num >= M:
        print(num)