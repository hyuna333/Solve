while True:
    N = int(input())

    if N == 0:
        break

    lst = list(str(N))

    n = len(lst) // 2

    ans = 'yes'

    for i in range(n):
        if lst[i] != lst[-1-i]:
            ans = 'no'
            break

    print(ans)
