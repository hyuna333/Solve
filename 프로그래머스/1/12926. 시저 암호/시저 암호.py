def solution(s, n):
    answer = ''
    for st in s:
        if st == ' ':
            answer += ' '
        elif ord(st) + n > 122:
            answer += chr(ord(st) + n - 26)
        elif ord(st) <= 90 and ord(st) + n >= 91:
            answer += chr(ord(st) + n - 26)
        else:
            answer += chr(ord(st) + n)
    return answer