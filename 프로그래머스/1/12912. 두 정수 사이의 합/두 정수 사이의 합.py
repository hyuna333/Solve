def solution(a, b):
    answer = 0
    
    if a == b:
        answer = a
    elif a > b:
        answer = ((a * (a+1)) // 2) - ((b * (b-1)) // 2)
    else:
        answer = ((b * (b+1)) // 2) - ((a * (a-1)) // 2)
    return answer