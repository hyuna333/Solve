def solution(x):
    answer = True
    sm = 0
    num = x
    
    while num >= 1:
        sm += num % 10
        num //= 10
    
    if x % sm:
        answer = False
    
    return answer