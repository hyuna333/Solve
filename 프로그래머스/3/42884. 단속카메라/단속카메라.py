def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x : x[1])
    
    tmp = -30001
    for route in routes:
        if route[0] <= tmp <= route[1]:
            continue
        
        tmp = route[1]
        answer += 1
    
    return answer