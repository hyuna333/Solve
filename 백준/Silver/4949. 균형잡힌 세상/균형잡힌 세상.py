import sys

dct = {')': '(', ']': '['}

while True:
    st = sys.stdin.readline().rstrip()
    if st == '.':
        break

    lst = []
    ans = 'yes'

    for ch in st:
        if ch == '(' or ch == '[':
            lst.append(ch)
        elif ch == ')' or ch == ']':
            if lst:
                if lst[-1] == dct[ch]:
                    lst.pop()
                else:
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
    
    if lst:
        ans = 'no'
        
    print(ans)