def bfs(si, sj, n, m, vi, land, lst):
    q = [(si, sj)]
    vi[si][sj] = 1
    cnt = 1
    s = e = sj
    
    while q:
        ci, cj = q.pop(0)
        e = max(e, cj)
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and land[ni][nj] == 1 and vi[ni][nj] == 0:
                q.append((ni, nj))
                vi[ni][nj] = 1
                cnt += 1
    for i in range(s, e+1):
        lst[i] += cnt
    
    return cnt


def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    vi = [[0] * m for _ in range(n)]
    lst = [0] * m
    
    for i in range(m):
        tmp = 0
        
        for j in range(n):
            if land[j][i] and not vi[j][i]:
                tmp += bfs(j, i, n, m, vi, land, lst)
        answer = max(lst)

    return answer