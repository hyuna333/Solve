import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int, input().split()))

i = 0
vi = [0]*N
print(i+1, end=' ')
vi[i] = 1
while True:
    if sum(vi) == N:
        break

    step = lst[i]
    if step > 0:
        while step > 0:
            i = (i+1)%N
            if vi[i] == 0:
                step -= 1
    else:
        while step < 0:
            i = (i-1)%N
            if vi[i] == 0:
                step += 1

    print(i+1, end=' ')
    vi[i] = 1
