T = int(input())

for _ in range(T):
    N, *lst = map(int, input().split())
    lst = list(lst)
    sm = sum(lst)
    avg = sm/N

    i = 0
    for score in lst:
        if score > avg:
            i += 1

    ans = round(i/N*100, 3)

    print('{0:.3f}%'.format(ans))