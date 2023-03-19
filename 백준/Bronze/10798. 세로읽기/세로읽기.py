import sys

arr = [sys.stdin.readline().strip() for _ in range(5)]

N = 0
# 최대 길이 찾기
for st in arr:
    if N < len(st):
        N = len(st)

ans = ''
for i in range(N):
    for j in range(5):
        # 인덱스가 길이보다 크면 넘어간다
        if i >= len(arr[j]):
            continue
        else:
            ans += arr[j][i]

print(ans)