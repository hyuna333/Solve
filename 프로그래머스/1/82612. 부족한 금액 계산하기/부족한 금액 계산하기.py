def solution(price, money, count):
    answer = -1
    need = price * ((count * (count + 1) // 2))
    if money - need <= 0:
        answer = need - money
    else:
        answer = 0

    return answer