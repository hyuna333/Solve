import sys
input = sys.stdin.readline

S = input()
ze = S.count('0') // 2
one = S.count('1')

tmp = S.replace('1', '', one//2)
ans = ''
for i in range(len(tmp)-1, -1, -1):
    if tmp[i] == '0' and ze:
        ze -= 1
    else:
        ans = tmp[i] + ans

print(ans)