def solution(arr):
    answer = []
    
    now = arr[0]
    answer.append(now)
    for i in range(1, len(arr)):
        if arr[i] != now:
            answer.append(arr[i])
            now = arr[i]
        
    return answer