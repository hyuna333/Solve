N = int(input())

lst = list(map(int, input().split()))

M = max(lst)

scores = [x/M*100 for x in lst]

print(sum(scores)/N)