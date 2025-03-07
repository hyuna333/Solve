import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = {i: {"le": -1, "ri": -1, "pa": -1} for i in range(1, N+1)}

for _ in range(N):
    pa, le, ri = map(int, input().split())
    if le != -1:
        tree[le]["pa"] = pa
        tree[pa]["le"] = le
    if ri != -1:
        tree[ri]["pa"] = pa
        tree[pa]["ri"] = ri

def dfs(c):
    global ans
    vi[c] = 1

    if tree[c]["le"] != -1 and not vi[tree[c]["le"]]:
        dfs(tree[c]["le"])
        ans += 1

    if tree[c]["ri"] != -1 and not vi[tree[c]["ri"]]:
        dfs(tree[c]["ri"])
        ans += 1

def ri(c):
    global cnt
    vi[c] = 1

    if tree[c]["ri"] != -1 and not vi[tree[c]["ri"]]:
        ri(tree[c]["ri"])
        cnt += 1


vi = [0]*(N+1)
ans = 0
dfs(1)

vi = [0]*(N+1)
cnt = 0
ri(1)

print(2*ans - cnt)