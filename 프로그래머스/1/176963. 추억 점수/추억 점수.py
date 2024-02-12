def solution(name, yearning, photo):
    answer = []
    dct = {name[i] : yearning[i] for i in range(len(name))}
    for lst in photo:
        sm = 0
        for pp in lst:
            if pp in dct:
                sm += dct[pp]
        answer.append(sm)
    return answer