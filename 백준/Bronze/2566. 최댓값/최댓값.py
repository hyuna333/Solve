import sys

mx = 0
mx_i = mx_j = 1

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if mx < arr[i][j]:
            mx = arr[i][j]
            mx_i, mx_j = i+1, j+1

print(mx)
print(mx_i, mx_j)