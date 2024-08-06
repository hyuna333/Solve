def solution(array):
    answer = 0
    st = ''.join(map(str, array))
    answer = st.count("7")
    
    return answer