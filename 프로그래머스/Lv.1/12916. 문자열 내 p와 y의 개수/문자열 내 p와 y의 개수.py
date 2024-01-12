def solution(s):
    answer = True
    st = s.lower()
    a = st.count('y')
    b = st.count('p')
    
    if a != b:
        answer = False
    return answer