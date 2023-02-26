import sys

N, M, L = map(int, sys.stdin.readline().split())
lst = [0]*N

# 시작 세팅
s = 0
lst[s] += 1
cnt = 0

while lst[s] < M:
    # 홀수라면 시계방향으로 L만큼 이동
    if lst[s]%2:
        s = (s+L)%N
        lst[s] += 1
        cnt += 1
    # 짝수라면 반시계반향으로 L만큼 이동
    else:
        if s < L:
            s = s+N-L
        else:
            s = s-L
        lst[s] += 1
        cnt += 1

print(cnt)

