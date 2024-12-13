from collections import defaultdict

def solution(n, words):
    answer = []
    dct = defaultdict(int)
    bf = ""
    
    for i in range(len(words)):
        if i == 0:
            dct[words[i]] += 1
            bf = words[i]
            continue
        
        # 중복단어이거나 끝말잇기 아니면 실패
        if dct[words[i]] == 1 or bf[-1] != words[i][0]:
            answer.append(i%n + 1)
            answer.append(i//n + 1)
            break
        else:
            bf = words[i]
            dct[words[i]] += 1
    
    if answer == []:
        answer = [0, 0]
    return answer