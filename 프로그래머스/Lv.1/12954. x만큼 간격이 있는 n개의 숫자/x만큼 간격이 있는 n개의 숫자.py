def solution(x, n):
    answer = []
    a = x
    while n > 0:
        answer.append(a)
        a += x
        n -= 1
    return answer