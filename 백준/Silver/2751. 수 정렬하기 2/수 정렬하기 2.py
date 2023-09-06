import sys
N = int(sys.stdin.readline())

lst = []
for _ in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)
    
lst.sort()

for n in lst:
    print(n)