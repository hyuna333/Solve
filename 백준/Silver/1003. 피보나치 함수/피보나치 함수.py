import sys
input = sys.stdin.readline

T = int(input())
fibonacci = [[0, 0] for _ in range(41)]
fibonacci[0] = [1, 0]
fibonacci[1] = [0, 1]

for i in range(2, 41):
    fibonacci[i][0] = fibonacci[i-1][0] + fibonacci[i-2][0]
    fibonacci[i][1] = fibonacci[i-1][1] + fibonacci[i-2][1]

for _ in range(T):
    num = int(input())
    print(fibonacci[num][0], fibonacci[num][1])