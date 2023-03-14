N, M = map(int, input().split())

box = [n for n in range(1, N+1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    chg = box[i-1:j]
    s = 0
    e = len(chg)
    m = e - (j-k)
    ans = chg[m-1:e] + chg[s:m-1]
    box = box[:i-1] + ans + box[j:]

print(*box)