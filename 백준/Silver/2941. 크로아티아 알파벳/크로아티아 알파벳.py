word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

N = input()
n = len(N)

ans = 0
for i in range(n-1):
    if N[i:i+2] in word:
        ans += 1

for i in range(n-2):
    if N[i:i+3] in word:
        ans += 1

print(n-ans)