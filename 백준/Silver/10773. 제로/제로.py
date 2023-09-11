import sys

K = int(sys.stdin.readline())

lst = []
for _ in range(K):
    num = int(sys.stdin.readline())

    if num == 0:
        lst.pop()
    else:
        lst.append(num)

print(sum(lst))