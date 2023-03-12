S = list(input())
alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dct = {}
for i in range(len(S)):
    if S[i] not in dct.keys():
        dct[S[i]] = i

for st in alpa:
    if st not in S:
        print(-1, end=' ')
    else:
        print(dct[st], end=' ')