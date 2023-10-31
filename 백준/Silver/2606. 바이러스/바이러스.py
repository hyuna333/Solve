import sys
input = sys.stdin.readline

def virus(s):
    q = [s]
    vi[s] = 1

    ans = 0
    while q:
        n = q.pop(0)
        for num in lst[n]:
            if not vi[num]:
                q.append(num)
                vi[num] = 1
                ans += 1

    return ans

N = int(input())
V = int(input())

lst = [[] for _ in range(N+1)]
for _ in range(V):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

vi = [0] * (N+1)

print(virus(1))