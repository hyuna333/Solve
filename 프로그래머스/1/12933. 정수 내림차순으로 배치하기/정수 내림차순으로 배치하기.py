def solution(n):
    answer = 0
    lst = []
    while n >= 1:
        lst.append(n % 10)
        n //= 10
    lst.sort(reverse=True)
    answer = int(''.join(str(x) for x in lst))
    return answer