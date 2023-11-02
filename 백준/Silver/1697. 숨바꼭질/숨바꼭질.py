import sys
input = sys.stdin.readline

def tp(s):
    vi = [0] * 100001
    q = [(s, 0)]
    vi[s] = 1

    while q:
        now, t = q.pop(0)
        if now == K:
            return t

        for num in (2 * now, now - 1, now + 1):
            if 0 <= num <= 100000 and not vi[num]:
                vi[num] = 1
                q.append((num, t + 1))

N, K = map(int, input().split())

ans = tp(N)

print(ans)