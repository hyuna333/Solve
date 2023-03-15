N = input().lower()

dct = {chr(i):0 for i in range(97, 123)}

for ch in N:
    dct[ch] += 1

mx = max(dct.values())
ans = ''

for alpha in dct.keys():
    if dct[alpha] == mx:
        if ans:
            ans = '?'
            break
        else:
            ans += alpha

print(ans.upper())