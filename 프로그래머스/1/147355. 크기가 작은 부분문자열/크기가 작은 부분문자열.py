def solution(t, p):
    answer = 0
    
    for i in range(len(t)-len(p)+1):
        a = int(t[i:i+len(p)])
        b = int(p)
        if a <= b:
            answer += 1
            
    return answer