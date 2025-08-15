import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))

if N == 0:
    print(0)
else:
    ans = 1
    rest = M
    for book in books:
        if rest - book >= 0:
            rest -= book
        else:
            ans += 1
            rest = M - book

    print(ans)