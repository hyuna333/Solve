import sys

lst = [0]*31

for _ in range(28):
    i = int(sys.stdin.readline())
    lst[i] += 1

for j in range(1, 31):
    if lst[j] == 0:
        print(j)