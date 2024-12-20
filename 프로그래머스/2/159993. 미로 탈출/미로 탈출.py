def miro(si, sj, ei, ej, maps):
    q = [(si, sj)]
    n = len(maps)
    m = len(maps[0])
    vi = [[0] * m for _ in range(n)]
    vi[si][sj] = 1

    while q:
        ci, cj = q.pop(0)

        if (ci, cj) == (ei, ej):
            return vi[ei][ej] - 1

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] != "X" and not vi[ni][nj]:
                q.append((ni, nj))
                vi[ni][nj] = vi[ci][cj] + 1

    return -1


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    si = sj = -1
    li = lj = -1
    ei = ej = -1

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                si, sj = i, j
            if maps[i][j] == "L":
                li, lj = i, j
            if maps[i][j] == "E":
                ei, ej = i, j

    lever = miro(si, sj, li, lj, maps)
    if lever == -1:
        return -1
    
    ed = miro(li, lj, ei, ej, maps)
    if ed == -1:
        return -1

    answer = lever + ed
    return answer