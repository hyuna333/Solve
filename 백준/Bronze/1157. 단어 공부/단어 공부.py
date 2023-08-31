dct = {chr(i):0 for i in range(97, 123)}

st = input().lower()

for ch in st:
    dct[ch] += 1

mx = max(dct.values())
ans = ''

for i in dct.keys():
    if dct[i] == mx:
        if ans:
            ans = "?"
            break
        else:
            ans = i

print(ans.upper())