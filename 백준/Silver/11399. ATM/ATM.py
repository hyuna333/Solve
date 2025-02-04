import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0

while lst:
    tmp = lst.pop(0)
    ans += tmp * (len(lst)+1)

print(ans)