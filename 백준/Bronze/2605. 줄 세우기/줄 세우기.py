import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
line = []
last = 0
num = 1

for i in lst:
    # 뽑은 숫자만큼 앞으로 땡겨서 저장해주기
    line.insert(last-i, num)
    last += 1
    num += 1

print(*line)