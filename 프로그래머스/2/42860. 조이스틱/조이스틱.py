def solution(name):
    answer = 0
    lst = []
    n = len(name)
    
    for ch in name:
        if ch != "A":
            lst.append(min(ord(ch)-ord("A"), ord("Z")-ord(ch)+1))
        else:
            lst.append(0)
            
    answer = sum(lst)
    move = n - 1
    
    for i in range(n):
        ni = i+1
        while ni < n and name[ni] == "A":
            ni += 1
        
        move = min(move, 2 * i + (n-ni), 2 * (n-ni) + i)
                
    answer += move
    return answer