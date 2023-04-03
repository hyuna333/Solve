import sys

A, B, V = map(int, sys.stdin.readline().split())

ans = (V-B)//(A-B)
if (V-B)%(A-B):
    ans += 1
    
print(ans)