lst = list(input())

dct = {chr(i):-1 for i in range(97, 123)}

for i in range(len(lst)):
    if dct[lst[i]] == -1:
        dct[lst[i]] = i

for n in dct.values():
    print(n, end=' ')