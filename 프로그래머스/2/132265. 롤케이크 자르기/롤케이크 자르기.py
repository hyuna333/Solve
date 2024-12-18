from collections import Counter

def solution(topping):
    answer = 0
    l = set()
    r = Counter(topping)
    
    for t in topping:
        l.add(t)
        r[t] -= 1
        
        if r[t] == 0:
            del r[t]
        
        if len(l) == len(r):
            answer += 1
    
    return answer