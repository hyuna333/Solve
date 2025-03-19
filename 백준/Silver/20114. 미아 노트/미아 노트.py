import sys
input = sys.stdin.readline

N, H, W = map(int, input().split())
ans = ['?']*N
for _ in range(H):
    st = list(input().strip())
    for i in range(len(st)):
        if st[i] != '?':
            ans[i//W] = st[i]

print(''.join(ans))