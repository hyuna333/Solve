T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    if H == 1:
        if N >= 10:
            ans = '1' + str(N)
        else:
            ans = '10' + str(N)
    else:
        if not N % H:
            floor = H
            room = N // H
        else:
            floor = N % H
            room = 1 + N // H

        if room >= 10:
            ans = str(floor) + str(room)
        else:
            ans = str(floor) + '0' + str(room)

    print(ans)
