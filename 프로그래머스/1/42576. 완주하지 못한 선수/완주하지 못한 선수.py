def solution(participant, completion):
    answer = ''
    
    dct = {}
    for e in completion:
        if e in dct:
            dct[e] += 1
        else:
            dct[e] = 1
            
    for p in participant:
        if p in dct and dct[p] > 0:
            dct[p] -= 1
        else:
            answer = p
            break
            
    return answer