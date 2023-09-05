dct = {chr(i):i-96 for i in range(97, 123)}

N = int(input())
st = input()

sm = 0
for i in range(N):
    sm += dct[st[i]] * (31 ** i)

print(sm)