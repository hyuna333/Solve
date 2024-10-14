import sys
input = sys.stdin.readline

N = int(input())
ans = 10000
sell = {}
buy = {}

def market(price, quantity, stock, other_stock):
    global ans

    # 재고가 있을 경우
    if stock.get(price):
        ans = price
        if quantity > stock[price]:
            if other_stock.get(price):
                other_stock[price] += quantity - stock[price]
            else:
                other_stock[price] = quantity - stock[price]
            stock[price] = 0
        else:
            stock[price] -= quantity
    else:
        if other_stock.get(price):
            other_stock[price] += quantity
        else:
            other_stock[price] = quantity

for _ in range(N):
    p, x, f = map(int, input().split())

    # 판매
    if f == -1:
        market(p, x, sell, buy)
    # 구매
    else:
        market(p, x, buy, sell)

print(ans)
