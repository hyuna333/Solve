def solution(s):
    answer = True
    q = []
    
    for st in s:
        if st == '(':
            q.append(st)
        else:
            if q:
                q.pop(-1)
            else:
                answer = False
                break
    
    if q:
        answer = False

    return answer