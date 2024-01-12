def solution(n):
    answer = 0
    r = n ** 0.5
    if int(r) == r:
        answer = int((r + 1) ** 2)
    else:
        answer = -1
    return answer