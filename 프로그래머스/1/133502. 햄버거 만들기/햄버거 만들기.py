def solution(ingredient):
    answer = 0
    
    lst = []
    for i in range(len(ingredient)):
        lst.append(ingredient[i])
        while True:
            if len(lst) >= 4 and lst[-4:] == [1, 2, 3, 1]:
                answer += 1
                del lst[-4:]
            else:
                break
        
    return answer