def solution(array, commands):
    answer = []
    for lst in commands:
        s = lst[0]
        e = lst[1]
        i = lst[2]
        tmp = array[s-1:e]
        tmp.sort()
        answer.append(tmp[i-1])
    return answer