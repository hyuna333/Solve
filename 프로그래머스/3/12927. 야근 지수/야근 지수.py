def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0

    works.sort(reverse=True)

    while n > 0:
        mx = works[0]
        for i in range(len(works)):
            if works[i] == mx:
                works[i] -= 1
                n -= 1
                if n == 0:
                    break
        works.sort(reverse=True)
    
    answer = sum(work ** 2 for work in works)
    
    return answer