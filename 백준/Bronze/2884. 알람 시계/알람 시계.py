H, M = map(int, input().split())

if H == 0 and M < 45:
    H = 23
    M = 60 - (45-M)
elif M >= 45: M -= 45
elif M < 45 and H >= 1:
    M = 60 - (45-M)
    H -= 1

print(H, M)