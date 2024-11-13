import sys
input = sys.stdin.readline

def work(s):
    q = [s]
    ans = 0
    vi = [0]*(N+1)
    vi[s] = 1
    while q:
        c = q.pop(0)
        for n in lst[c]:
            if not vi[n]:
                q.append(n)
                ans += 1
                vi[n] = 1

    return ans



N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[b].append(a)

s = int(input())
print(work(s))