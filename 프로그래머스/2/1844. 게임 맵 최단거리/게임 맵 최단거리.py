def dis(i, j, n, m, maps):
    q = [(i, j)]
    vi = [[0]*m for _ in range(n)]
    vi[i][j] = 1
    
    while q:
        ci, cj = q.pop(0)
        if (ci, cj) == (n-1,m-1):
            return vi[ci][cj]
        
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1 and vi[ni][nj] == 0:
                q.append((ni,nj))
                vi[ni][nj] = vi[ci][cj] + 1
    return -1


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    answer = dis(0,0,n,m,maps)
    
    
    return answer