import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    tn = max(lst)
    team = [[] for _ in range(tn+1)]
    ps = {n:lst.count(n) for n in range(1, tn+1)}

    sc = 1
    for i in range(N):
        if ps[lst[i]] == 6:
            team[lst[i]].append(sc)
            sc += 1

    score = []
    for j in range(tn+1):
        if len(team[j]) == 6:
            score.append((team[j], sum(team[j][:4]), j))

    score.sort(key=lambda x : (x[1], x[0][4]))
    print(score[0][2])