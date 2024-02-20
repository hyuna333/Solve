def yak(n):
    num = 0
    for i in range(1, int(n ** (1/2))+1):
        if n % i == 0:
            num += 1
            if i ** 2 != n:
                num += 1
    return num
        
def solution(number, limit, power):
    answer = 0
    lst = [0] * number
    for i in range(1, number+1):
        lst[i-1] = yak(i)
    
    for num in lst:
        if num > limit:
            answer += power
        else:
            answer += num
    return answer