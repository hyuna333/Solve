import sys
input = sys.stdin.readline

value = {'black':0, 'brown': 1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

num = ''
for _ in range(2):
    R = input().strip()
    num += str(value[R])

M = input().strip()
ans = int(num) * (10 ** value[M])
print(ans)