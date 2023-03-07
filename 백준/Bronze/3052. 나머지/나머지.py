import sys
B = 42
lst = []
cnt = 0

for _ in range(10):
    A = int(sys.stdin.readline())
    C = A%B
    if C not in lst:
        lst.append(C)
        cnt += 1
        
print(cnt)