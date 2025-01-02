import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = []
    A.sort()
    B.sort()

    j = 0
    for num in A:
        while j + 1 < m and abs(B[j+1] - num) < abs(B[j] - num):
            j += 1
        C.append(B[j])

    print(sum(C))