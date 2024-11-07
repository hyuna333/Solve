import sys
input = sys.stdin.readline

def fam(s, e):
    q = [s]
    vi = [0] * (n+1)
    vi[s] = 1

    while q:
        c = q.pop(0)
        if c == e:
            return vi[e]-1

        for i in arr[c]:
            if not vi[i]:
                vi[i] = vi[c] + 1
                q.append(i)
    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

ans = fam(a, b)
print(ans)