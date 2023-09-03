while True:
    lst = list(map(int, input().split()))

    if not lst[0]:
        break

    lst.sort()

    ans = 'wrong'

    if lst[2] ** 2 == lst[0] ** 2 + lst[1] ** 2:
        ans = 'right'

    print(ans)