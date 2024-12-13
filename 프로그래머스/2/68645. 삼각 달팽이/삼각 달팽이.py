def solution(n):
    answer = []
    tmp = [[0]*(i+1) for i in range(n)]
    lm = (n*(n+1))//2
    num = n
    now = 1
    
    idx = -1
    idy = 0
    # 아래, 옆, 위
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    di = 0
    
    while now <= lm:
        for _ in range(num):
            idx += dx[di]
            idy += dy[di]
            tmp[idx][idy] = now
            now += 1
        di = (di+1)%3
        num -= 1
    
    answer = [l for lst in tmp for l in lst]
        
    return answer