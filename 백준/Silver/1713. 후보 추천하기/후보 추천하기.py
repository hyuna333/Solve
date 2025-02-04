import sys
input = sys.stdin.readline
import heapq
from collections import deque

N = int(input())
C = int(input())
reco = list(map(int, input().split()))

# {번호: [추천수, 시간]}
photo = {}
q = deque()
time = 0

for can in reco:
    time += 1
    # 이미 나온 후보
    if can in photo:
        photo[can][0] += 1
    else:
        if len(photo) == N:
            # 젤 추천수 적고, 오래된 애 삭제
            de = min(photo.items(), key=lambda x: (x[1][0], x[1][1]))[0]
            del photo[de]
            q.remove(de)

        photo[can] = [1, time]
        q.append(can)
        
print(*sorted(photo.keys()))