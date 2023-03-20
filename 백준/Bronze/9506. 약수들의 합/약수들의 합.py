import sys

while True:
    N = int(sys.stdin.readline())
    if N == -1:
        break
    else:
        ans = '1'
        sm = 1
        for i in range(2, N):
            if N%i == 0:
                ans += ' + ' + str(i)
                sm += i

        if sm == N:
            print(f'{N} = {ans}')
        else:
            print(f'{N} is NOT perfect.')
