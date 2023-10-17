import sys
input = sys.stdin.readline

N = int(input())

dct = {i:0 for i in range(-4000, 4001)}
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)
    dct[num] += 1

lst.sort()
# 산술평균
if sum(lst) >= 0:
    print(int(sum(lst) / N + 0.5))
else:
    print(int(sum(lst) / N - 0.5))
# 중앙값
print(lst[N // 2])
# 최빈값
mx = max(dct.values())
mx_lst = []

for i in dct:
    if dct[i] == mx:
        mx_lst.append(i)
if len(mx_lst) > 1:
    print(mx_lst[1])
else:
    print(mx_lst[0])
# 범위
print(max(lst) - min(lst))