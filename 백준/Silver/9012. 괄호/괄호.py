import sys

N = int(sys.stdin.readline())
dct = {')':'(', ']':'['}

for _ in range(N):
    st = sys.stdin.readline()

    lst = []
    ans = 'YES'

    for ch in st:
        if ch == '(' or ch == '[':
            lst.append(ch)
        elif ch == ')' or ch == ']':
            if lst:
                if lst[-1] == dct[ch]:
                    lst.pop()
                else:
                    ans = 'NO'
                    break
            else:
                ans = 'NO'
                break
    if lst:
        ans = 'NO'

    print(ans)