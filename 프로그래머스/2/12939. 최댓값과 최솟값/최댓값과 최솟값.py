def solution(s):
    answer = ''
    lst = list(map(int, s.split()))
    mx = max(lst)
    mn = min(lst)
    answer = str(mn) + ' ' + str(mx)
    return answer