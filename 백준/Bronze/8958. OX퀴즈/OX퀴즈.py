T = int(input())

for _ in range(T):
    case = list(input())

    score = 0
    ans = 0

    for i in range(len(case)):
        if case[i] == 'O':
            score += 1
            ans += score
        else:
            score = 0

    print(ans)