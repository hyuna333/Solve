def solution(arr):
    answer = []
    mn = min(arr)
    arr.remove(mn)
    answer = arr
    if not answer:
        answer = [-1]
    
    return answer