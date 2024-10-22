def link(s, computers):
    global vi
    q = [s]
    vi[s] = 1
    cnt = 1
    while q:
        c = q.pop(0)
        for i in range(len(computers)):
            if computers[c][i] == 1 and not vi[i]:
                vi[i] = 1
                cnt += 1
                q.append(i)
    return

def solution(n, computers):
    global vi
    answer = 0
    vi = [0] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not vi[j]:
                link(j, computers)
                answer += 1
    
    return answer