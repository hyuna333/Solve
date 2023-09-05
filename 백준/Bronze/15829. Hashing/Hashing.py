N = int(input())
st = input()

sm = 0
for i in range(N):
    sm += (ord(st[i])-96) * (31 ** i)

print(sm)