import sys
input = sys.stdin.readline

def step(num, lst):
    score = [0] * num

    score[0] = lst[0]
    score[1] = lst[0] + lst[1]
    score[2] = max(lst[1]+lst[2], lst[0]+lst[2])

    for i in range(3, num):
        score[i] = max(score[i-3] + lst[i-1] + lst[i], score[i-2] + lst[i])

    return score[num-1]


num = int(input())
lst = []

for _ in range(num):
    tmp = int(input())
    lst.append(tmp)

if num == 1:
    ans = lst[0]
elif num == 2:
    ans = lst[0] + lst[1]
else:
    ans = step(num, lst)
print(ans)