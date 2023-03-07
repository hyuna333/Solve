import sys

N = int(sys.stdin.readline())
dct = {'4':0, '3':1, '2':2, '1':3}

for _ in range(N):
    A = list(sys.stdin.readline().split())
    B = list(sys.stdin.readline().split())
    a = A.pop(0)
    b = B.pop(0)
    cnt_A = [0]*4
    cnt_B = [0]*4

    for i in A:
        cnt_A[dct[i]] += 1
    for i in B:
        cnt_B[dct[i]] += 1

    ans = 'D'
    for i in range(4):
        if cnt_A[i] > cnt_B[i]:
            ans = 'A'
            break
        elif cnt_B[i] > cnt_A[i]:
            ans = 'B'
            break

    print(ans)