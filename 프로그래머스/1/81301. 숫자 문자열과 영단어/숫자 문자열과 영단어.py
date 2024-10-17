def solution(s):
    answer = 0
    dct = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    
    tmp = ''
    ans = ''
    for st in s:
        if not st.isdigit():
            tmp += st
            if tmp in dct.keys():
                ans += dct[tmp]
                tmp = ''
        else:
            ans += st
    
    answer = int(ans)
    return answer