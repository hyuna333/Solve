def bfs(si, sj, n, m, vi, land):
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

    return cnt, s, e


def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    lst = [0] * m
    vi = [[0] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            if land[j][i] and not vi[j][i]:
                cnt, s, e = bfs(j, i, n, m, vi, land)
                for k in range(s, e + 1):
                    lst[k] += cnt
        answer = max(lst)

    return answer